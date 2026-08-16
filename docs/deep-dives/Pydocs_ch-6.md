# Python Tutorial 6: Modules & Packages

If you quit the Python REPL, all your hard work, functions, and variables vanish into the digital void. To build actual software, you need to save your code in files.

A **module** is just a text file containing Python code, with a `.py` extension. That's it. It allows you to organize your code and reuse functions without copy-pasting them.

---

## 1. Importing: How Namespaces Actually Work

Let's say you write a file named `fibo.py` containing a function `fib()`.

When you type `import fibo`, Python does **not** dump all of `fibo`'s functions into your current environment. It creates an isolated namespace (a bubble) called `fibo`. To use the function, you have to explicitly point to that bubble:

```python
import fibo
fibo.fib(1000) # Reaching into the bubble

```

If you hate typing `fibo.` every time, you have two options to bypass the bubble:

1. **Direct Import:** `from fibo import fib` (Puts `fib` directly into your main namespace).
2. **Aliasing:** `import fibo as f` (Renames the bubble to `f` to save keystrokes).

### The Evil `import *`

You can type `from fibo import *` to dump *everything* from the module into your current namespace (except variables starting with an underscore `_`).

> **Warning:** In production code, this is highly frowned upon. It causes "namespace pollution"—silently overwriting variables you've already defined. It’s a nightmare to debug. Keep this trick in the interactive REPL where you're just messing around.

---

## 2. The Classic Boilerplate: `if __name__ == "__main__":`

Every module has a built-in, hidden global variable called `__name__`.

* If you **import** a module, its `__name__` is its filename (e.g., `"fibo"`).
* If you **run** the file directly from the terminal (`python fibo.py`), Python forces its `__name__` to be `"__main__"`.

We exploit this mechanic to make a file dual-purpose. You can write code that *only* triggers if the file is executed directly (like a script), but stays completely silent if the file is just being imported by someone else:

```python
# fibo.py
def fib(n):
    # ... magic happens ...

# This block is ignored if the file is imported!
if __name__ == "__main__":
    import sys
    # Runs the function using the terminal argument
    fib(int(sys.argv[1])) 

```

---

## 3. Where Does Python Look? (The `sys.path` Hierarchy)

When you type `import spam`, Python doesn't just magically scan your entire hard drive. It searches in a very strict, chronological order defined by a list called `sys.path`:

1. **The Current Directory:** Wherever your main script is running from.
2. **`PYTHONPATH`:** Environment variables set in your OS.
3. **Standard Library & Site-Packages:** The default installation directories.

**The Hacker Move:** Because `sys.path` is literally just a Python list, you can mutate it on the fly while your program is running to force Python to look in weird directories:

```python
import sys
sys.path.append('/home/surya/custom_libs/python')

```

---

## 4. The `__pycache__` Cursed Folder

If you've ever run a Python project, you've seen that annoying `__pycache__` folder spawn in your directory.

**What is it?**
To speed up *loading* modules, Python compiles your human-readable `.py` code into machine-friendly bytecode and caches it as a `.pyc` file (e.g., `spam.cpython-314.pyc`).

* **The Reality:** A `.pyc` file does **not** make your program execute faster. It only makes the initial *loading/importing* phase faster.
* **Automatic:** Python checks the timestamp of your `.py` file against the `.pyc` file. If you edited the source code, Python automatically throws away the old cache and recompiles it.

*(Tired? Jal lijiye! 🥛 Let's talk about folders.)*

---

## 5. Packages: Directories with a VIP Pass

As your project grows, you'll want to group related modules into folders. A **Package** is just a folder full of `.py` modules.

However, to prevent Python from treating *every* random folder on your computer as a Python package, the folder **must** contain a file named `__init__.py`.

```text
sound/                          # Top-level package
      __init__.py               # The VIP Pass (can be totally empty)
      formats/                  # Subpackage
              __init__.py
              wavread.py
      effects/                  # Subpackage
              __init__.py
              echo.py

```

To import the echo module, you use dot notation:

```python
import sound.effects.echo
# or
from sound.effects import echo

```

### Intra-package References (Dot Notation)

If a module inside the package needs to talk to its sibling, it can use relative imports based on the current package's structure:

* `from . import echo` (Look in the current folder)
* `from .. import formats` (Go up one folder, then into formats)

> **The Golden Rule of Relative Imports:** Relative imports *only* work inside packages. If you are writing your main executable script, you **must** use absolute imports.

---

## 6. Taming `import *` with `__all__`

If an end-user types `from sound.effects import *`, Python does not automatically scan the filesystem and import every `.py` file in the folder. That would be slow and potentially dangerous.

If you, the package author, want to support `import *`, you have to explicitly create an allowed list inside the `__init__.py` file using the `__all__` variable:

```python
# inside sound/effects/__init__.py
__all__ = ["echo", "surround", "reverse"]

```

Now, if someone uses `import *`, they only get exactly what you specified in that list.

---

## 7. Introspection: The `dir()` Function

When you are deep in the terminal and forget what a module actually contains, `dir()` is your flashlight. It returns a sorted list of every single string name (variables, functions, classes) defined inside that module.

```text
surya: import sys
surya: dir(sys)
['__displayhook__', '__doc__', '__name__', 'argv', 'path', 'ps1', 'ps2', 'version', ...]

```

If you call `dir()` without any arguments, it lists everything currently floating around in your active local environment.

> **Under the hood:** `dir()` doesn't show the core built-in functions (like `print()` or `len()`). If you want to see the literal bedrock of Python, you have to run `dir(builtins)`.