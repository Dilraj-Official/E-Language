
## THE OFFICIAL REFERENCE MANUAL: THE E PROGRAMMING LANGUAGE (VERSION 1.0.0)
E is a high-level, explicitly typed, purely interpreted, Turing-complete programming language engineered for readable, predictable, and structurally isolated execution. By intentionally eliminating traditional mathematical operator symbols and loop syntax constraints, E delivers an explicit, narrative-driven codebase that prevents standard parsing ambiguities such as PEMDAS precedence errors or index-tracking bugs.
------------------------------
## 1. SYSTEM SPECIFICATION MATRIX

* Workspace Bounds Perimeter
Syntax Variant: Start.ProjectName ... End.ProjectName
Execution Behavior: Enforces an isolated runtime workspace. Any lines or text tokens situated outside these strict barriers are discarded immediately by the lexical analyzer.
* Memory Data Allocations
Syntax Variant: var(variable_name) = value
Execution Behavior: Initializes a memory state tracking register pointer. Dynamically parses and detects integer integers, standard quoted strings, and unquoted Bare Text.
Special Mechanics: Unquoted raw alphanumeric words are natively verified and captured as strings without throwing casting validation faults.
* The Prefix Semantic Math Processor
Syntax Variant: var.[operation_prefix] = identifierA.identifierB
Execution Behavior: Evaluates mathematical equations strictly based on destination prefixes, avoiding PEMDAS operational precedence errors.
var.add -> Handles mathematical addition or string text sequence concatenation.
var.sub -> Handles algebraic subtraction.
var.mult -> Handles algebraic multiplication.
var.div -> Handles algebraic division (Safely yields Undefined if the denominator parameter is 0).
* Chained Conditional Logic
Syntax Variant: Statement.if [ if conditionA AND/OR conditionB then Action ]
Execution Behavior: Evaluates complex boolean criteria checks wrapped in square brackets using unified uppercase operators (AND, OR).
* Control Iteration Loops
Syntax Variant: System.repeat.loopX times - { Block }
Execution Behavior: Runs a continuous loop exactly X times sequentially without requiring a manual indexing increment array tracking counter.
* Vector Indexing Collections
Syntax Variant: var.list(Identifier) = (element1, element2)
Execution Behavior: Allocates a storage array tracking register and retrieves individual elements via a static zero-indexed dot-notation lookup.
Example Lookup: Identifier.position0, Identifier.position1
* Dynamic Arrays Modifiers
Syntax Variant: Identifier.append(value);
Execution Behavior: Appends data elements to an existing list array at runtime dynamically.
Size Computation Syntax: var(size) = Identifier.length
* Fault Interception Protection Barriers
Syntax Variant: System.try [ Risky Code Block ] System.catch [ Backup Failure Block ]
Execution Behavior: Establishes a crash-safeguard environment trap. Captures severe math exceptions or input casting issues smoothly without crashing the active execution thread.
* Direct Hard Drive Disk Operations
Syntax Variant: System.file.write("filename.txt", (variable_identifier));
Execution Behavior: Streams active variable data payloads directly out into the physical hardware storage space of your MacBook Air's SSD natively.

------------------------------
## 2. REUSE SYNTAX SPECS & BLUEPRINTS## 2.1 Memory Variables & The Bare-Text Evaluator
var(username) = Dilraj
var(releaseYear) = 2026
var(greeting) = "Hello World"
## 2.2 The Prefix Math Engine
var(x) = 100
var(y) = 25
var.add = x.y // Evaluates to: 125
var.sub = x.y // Evaluates to: 75
var.mult = x.y // Evaluates to: 2500
var.div = x.y // Evaluates to: 4.0
## 2.3 Chained Conditional Evaluations
Statement.if [
if status == Verified AND rank == Champion then System.output: Print("Access Granted.");
]
## 2.4 Lists & Dynamic Append Registers
var.list(Inventory) = (Sword, Shield, Potion)
System.output: Print("First Item:", Inventory.position0);
Inventory.append(M4_Air_Laptop);
var(inventorySize) = Inventory.length
------------------------------
## 3. PLATFORM CONFIGURATION & LAUNCH PIPELINES## 3.1 macOS Deployment (Apple Silicon M1-M4 & Intel Core)

   1. Verify Python 3 is active via your terminal window console:
   python3 --version
   2. Navigate to your project folder location path and execute via command:
   cd ~/Desktop/E-Language
   python3 interpreter.py app.e
   3. Double-Click Automation Launcher Setup:
   * Open the built-in Automator app on your Mac and select New Document -> Application.
      * Add a Run Shell Script block module and change the Pass input dropdown configuration to as arguments.
      * Paste this exact directory command inside the script window block box:
      osascript -e 'tell application "Terminal" to do script "python3 $HOME/Desktop/E-Language/interpreter.py '"$1"'"'
      * Save the file inside your Applications directory folder named Run_E_Lang.
      * Locate your app.e script file in Finder, right-click it, choose Get Info, expand the Open with: panel, choose your Run_E_Lang app, and hit Change All...
   
## 3.2 Microsoft Windows Deployment (Windows 10 & 11)

   1. Install Python 3 via the official executable installer setup wizard. Ensure you check the box that says "Add python.exe to PATH" before clicking install.
   2. Launch your Command Prompt and navigate to your working directory folder location path:
   cd C:\Users\YourUsername\Desktop\E-Language
   python interpreter.py app.e
   3. Double-Click Automation Launcher Setup:
   * Create a text file named run.bat inside your project directory.
      * Open it in a text editor and paste this execution batch file script:
      @echo off
      python "%~dp0interpreter.py" "%~1"
      pause
      * Save and close the file. Right-click your app.e script file, select Open with -> Choose Another App -> Browse and target your new run.bat script file. Check "Always use this app to open .e files".
   
## 3.3 Linux Deployment Systems (Ubuntu, Debian, Fedora, Arch)

   1. Initialize the prerequisite system runtime components:
   sudo apt update && sudo apt install python3 -y
   2. Run your script files via terminal command entries:
   python3 interpreter.py app.e
   3. Setting a Global Environment Alias Link Shortcut:
   echo "alias e-lang='python3 ~/E-Language/interpreter.py'" >> ~/.bashrc
   source ~/.bashrc
   Now execute your custom language anywhere globally by typing:
   e-lang app.e

------------------------------
## 4. VS CODE EDITOR INTEGRATION CODES & SPECS
To unlock automatic space indentation formatting and keywords color code highlights, open your Mac terminal and create this local extension folder path layout:
mkdir -p ~/.vscode/extensions/e-lang-support/syntaxes
Create these three structural control mapping documents directly inside that path:
## 4.1 Document 1: package.json
{
"name": "e-lang-support",
"displayName": "E Language Support",
"description": "Syntax highlighting and auto-spacing for the E language",
"version": "1.0.0",
"engines": { "vscode": "^1.80.0" },
"categories": [ "Programming Languages" ],
"contributes": {
"languages": [{
"id": "e",
"aliases": ["E", "e"],
"extensions": [".e"],
"configuration": "./language-configuration.json"
}],
"grammars": [{
"language": "e",
"scopeName": "source.e",
"path": "./syntaxes/e.tmLanguage.json"
}]
}
}
## 4.2 Document 2: language-configuration.json
{
"comments": { "lineComment": "//" },
"brackets": [ ["{", "}"], ["[", "]"], ["(", ")"] ],
"autoClosingPairs": [
{ "open": "{", "close": "}" },
{ "open": "[", "close": "]" },
{ "open": "(", "close": ")" },
{ "open": """, "close": """ }
],
"indentationRules": {
"increaseIndentPattern": "(\{|\[|Start\..|System\.output:|Statement\.if \[)$", "decreaseIndentPattern": "^(\s)(}\vert{}\]|End\..*)$"
}
}
## 4.3 Document 3: syntaxes/e.tmLanguage.json
{
"$schema": "githubusercontent.com",
"name": "E",
"patterns": [
{ "name": "comment.line.double-slash.e", "match": "//.*$" },
{ "name": "keyword.control.e", "match": "\b(Start\.\w+|End\.\w+|Statement\.if|System\.try|System\.catch|System\.repeat\.loop)\b" },
{ "name": "support.function.e", "match": "\b(Print|System\.output)\b" },
{ "name": "variable.parameter.e", "match": "var\(\w+\)|var\.\w+" },
{ "name": "string.quoted.double.e", "begin": """, "end": """, "patterns": [{ "name": "constant.character.escape.e", "match": "\\." }] }
],
"scopeName": "source.e"
}
------------------------------
