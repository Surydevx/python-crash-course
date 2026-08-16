# Python Tutorial 7: I/O formatting and Files

If your program can't talk to the outside world, it's basically just heating up your CPU for no reason. This chapter covers how to format text, how to read/write files, and how to save complex data structures.

---

## 1. Fancier Output Formatting (String Magic)

We already know `print()` just dumps space-separated values to the terminal (`sys.stdout`). But when you need actual alignment, padding, or dynamic variable injection, you need string formatting.

### 1.1 `str()` vs `repr()`: A Quick Refresher

Remember our talk about the "friendly View" vs the "Developer View"?

* `str(x)`: Returns a clean, readable string.
* `repr(x)`: Returns the hardcore, developer-safe string. It explicitly shows quotes and escapes special characters like `\n` so you know *exactly* what's in memory. If you print a `repr()`, it looks like a literal Python code string.

### 1.2 Formatted String Literals (f-strings)

This is the modern, undisputed king of Python string formatting. Just slap an `f` or `F` before the quotes and inject your variables directly using `{}`.

```python
year = 2026
event = 'Apocalypse'
print(f'Results of the {year} {event}')
# Output: Results of the 2026 Apocalypse

```

**F-String Superpowers:**

* **Math on the fly:** `f"Half of 10 is {10/2}"`
* **Rounding:** Add `:.3f` to round floats to 3 decimal places.
* **The Debugging `=` Trick:** Add an `=` after the variable to print both the name and the value instantly. (This saves *so* much typing).

```text
surya: bugs = 'roaches'
surya: count = 13
surya: print(f'Debugging {bugs=} {count=}')
Debugging bugs='roaches' count=13

```

*(i changed the prompt of python interpreter, cool isn't it?)*

### 1.3 The Older Ways: `.format()` and `%`

Before f-strings, we had `str.format()`. You'll still see it in older codebases. It uses empty `{}` as placeholders and passes the variables at the end.

```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

```

You can also use it to unpack dictionaries directly into a string:

```python
table = {'Sjoerd': 4127, 'Jack': 4098}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}'.format(**table))

```

> **A little Note on `%` Formatting:** You might see strings like `"Hello %s" % name`. This is called printf-style formatting. It's a World War 2 relic borrowed from C. You can totally ignore it for new code, but know it exists so you don't get confused reading legacy scripts.

---

## 2. Reading and Writing Files

To interact with files on your hard drive, we use the built-in `open()` function.

### 2.1 The `with` Keyword (Do Not Skip This)

Opening a file locks it in your operating system. If your program crashes before you explicitly call `f.close()`, that file stays locked, leaking memory and potentially corrupting data.

**Always** use the `with` context manager. It acts as a safety net that automatically closes the file the exact millisecond the block ends, even if your code crashes inside the block.

```python
# THE SAFE WAY:
with open('workfile.txt', 'w', encoding="utf-8") as f:
    f.write("Hello World!")
    
# We check if it closed automatically:
print(f.closed) # True

```

### 2.2 File Modes

When you open a file, you have to tell Python *why* you are opening it.

| Mode | Name | What it does |
| --- | --- | --- |
| `'r'` | Read | (Default) Opens for reading. Crashes if file doesn't exist. |
| `'w'` | Write | Opens for writing. **Erases the existing file completely** before writing. |
| `'a'` | Append | Opens for writing, but adds new data to the *end* of the file. |
| `'r+'` | Read/Write | Opens for both reading and writing. |
| `'b'` | Binary | Appended to modes (like `'rb'` or `'wb'`) for non-text files (JPEGs, EXEs). |

> **Warning: The Line-Ending Trap:**
> By default, Python opens files in **Text Mode**. In text mode, Python secretly translates Windows line endings (`\r\n`) into Unix line endings (`\n`) behind your back. For text, this is incredibly helpful. But if you open a JPEG or an EXE in text mode, Python will try to "fix" the raw binary bytes, **corrupting your file permanently**. Always use `'rb'` or `'wb'` for non-text files!

### 2.3 Reading File Contents

Assuming you have `f = open(...)`:

* **`f.read()`**: Reads the entire file into a massive string. (Dangerous if the file is larger than your RAM).
* **`f.readline()`**: Reads a single line.
* **Looping (The Pro Way):** The most memory-efficient way to read a file is to treat the file object as an iterable. It loads one line into RAM at a time.

```python
with open('huge_log.txt', encoding="utf-8") as f:
    for line in f:
        print(line, end='') # end='' prevents double-spacing since the line already has a \n

```

### 2.4 Moving the Cursor (`seek` and `tell`)

Think of a file like a cassette tape.

* **`f.tell()`**: Returns a number telling you exactly where the "playhead" cursor is currently resting (in bytes from the start of the file).
* **`f.seek(offset, reference)`**: Fast-forwards or rewinds the cursor so you can read/write at a specific byte.

*(Tired? Jal lijiye! 🥛 Let's finish up with data saving.)*

---

## 3. Saving Structured Data (JSON vs. Pickle)

Writing simple strings to a file is easy. But what if you have a massive dictionary full of nested lists and you want to save it to your hard drive? If you write it as a string, you'll have to manually parse it back into a dictionary later.

Python gives you two built-in modules for this: **JSON** and **Pickle**.

### 3.1 JSON (The Universal Standard)

JSON (JavaScript Object Notation) converts Python lists and dictionaries into a standardized string format. It is the de-facto language of the internet. If you save data as JSON, a program written in Rust, Java, or C++ can easily read it.

* **`json.dumps(x)`**: Serializes an object `x` into a JSON formatted string in memory.
* **`json.dump(x, f)`**: Serializes `x` and writes it directly into an open file `f`.
* **`json.load(f)`**: Deserializes (reads) a JSON file back into a usable Python dictionary/list.

```python
import json

my_data = [1, 'simple', 'list']

with open('data.json', 'w', encoding="utf-8") as f:
    json.dump(my_data, f)

```

### 3.2 Pickle (The Python Black Magic)

JSON is safe, but it can only handle basic data types (strings, numbers, lists, dicts). It cannot save custom Python Classes or complex objects.

`pickle` is a Python-specific protocol that can serialize almost *any* arbitrary Python object (even custom classes) into a raw byte stream.

> **CRITICAL SECURITY WARNING:** `pickle` is insecure by design. When you `json.load()` a file, Python just reads the data. When you `pickle.load()` a file, Python actively executes the instructions embedded in the byte stream to reconstruct the object.
> **Never, ever unpickle data you received from an untrusted source.** A malicious user can craft a pickle file that instantly executes a reverse shell or deletes your hard drive the moment you load it. Use JSON for sharing; use Pickle only for temporary local caching of your own trusted data.