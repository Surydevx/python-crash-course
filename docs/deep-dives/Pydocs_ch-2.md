# Python Tutorial 2: Using the Python Interpreter

## 1. Finding and Launching Python

The Python interpreter's binary is generally located at `/usr/local/bin/python3.14` in the file system. Other places are also possible since it depends on the installation path. For example, on Arch Linux, system packages are typically installed directly to `/usr/bin/python` or `/usr/bin/python3.14`.

> **Note:** Since I use ARCH BTW, I won't talk about MicroSlop, the main reason is I don't understand the Windows filesystem and have no respect or interest to learn. This opinion is solely mine and could change depending on various conditions.

The primary Python interpreter can be entered on the system via the command:

```bash
python

```

The interpreter session can be exited via the End-Of-File character (`Ctrl+D` on Unix) or by typing the command:

```python
quit()

```

The Python interpreter works somewhat like the Unix shell. When it's called with standard input connected to a tty device, it reads and executes commands interactively. When called with a file name argument or with a file as standard input, it reads and executes a *Python script* from that file.

---

## 2. Terminals, Shells, and TTYs (A Nerd's Note)

> **Note:** Let me explain what gibberish the upper paragraph is talking about, if you aren't a Linux nerd... probability is that you aren't.
> If you use Windows you gotta have Command Prompt or PowerShell? Yes, that's your terminal to be simple... though the originality of the above concept is concerned with the UNIX shell which is only present in UNIX-based operating systems like Berkeley Software Distribution (BSDs), MacOS which is kinda based on BSDs (BSD license permits the use), and finally GNU/LINUX (Yes, I fear meticulous perfectionists).
> In Linux Distributions (or simply Distro) you can install various terminals like Ghostty, Kitty, and Alacritty—there's a whole circus out there. What these terminals do is render graphs, handle font management, and take user input. They pass these commands to a pseudo-terminal called a `pty` (it is what it is man...) which acts as an emulation layer over traditional physical hardware TTY devices.
> I don't know about MacOS, though they have a terminal named `Terminal` and I am assuming this would work similarly, but good luck installing other terminals (Maybe you could get homebrew and try out different terminals).
> The main deal is the Shell. You have a lot of options for shells: Bash (default for many Linux distros), Zsh (feature-rich and loved by many Linux nerds—also Tim Cook, yes, I am not joking, MacOS defaults to Zsh in its terminal emulator named `Terminal`), fish, PowerShell (I wanted to ignore this MicroSlop badly but, it is what it is) and other less popular options are there like Korn Shell, csh, tcsh, and a whole list of World War 2 relics you can totally avoid.
> The shell here is what processes your input, conveys your input to the kernel, and does all types of gymnastics.

*Tired? Jal lijiye!* 🥛

---

## 3. Running Python Code

Let's talk not-so-routine things. You run a Python program by writing it in a text editor like VSCode, Vim, NVim, Emacs, Sublime Text, IntelliJ IDEA, or whatever you want, and then typing the command:

```bash
python script.py # Note that the name could be python3.14 depending on how it was installed.

```

Alternatively, you can just enter the Python interpreter, also called the **REPL** (Read-Evaluate-Print-Loop), which basically means a simple computer program that is interactive (takes a single input and spits the output after processing).

The third option is running Python code directly from the command line as a string:

```bash
python -c "Your python code goes here" [arg] ... # The ellipsis means more flags can be used.

```

Understand that the command should be inside quotes because your code could contain characters which are meaningful to the shell, and thus the shell could hijack your program to interpret its own meaning.

```bash
python -c "import sys; print(f'Hello, {sys.argv[1]}!')" surya 
# 'surya' is the argument stored in the sys.argv variable (which is a list)

```

---

## 4. Modules Used as Commands (`-m`)

To use modules from the terminal rather than importing them into a file, we can use the following command:

```bash
python -m <module_name> [arg]

```

Where the `-m` flag represents the module name. What this command does is find the module path under the directories listed in the variable `sys.path`, and then executes the module. Several Python package managers install the executable of the package, though using it through the `-m` flag is safer.

Here is how it resolves:

* **If `module_name.py` is a single file:** Python executes `module_name.py` directly.
* **If `module_name.py` is a directory/folder:** Python looks for a file named `__main__.py` inside that directory and executes it.

By the way, wanna see what `sys.path` looks like? Have it your way... it's just a list as you can see:

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python314.zip', '/usr/lib/python3.14', '/usr/lib/python3.14/lib-dynload', '/usr/lib/python3.14/site-packages']
>>>

```

**Why using the `-m` flag is safer:**
The reason is **Exact Environment Targeting**. If we have multiple Python versions installed (e.g., Python 3.10 and 3.12, or a virtual environment), running `pip install` might use the wrong Python version. Running `python3.12 -m pip install` guarantees that `pip` installs the package specifically into Python 3.12.

**Wanna see magic?**

```bash
# Start a local HTTP web server serving in the current directory
python -m http.server 8000

# Format a JSON file/string
python -m json.tool data.json

# Create a brand new virtual environment
python -m venv myenv

# Inspect performance/benchmarks of a statement
python -m timeit "'-'.join(str(n) for n in range(100))"

```

Okay, it ain't magic. Don't blame my little soul for over-exciting.

> **Note:** For most Python tools, `/usr/local/bin/yada-yada` is **not** the actual core binary of `yada-yada`—it is just a tiny generated wrapper script. Yk now... this cursed knowledge will live on with you.

---

## 5. Argument Passing (`sys.argv`)

Whatever argument is passed to the script gets converted to a list and assigned to a variable called `sys.argv`. If there are no arguments given, the length of the list is 1, and `sys.argv[0] = ''` (an empty string).

| How You Launch Python | Command Example | Value of `sys.argv[0]` | Explanation |
| --- | --- | --- | --- |
| **Interactive (REPL)** | `python` | `''` (empty string) | Launched with no arguments; opens the interactive shell. |
| **Standard Script** | `python app.py` | `'app.py'` | The path/filename of the script. |
| **Standard Input (`-`)** | cat script.py | python - | `'-'` | Directs Python to read code from standard input (stdin). |
| **Command String (`-c`)** | `python -c "import sys; print(sys.argv[0])"` | `'-c'` | Tells you the code was executed directly from an inline string command. |
| **Module Execution (`-m`)** | `python -m http.server` | *Full absolute path* | The resolved absolute file path of the located module's `__main__.py` on your system. |

---

## 6. The REPL (Interactive Mode)

This is also called the interactive Read Eval Print Loop. That is, it's an interactive Python interpreter. It kind of behaves like a terminal/shell on its own. In interactive mode, the commands are read from a TTY shell.

By the way, we can even change the default `>>>` and `...` prompts to our liking. They are just variables stored in the `sys` module.

```python
import sys
sys.ps1 = "surya the lord> "
sys.ps2 = "                ... "

```

Now every time Python waits for my input, it will bow to `surya the lord>`.

> **Technical Note:** `sys.ps1` and `sys.ps2` are only defined if the interpreter is in interactive mode. If you try to print them from inside a script file, Python will throw an error!

---

## 7. Source Encoding & UTF-8

By default, Python source files are treated as encoded in UTF-8.

**WTF is UTF-8?**

> To understand what UTF-8 is, we need to understand what source encoding is.
> Source encoding is the process of translating human-readable characters into digital binary code (1s and 0s) so a computer can store, process, and display the text correctly. To do this process, we initially had ASCII. You can assume ASCII is a kind of dictionary (not a Python dictionary, but an actual language dictionary) which holds the character name and the corresponding number for it. This number gets converted to binary sequences in computers.
> The limitation was that ASCII only had 128 characters, and that only supported English. So it was kind of weird for the rest of the world. Now, we have UTF-8 source encoding, which supports almost every character in the world (provided that your fonts are capable; yk some fonts just can't represent some emojis, or Japanese/Chinese characters).

In UTF-8 encoding, characters of most languages in the world can be used simultaneously in string literals, identifiers, and comments—although the standard library only uses ASCII characters for identifiers, a convention that any portable code should follow. To display all these characters properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the characters in the file.

### ASCII vs Bytes (The Genius of UTF-8)

ASCII takes exactly 7 bits for each type of character in source code. However, computers don't store memory in 7-bit chunks; they store memory in 8-bit bytes. So, an ASCII character still takes up 1 full byte (8 bits) of disk space. It just leaves the very first bit empty (it's always a `0`).

This is exactly where the genius of UTF-8 comes into play:

* UTF-8 looks at that first bit. If it's a `0`, UTF-8 says: *"Ah, this is just plain old ASCII. I'll only read this 1 byte."*
* If you use a Japanese Kanji or an emoji, UTF-8 flips that first bit to a `1`, which tells the computer: *"Hey! Stop! This is a big character, you need to read the next 2, 3, or 4 bytes to figure out what it is!"*

Because of this, if you aren't using Japanese/Korean/Mandarin in your code, an English Python script encoded in UTF-8 is byte-for-byte identical to the exact same script encoded in ASCII. No extra memory is wasted. Otherwise, it can take 1 to 4 bytes to represent a heavier character in memory.

### Summary of Encoding Rules:

* **Python 3 Default:** Yes, since Python 3.0, all source code is assumed to be UTF-8 by default.
* **Font vs. Encoding:** This is a crucial distinction that many beginners miss. The *encoding* tells the computer what character it is (the bytes); the *font* tells the screen how to draw it (the glyph). If the font lacks the glyph, you get the dreaded "tofu" (those empty little rectangles ▯).
* **Portable Code (PEP 8):** Even though Python allows you to name a variable `उम्र = 25` or `résumé = True`, the official style guide (PEP 8) strongly dictates using only standard ASCII for variables, functions, and classes so anyone anywhere can read and type your code.

### Declaring a Custom Encoding

To declare an encoding other than the default one, a special comment line should be added as the **first line** of the file. The syntax is as follows:

```python
# -*- coding: encoding -*-

```

where `encoding` is one of the valid codecs supported by Python.

For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:

```python
# -*- coding: cp1252 -*-

```

One exception to the first-line rule is when the source code starts with a UNIX "shebang" line. In this case, the encoding declaration should be added as the **second line** of the file. For example:

```python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-

```

;) done.