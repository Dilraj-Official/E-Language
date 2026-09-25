# 🚀 The E Programming Language (Official Production Version 1.0.0)

Welcome to **E**, a robust, high-level, explicitly typed interpreted programming language engineered for cross-platform execution. **E** combines clear block structure rules with an intuitive semantic mathematical engine, multi-condition evaluation branches, data collection vectors, and crash-safeguarding error handlers.

---

## 🏛️ 1. Core Language Architecture Spec Matrix

| Feature Module | Code Syntax Implementation Example | Execution Behavioral Mechanics |
| :--- | :--- | :--- |
| **Workspace Bounds** | `Start.App` ... `End.App` | Code outside explicitly declared project containers is discarded. |
| **Dynamic Allocations**| `var(name) = Dilraj` | Automatically parses numeric types, standard strings, and raw bare text. |
| **Semantic Calculations**| `var.mult = a.b` | Operations are dictated by assignment prefixes, avoiding PEMDAS precedence errors. |
| **Logic Brackets** | `Statement.if [ if a > b AND c == yes then ... ]` | Supports inline actions or variables updates using unified uppercase operators (`AND`, `OR`). |
| **Iteration Loops** | `System.repeat.loop5 *times* - { ... }` | Executes continuous loops efficiently without needing loop counter index trackers. |
| **Vector Collections** | `var.list(Data) = (10, 20)` → `Data.position0` | Creates array tracking registers and fetches target index elements natively. |
| **Dynamic Arrays** | `Data.append(30);` → `var(t) = Data.length` | Appends elements onto lists dynamically and calculates list sizes on the fly. |
| **Fault Protection** | `System.try [ ... ] System.catch [ ... ]` | Prevents runtime crashes by trapping exceptions like zero division errors. |
| **Disk Operations** | `System.file.write("log.txt", (var));` | Streams variable payloads directly out onto your machine's physical storage disk. |

---

## 💻 2. Complete Execution & Setup Guide Across All Operating Systems

Because **E** is engineered as a hosted scripting infrastructure running on top of **Python 3**, it can be executed seamlessly on any desktop ecosystem.

### 🍏 A. macOS (Apple Silicon M-Series & Intel)

#### 1. Setup Your Command Environment
Open your native **Terminal** app (`Cmd + Space`, search `Terminal`) and verify Python 3 is installed:
```bash
python3 --version
```
*If not found, download and install the official package manager from [Python.org](https://python.org).*

#### 2. Manual Command Line Execution
Change directory (`cd`) to your working path folder containing your source files and pass your script asset path directly to the interpreter core:
```bash
cd Desktop/E-Language
python3 interpreter.py app.e
```

#### 3. Configuring Double-Click Automated Execution
To make your `.e` scripts automatically open the Terminal window and execute upon double-clicking:
1. Open the built-in **Automator** app on your Mac and select **New Document** → **Application**.
2. Search for **Run Shell Script**, double-click it, and switch the *Pass input* dropdown configuration to **as arguments**.
3. Paste this command inside the text execution window box:
   ```bash
   osascript -e 'tell application "Terminal" to do script "python3 $HOME/Desktop/E-Language/interpreter.py '"$1"'"'
   ```
4. Save the file inside your Applications folder named **`Run_E_Lang`**.
5. Find your `app.e` file in Finder, right-click it, select **Get Info**, expand **Open with:**, choose your new `Run_E_Lang` app, and click **Change All...**.

---

### 🪟 B. Microsoft Windows (Windows 10 & 11)

#### 1. Setup Your Command Environment
1. Download and run the native installer from [Python.org](https://python.org). 
2. **CRITICAL:** Check the box at the bottom of the installer wizard page that says **"Add python.exe to PATH"** before clicking install.
3. Open **Command Prompt** (`Win + R`, type `cmd`, hit Enter) and check installation safety flags:
   ```cmd
   python --version
   ```

#### 2. Manual Command Line Execution
Navigate to your specific directory folder location path and invoke the host engine:
```cmd
cd C:\Users\YourUsername\Desktop\E-Language
python interpreter.py app.e
```

#### 3. Configuring Double-Click Automated Execution
To make your `.e` source text scripts compile and execute automatically when double-clicked on Windows:
1. Create a brand new blank text document in your folder named exactly **`run.bat`**.
2. Open it in a text editor and paste this single line batch loop automation script:
   ```batch
   @echo off
   python "%~dp0interpreter.py" "%~1"
   pause
   ```
3. Save and close the file.
4. Right-click your `app.e` data file, choose **Open with** → **Choose another app**.
5. Browse your computer, select your new **`run.bat`** script, check the box that says **"Always use this app to open .e files"**, and click OK.

---

### 🐧 C. Linux (Ubuntu, Debian, Fedora, Arch)

#### 1. Setup Your Command Environment
Open your terminal window console and verify the compiler hosting parameters are configured:
```bash
sudo apt update && sudo apt install python3 python3-pip -y
```

#### 2. Command Line Execution
```bash
cd ~/E-Language
python3 interpreter.py app.e
```

#### 3. Creating a System Alias Link Shortcut
To make your custom language a globally accessible native terminal bin command option anywhere inside your operating filesystem, run this configuration route wrapper rule:
```bash
echo "alias e-lang='python3 ~/E-Language/interpreter.py'" >> ~/.bashrc
source ~/.bashrc
```
Now, you can execute any script anywhere on your Linux system by typing:
```bash
e-lang app.e
```

---

## 🎨 3. IDE Integration: Visual Studio Code Custom Styling

To unlock automatic space indentation formatting and keyword color code highlights:
1. Open your Mac Terminal app and execute this folder tree creation route:
   ```bash
   mkdir -p ~/.vscode/extensions/e-lang-support/syntaxes
   ```
2. Place your `package.json`, `language-configuration.json`, and `syntaxes/e.tmLanguage.json` schema metadata documents straight inside that directory layout path workspace.
3. Restart **VS Code** to immediately run your custom language highlight themes live!
