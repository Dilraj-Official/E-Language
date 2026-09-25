{
  "language_spec": {
    "name": "E",
    "version": "1.0.0",
    "status": "Official Production Release",
    "type_system": "Dynamic with Explicit Casting Bounds",
    "execution_model": "Purely Interpreted (Python Hosted)",
    "abstraction_layer": "High-Level",
    "turing_complete": true
  },
  "architecture_matrix": {
    "program_isolation": {
      "entry_delimiter": "Start.ProjectName",
      "exit_delimiter": "End.ProjectName",
      "behavior": "Enforces isolated runtime. Any tokens situated outside these barriers are discarded immediately."
    },
    "variable_allocator": {
      "syntax": "var(identifier) = value",
      "supported_primitives": {
        "integer": "var(x) = 150",
        "quoted_string": "var(msg) = \"Stable Build\"",
        "bare_text_literal": "var(user) = Dilraj"
      },
      "special_mechanics": "Unquoted raw alphanumeric words are natively verified and captured as strings without casting faults."
    },
    "semantic_math_engine": {
      "syntax": "var.[operation_prefix] = identifierA.identifierB",
      "operators": {
        "var.add": "Addition / String Text Concatenation",
        "var.sub": "Algebraic Subtraction",
        "var.mult": "Algebraic Multiplication",
        "var.div": "Algebraic Division"
      },
      "crash_protection": "Division by zero intercepts are safely returned as an 'Undefined' state value token string."
    }
  },
  "advanced_subsystems": {
    "control_flow": {
      "syntax": "Statement.if [ if conditionA AND/OR conditionB then Action ]",
      "boolean_logical_operators": ["AND", "OR"],
      "comparison_operators": ["<", ">", "=="],
      "blueprint_example": "Statement.if [ if score == 2 AND check == yes then System.output: Print(\"Success\"); ]"
    },
    "iteration_engine": {
      "syntax": "System.repeat.loopX *times* - { Block }",
      "mechanics": "Runs a continuous loop exactly X times without requiring a manual indexing tracking increment register counter."
    },
    "vector_collections": {
      "syntax": "var.list(Identifier) = (element1, element2)",
      "positional_lookup": "Identifier.position0, Identifier.position1",
      "dynamic_modifiers": {
        "append_element": "Identifier.append(value);",
        "calculate_size": "var(size) = Identifier.length"
      }
    },
    "fault_isolation_barriers": {
      "syntax_try": "System.try [ Risky Operations Block ]",
      "syntax_catch": "System.catch [ Exception Handling Backup Block ]",
      "behavior": "Safeguards execution threads. Deflects severe software math exceptions smoothly to avoid application crash loops."
    },
    "disk_io_pipelines": {
      "syntax_write": "System.file.write(\"filename.txt\", (variable_identifier));",
      "behavior": "Streams active data payloads directly out into the physical hardware SSD storage space of the computer natively."
    }
  },
  "cross_platform_deployment_pipelines": {
    "macos": {
      "terminal_command": "python3 interpreter.py app.e",
      "double_click_launcher_payload": "osascript -e 'tell application \"Terminal\" to do script \"python3 $HOME/Desktop/E-Language/interpreter.py '\"$1\"'\"'"
    },
    "windows": {
      "terminal_command": "python interpreter.py app.e",
      "double_click_batch_payload": "@echo off\npython \"%~dp0interpreter.py\" \"%~1\"\npause"
    },
    "linux": {
      "terminal_command": "python3 interpreter.py app.e",
      "global_environment_alias": "alias e-lang='python3 ~/E-Language/interpreter.py'"
    }
  },
  "ide_integration_editor_specs": {
    "extension_folder_route": "~/.vscode/extensions/e-lang-support/syntaxes",
    "theme_highlighter_keywords": [
      "Start.\\w+",
      "End.\\w+",
      "Statement.if",
      "System.try",
      "System.catch",
      "System.repeat.loop",
      "Print",
      "System.output",
      "var\\(\\w+\\)",
      "var\\.\\w+"
    ]
  }
}
