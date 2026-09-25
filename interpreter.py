
import re
import sys
import os


class E_Interpreter_v1:
    def __init__(self):
        self.variables = {}
        self.in_project = False

    def parse_value(self, token):
        token = token.strip()

        if not token:
            return ""

        if (
            (token.startswith('"') and token.endswith('"'))
            or (token.startswith("'") and token.endswith("'"))
        ):
            return token[1:-1]

        if token.isdigit():
            return int(token)

        if token in self.variables:
            return self.variables[token]

        return token

    def execute_print(self, print_content, line_num):
        parts = []

        tokens = re.findall(
            r'(?:[^\s,"]|"(?:\\.|[^"])*"|\'(?:\\.|[^\'])*\'|[\w.]+\.position\d+|[\w.]+\.length)+',
            print_content
        )

        for token in tokens:
            token = token.strip()

            if ".position" in token:
                match = re.match(r"([\w.]+)\.position(\d+)", token)

                if match:
                    list_name, idx_str = match.groups()
                    idx = int(idx_str)

                    if (
                        list_name in self.variables
                        and isinstance(self.variables[list_name], list)
                    ):
                        if idx < len(self.variables[list_name]):
                            parts.append(str(self.variables[list_name][idx]))
                        else:
                            raise IndexError("List index out of bounds.")
                    else:
                        raise NameError(
                            f"List '{list_name}' not initialized."
                        )

                continue

            if ".length" in token:
                list_name = token.split(".length")[0].strip()

                if (
                    list_name in self.variables
                    and isinstance(self.variables[list_name], list)
                ):
                    parts.append(str(len(self.variables[list_name])))
                else:
                    parts.append("0")

                continue

            if token.startswith("(") and token.endswith(")"):
                inner = token[1:-1].strip()
                parts.append(str(self.parse_value(inner)))
            else:
                parts.append(str(self.parse_value(token)))

        print(" ".join(parts))

    def evaluate_condition(self, cond_str):
        if " AND " in cond_str:
            sub_conds = cond_str.split(" AND ")
            return (
                self.evaluate_single_condition(sub_conds[0])
                and self.evaluate_single_condition(sub_conds[1])
            )

        if " OR " in cond_str:
            sub_conds = cond_str.split(" OR ")
            return (
                self.evaluate_single_condition(sub_conds[0])
                or self.evaluate_single_condition(sub_conds[1])
            )

        return self.evaluate_single_condition(cond_str)

    def evaluate_single_condition(self, cond):
        comp = re.match(
            r"(\w+)\s*(<|>|==)\s*(\w+)",
            cond.strip()
        )

        if comp:
            v1_name, op, v2_name = comp.groups()

            v1 = self.parse_value(v1_name)
            v2 = self.parse_value(v2_name)

            if op == "<":
                return v1 < v2

            if op == ">":
                return v1 > v2

            if op == "==":
                return v1 == v2

        return False

    def execute_block(self, lines):
        i = 0

        while i < len(lines):
            line = lines[i].strip()
            line_num = i + 1

            if not line or line.startswith("//"):
                i += 1
                continue

            if line.startswith("Start."):
                self.in_project = True
                i += 1
                continue

            if line.startswith("End."):
                self.in_project = False
                i += 1
                continue

            if not self.in_project:
                i += 1
                continue

            # System.file.write
            if line.startswith("System.file.write"):
                match = re.match(
                    r"System\.file\.write\((.*?)\s*,\s*(.*?)\);?$",
                    line
                )

                if match:
                    filepath = self.parse_value(
                        match.group(1).strip()
                    )

                    data_var = (
                        match.group(2)
                        .strip()
                        .strip("()")
                        .strip()
                    )

                    payload = str(self.parse_value(data_var))

                    with open(filepath, "w") as f:
                        f.write(payload)

                i += 1
                continue

            # List append
            if ".append(" in line:
                match = re.match(
                    r"([\w.]+)\.append\((.*?)\);?",
                    line
                )

                if match:
                    list_name, item_raw = match.groups()

                    if (
                        list_name in self.variables
                        and isinstance(self.variables[list_name], list)
                    ):
                        self.variables[list_name].append(
                            self.parse_value(item_raw)
                        )

                i += 1
                continue

            # System.try / System.catch
            if line.startswith("System.try ["):
                try_body = []
                i += 1
                bc = 1

                while i < len(lines) and bc > 0:
                    if "System.try [" in lines[i]:
                        bc += 1

                    if "]" in lines[i] and "System.catch" not in lines[i]:
                        bc -= 1

                    if bc > 0:
                        try_body.append(lines[i])

                    i += 1

                catch_body = []

                if i < len(lines) and "System.catch [" in lines[i]:
                    i += 1
                    cb = 1

                    while i < len(lines) and cb > 0:
                        if "]" in lines[i]:
                            cb -= 1

                        if cb > 0:
                            catch_body.append(lines[i])

                        i += 1

                try:
                    self.execute_block(try_body)
                except Exception:
                    self.execute_block(catch_body)

                continue

            # Repeat loop
            if line.startswith("System.repeat.loop"):
                match = re.match(
                    r"System\.repeat\.loop(\d+)\s*\*\*times\*\s*-\s*\{",
                    line
                )

                if match:
                    times = int(match.group(1))

                    loop_body = []
                    i += 1
                    brace_count = 1

                    while i < len(lines) and brace_count > 0:
                        if "{" in lines[i]:
                            brace_count += 1

                        if "}" in lines[i]:
                            brace_count -= 1

                        if brace_count > 0:
                            loop_body.append(lines[i])

                        i += 1

                    for _ in range(times):
                        self.execute_block(loop_body)

                continue

            # Statement.if
            if line.startswith("Statement.if"):
                if "[" in line:
                    if_body = []
                    i += 1

                    while (
                        i < len(lines)
                        and lines[i].strip() != "]"
                    ):
                        if_body.append(lines[i])
                        i += 1

                    for if_line in if_body:
                        if_line = if_line.strip()

                        if (
                            if_line.startswith("if ")
                            and " then " in if_line
                        ):
                            match = re.match(
                                r"if\s+(.*?)\s+then\s+(.*)",
                                if_line
                            )

                            if match:
                                cond, action = match.groups()

                                if self.evaluate_condition(cond):
                                    if "System.output:" in action:
                                        print_cmd = action.split(
                                            "System.output:",
                                            1
                                        )[1].strip()

                                        if print_cmd.startswith("Print"):
                                            self.execute_print(
                                                print_cmd
                                                .rstrip(";")
                                                .strip()[6:-1],
                                                line_num
                                            )

                                    elif "=" in action:
                                        v_n, v_r = action.split("=", 1)

                                        v_n = (
                                            v_n
                                            .strip()
                                            .replace("var(", "")
                                            .replace(")", "")
                                        )

                                        self.variables[v_n] = (
                                            self.parse_value(v_r)
                                        )

                    i += 1
                    continue

            # var.list(...)
            if line.startswith("var.list("):
                match = re.match(
                    r"var\.list\((.*?)\)\s*=\s*(.*)",
                    line
                )

                if match:
                    list_name, values = match.groups()

                    self.variables[list_name.strip()] = [
                        int(e.strip())
                        if e.strip().isdigit()
                        else e.strip().strip("'\"")
                        for e in values.split(",")
                    ]

                i += 1
                continue

            # Syntax.System.input
            if "=(Syntax).System.input" in line.replace(" ", ""):
                match = re.match(
                    r"var\((.*?)\)\s*=\s*Syntax\.System\.input(.*)",
                    line
                )

                if match:
                    v_name, args_raw = match.groups()

                    arg_tokens = re.findall(
                        r'(?:[^\s,"]|"(?:\\.|[^"])*"|\'(?:\\.|[^\'])*\')+',
                        args_raw
                    )

                    prompt = (
                        arg_tokens[0]
                        .strip()
                        .strip("'\"")
                        if arg_tokens
                        else ""
                    )

                    type_token = (
                        arg_tokens[1].strip()
                        if len(arg_tokens) > 1
                        else ""
                    )

                    resp = input(f"{prompt} ")

                    if "(Int.input)" in type_token and resp.isdigit():
                        self.variables[v_name.strip()] = int(resp)
                    else:
                        self.variables[v_name.strip()] = resp

                i += 1
                continue

            # var.add / var.sub / var.mult / var.div
            if line.startswith("var."):
                match = re.match(
                    r"var\.(.*?)\s*=\s*(.*)",
                    line
                )

                if match:
                    op, expr = match.groups()
                    dest = f"var.{op}"

                    if "." in expr:
                        parts = [
                            p.strip()
                            for p in expr.split(".")
                        ]

                        vals = [
                            self.parse_value(p)
                            for p in parts
                        ]

                        if len(vals) >= 2:
                            if op == "add":
                                if (
                                    isinstance(vals[0], int)
                                    and isinstance(vals[1], int)
                                ):
                                    self.variables[dest] = (
                                        vals[0] + vals[1]
                                    )
                                else:
                                    self.variables[dest] = (
                                        f"{vals[0]}{vals[1]}"
                                    )

                            elif op == "sub":
                                self.variables[dest] = (
                                    vals[0] - vals[1]
                                )

                            elif op == "mult":
                                self.variables[dest] = (
                                    vals[0] * vals[1]
                                )

                            elif op == "div":
                                if vals[1] == 0:
                                    raise ZeroDivisionError(
                                        "Cannot divide by zero."
                                    )

                                self.variables[dest] = (
                                    vals[0] / vals[1]
                                )

                i += 1
                continue

            # var(...)
            if line.startswith("var("):
                match = re.match(
                    r"var\((.*?)\)\s*=\s*(.*)",
                    line
                )

                if match:
                    var_name, value = match.groups()

                    self.variables[var_name.strip()] = (
                        self.parse_value(value.strip())
                    )

                i += 1
                continue

            # Print
            if line.startswith("Print") or "System.output:" in line:
                p_ln = (
                    line.split("System.output:", 1)[1].strip()
                    if "System.output:" in line
                    else line
                )

                if p_ln.startswith("Print"):
                    self.execute_print(
                        p_ln.rstrip(";").strip()[6:-1],
                        line_num
                    )

                i += 1
                continue

            i += 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as file:
            source_code = file.readlines()

        E_Interpreter_v1().execute_block(source_code)
