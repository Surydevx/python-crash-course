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

IF there are no arguments given the length of the string is 1, a nd `sys.argv[0] = ''` that's an empty string.
```
|**How You Launch Python**|**Command Example**|**Value of sys.argv[0]**|**Explanation**|
|---|---|---|---|
|**Standard Script**|`python app.py`|`'app.py'`|The path/filename of the script.|
|**Standard Input (`-`)**|`cat script.py \| python -`|`'-'`|Directs Python to read code from standard input (stdin).|
|**Command String (`-c`)**|`python -c "import sys; print(sys.argv[0])"`|`'-c'`|Tells you the code was executed directly from a inline string command.|
|**Module Execution (`-m`)**|`python -m http.server`|`'/usr/lib/python3.14/http/server.py'` _(or full path to module)_|The resolved file path of the located module on your system.|
```
