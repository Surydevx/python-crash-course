The python interpreter's binary is generally located at `/usr/local/bin/python3.14` in the file system.
Other places  are also possible since it depends upon the installation path and so you could find the binary also at `/usr/local/python` 

> Note: Since i use ARCH BTW, i won't talk about MicroSLop, the main reason is i don't understand the windows filesystem and have no respect or interest to learn, this opinion is soulely mine and could be change depends on various conditions.

The primary python interpreter can be entered on the system via the command: 

```
python
```
 and the interpreter session can be exited via the End-Of -File character `Ctrl+D` or typing the command:
 
 ```
 quit()
 ```

The python interpreter works somewhat like the Unix shell ( Also can be understood as a terminal), that's when it's called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a _python script_ from that file.

> Note: Let me explain what gibberish the upper paragraph is talking about, if you aren't a linux nerd...probability is that you aren't.
> if you use windows you gotta have command prompt or powershell? yes, that's your terminal to be simple...though the originality of the above concept is concerned with the UNIX shell which is only present in UNIX based  operating systems like Berkeley Software Distribution (BSD's), MacOS which is kinda based on BSD's ( BSD license permits the use), and finally GNU/LINUX (Yes, i fear Meticulous perfectionists.)
> 
> In Linux Distributions (or simply Distro) you can install various terminals Like Ghostty, Kitty and Alacritty there's a whole circus out there. what these terminal does is rendering graphs, and handling font managements and user input and they pass these commands to a pseudo terminal called pty (it is what it is man...) which acts as an emulation layer over traditional physical hardware TTY devices.
> 
>  I don't know about MacOS, though they have a terminal named `Terminal`  and  i am assuming this would work similar but good luck installling other terminals (Maybe you could get homebrew and try out different terminals)
>  
> The main deal is Shell, you have kind of a lot of options for shell Bash(default for many linux distro's), Zsh(feature rich and loved by many llinux nerd's also Tim cook yess, i am not joking, MacOS Defaults to Zsh in it's terminal emulator named `Terminal` ), fish, powershell (I wanted to ignore this MIcroslop badly but, it is what it is. ) and other less popular options are there like Korn Shell, csh, tcsh ad whole list of world war 2 relics, you can totally avoid them.
> The shells here what processes your input and convey your input to kernel and does all types of gymnastics.

Tired? jal lijiye !

Let's Talk not so routine tthings...
You run a python progamme by either writing it in a text editor like Vscode, vim or NVim , Emacs, sublime  Text, Intellij idea or anything you want to do and then typing command :

```
python script.py # note that the name could be python3.14 too depending on the name with which the prorgamme was installed in your computer.
```

or you can just enter the python interpreter also called REPL(Read-Evaluate-Print-Loop) which basically means a simple computer prorgammme which is interactive, i.e.  takes a single input and spits the output after processing.

The third option is running python code like a command, processes the command and input and returns the results and exits the programme.

```
python -c "Your python code goes here" [arg] ... # the ellipsis means more flags can be used.
```

Understand that the command should be inside quotes as your code could contain characters which are meaningful to the shell and thus shell can hijack your programme to interpret their own meaning.

```
python -c "import sys; print(f'Hello, {sys.argv[1]}!')" surya # surya is the argument stored in sys.argv variable (which is a list)
```

## Modules used  as commands.
To use modules from terminal rather than importing them into a file, we can use the following command: 
```
python -m <module_name> [arg]
```
where `-m` flag represent module name.
what the above command does is find the module path under the directories listed in variable `sys.path` and then executes the executable of module, as several python package manager install the executable of the package, though using it through the`-m` flag is safer.
see...
- **If `module_name.py` is a single file:** Python executes `module_name.py` directly.
- **If `module_name.py` is a directory/folder:** Python executes a file named `module_name/__main__.py` inside that directory and executes it.
btw, wanna see how `sys.path` looks like ? 
```
>>> import sys
>>> sys.path
['', '/usr/lib/python314.zip', '/usr/lib/python3.14', '/usr/lib/python3.14/lib-dynload', '/usr/lib/python3.14/site-packages']
>>>
```
have your way...it's just a list as you can see.
explanation to why using `-m` flag is safer, 
The reason is `Exact Environment Targeting` :
If we have multiple Python versions installed (e.g., Python 3.10 and 3.12, or a virtual environment), running `pip install` might use the wrong Python version. Running **`python3.12 -m pip install`** guarantees that `pip` installs the package specifically into **Python 3.12**.

wanna see Magic?
```
# we can Start a local HTTP web server serving in current directory.
python -m http.server 8000

# we can Format a JSON file/string.
python -m json.tool data.json

# we can create a brand new virtual environment.
python -m venv myenv

# we can inspect performance/benchmarks of a statement.
python -m timeit "'-'.join(str(n) for n in range(100))"
```
ohkay, it ain't magic. don't blame my little soul for over exciting.

>Note: For most Python tools, `/usr/local/bin/yada-yada` is **not** the actual core binary of `yada-yada`—it is just a tiny generated wrapper script. yk now...this cursed knowledge will live on with you.

## Argument passing.
Whatever the argument is passed to the script get's converted to a list and assigned to a  variable called `sys.argv` .

IF there are no arguments given the length of the string is 1, a nd `sys.argv[0] = ''` that's an empty string

| How You Launch Python | Command Example | Value of sys.argv[0] | Explanation |
|---|---|---|---|
| Interactive (REPL) | python | '' (empty string) | Launched with no arguments; opens the interactive shell. |
| Standard Script | python app.py | 'app.py' | The path/filename of the script. |
| Standard Input (-) | <code>cat script.py | python -</code> | '-' | Directs Python to read code from standard input (stdin). |
| Command String (-c) | python -c "import sys; print(sys.argv[0])" | '-c' | Tells you the code was executed directly from an inline string command. |
| Module Execution (-m) | python -m http.server | '/usr/lib/python3.14/http/server.py' | The resolved absolute file path of the located module on your system. |

# the REPL.
this is also called interactive Read Eval Print Loop.
that's it's an interactive python ibterpreter.
it k8nd if behaced likes an terminal/shell in it's own.
in interact8ve mode the commands are read from a tty shell.
btw we can even change the default ">>>" and "..." to our likes.
```Pytyon
sys.ps1 = "yada yada"
sys.ps2 = "bla bla"
```
its just a default stribg we can chabge its name to maybe "surya the lord" or whatever we want.

# encoding.

By default, Python source files are treated as encoded in UTF-8. 
`wtf is utf-8?`
```text
To ubderstand what is utf-8 we need to understand what is source encoding is?

Source encoding is the process of translating human-readable characters into digital binary code (1s and 0s) so a computer can store, process, and display the text correctly
so to do this process we have ASCII and what dies ASCII does is that you can assume its a kind of dictionary (not python rictionary but actyal labguafe dictionary) which h9lds the cgaracter name and corrrespind8ng numver of it.
and this number gets converted to binary sequ3nces 8n computers.
the limitation 2as that ascii only had 128 charact3rs that too onky supported 3ngl8sh...
so it was kind of weird for the rest of the world.. 
so we have utf-8 source encoding which supports almost every character in the world provided that your fonts are capable?
yk some fonts just can"t represent some emojis, or maybe some japanese characters, chinese?
```

In utf-8 encoding, characters of most languages in the world can be used simultaneously in string literals, identifiers and comments — although the standard library only uses ASCII characters for identifiers, a convention that any portable code should follow. To display all these characters properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the characters in the file.

btw ascii takes 7 bits for each type of character in source code. nothing more nothing less.

but the genius if utf8 is if u aren't using some japanese/korean/mandarin(chinese) in ur code it would tge exact same space as if th3 source code was encoded in ascii.

otherwise it can 5ake more space to repr3sent that character in memory.
it can take 1 to 4 vytes (ascii takes 7 bits)

## The Interactive Mode

The REPL (Read-Eval-Print Loop) is: an interactive shell running in a TTY.
And if we want we can change the default >>> and ... prompts. They are just variables stored in the sys module. If we want to we can change those variables, by typing this:

```python
import sys
sys.ps1 = "surya the lord> "
sys.ps2 = "                ... "
```

Now every time Python waits for my input, it will bow to surya the lord>.

 # Source Encoding & UTF-8

 * Python 3 Default: Yes, since Python 3.0, all source code is assumed to be UTF-8 by default.
 * Font vs. Encoding: its a crucial distinction here that many beginners miss. The encoding tells the computer what character it is (the bytes); the font tells the screen how to draw it (the glyph). If the font lacks the glyph, you get the dreaded "tofu" (those empty little rectangles ▯).
 
 * Portable Code (PEP 8): Even though Python allows you to name a variable उम्र = 25 or résumé = True, the official style guide (PEP 8) strongly dictates using only standard ASCII for variables, functions, and classes so anyone anywhere can read and type your code.
 
Technical clarification on ASCII vs Bytes:

You correctly noted that ASCII takes exactly 7 bits. However, computers don't store memory in 7-bit chunks; they store memory in 8-bit bytes.

So, an ASCII character still takes up 1 full byte (8 bits) of disk space. It just leaves the very first bit empty (it's always a 0).
This is exactly where the "genius of UTF-8" that you mentioned comes into play:
 * UTF-8 looks at that first bit. If it's a 0, UTF-8 says: "Ah, this is just plain old ASCII. I'll only read this 1 byte."
 * If you use a Japanese Kanji or an emoji, UTF-8 flips that first bit to a 1, which tells the computer: "Hey! Stop! This is a big character, you need to read the next 2, 3, or 4 bytes to figure out what it is!"
Because of this, an English Python script encoded in UTF-8 is byte-for-byte identical to the exact same script encoded in ASCII. No extra memory is wasted.
To declare an encoding other than the default one, a special comment line should be added as the first line of the file. The syntax is as follows:

# -*- coding: encoding -*-
where encoding is one of the valid codecs supported by Python.

For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:
```python
# -*- coding: cp1252 -*-
```
One exception to the first line rule is when the source code starts with a UNIX “shebang” line. 
In this case, the encoding declaration should be added as the second line of the file. For example:
```python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```
;) done.

