# Tutorial 8

In this tutorial, we are diving into **Files, Exceptions, and Storing Data**. We will cover how to read/write to the hard drive, how to handle errors gracefully, and how data translates between RAM and storage.

## 1. Reading from a File

To interact with files, Python uses the `pathlib` module.

```python
from pathlib import Path

# 1. Create a Path object pointing to the file
path = Path('pi_digits.txt')

# 2. Read the entire file into a single string
contents = path.read_text()
print(contents)

```

### Absolute vs. Relative Paths (The Cafe Analogy)

When you tell Python where a file is, you use a **path**.

* **Absolute Path:** This is like the Google Maps GPS coordinates of a cafe. It is the exact, absolute location in the system from the root folder (e.g., `/home/eric/data_files/filename.txt`). It works no matter where your program is currently running.
* **Relative Path:** This is like giving someone directions based on where they are standing right now: *"Go straight, take a left, then another left."* By default, `Path('pi_digits.txt')` is a relative path. Python looks in the *exact same folder* where the Python script is running.
* Up one level: `Path('../pi_digits.txt')`
* Down into a folder: `Path('data_folders/pi_digits.txt')`

---

## 2. Accessing a File's Lines (and Memory Mechanics)

Often, you don't want one giant string; you want to look at a file line-by-line.

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

# Slices the giant string into a list of smaller strings
lines = contents.splitlines() 

pi_string = ''
for line in lines:
    pi_string += line # Concatenating the strings

print(pi_string)
print(len(pi_string))

```

> **Deep Dive: The Mechanics of `splitlines()**`
> When you run `read_text()`, Python asks the OS to load the entire file from the hard drive into RAM as one massive, contiguous string. If the file has 100,000 lines, there are 100,000 hidden newline characters (`\n`) buried inside it.
> `splitlines()` reads this massive string from left to right. The exact millisecond it hits a `\n`, it deletes the `\n`, slices the string into two, creates a brand new string object in RAM, and drops the memory address of that new string into a List.
> *Note: This method can be memory-inefficient for massive files because it essentially requires double the RAM to hold the original giant string AND the new list of smaller strings.*
> *(Also, string concatenation using `+=` in a loop is clunky. Since strings are immutable, Python has to recalculate and allocate new memory every single time it adds a piece!)*

If your system's default encoding doesn't match the file, you can pass an argument to fix it:
`contents = path.read_text(encoding='utf-8')`

---

## 3. Writing to a File

Writing to a file is just as easy as reading from one.

```python
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.")

```

**⚠️ WARNING: The Danger of Write Mode**
The `write_text()` method operates in "Write" mode (`'w'`). In Linux/C system calls, this literally means "truncate the file to zero bytes, then write the new data."

* If the file doesn't exist, Python creates it.
* If the file *does* exist and has 10,000 lines of highly valuable data... `write_text()` will completely obliterate it instantly without asking permission, replacing it with "I love programming."

*Note: Python can only write strings to a text file. If you have numerical data, you must typecast it first using `str()`.*

---

## 4. Exceptions and Error Handling

Why do we handle errors? If a program crashes, Python spits out a **traceback**. If malicious hackers see a traceback, it gives them inside information about your program's structure. Instead of crashing, we want the program to fail gracefully with a pre-decided, friendly error message.

Python manages errors using **Exception Objects** and `try-except-else` blocks.

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
        
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    # Put the risky code in the 'try' block
    try:
        answer = int(first_number) / int(second_number)
        
    # Catch specific errors and handle them gracefully
    except ValueError:
        print("Please input only numerical values.")
    except ZeroDivisionError:
        print("You can't divide by zero! It is undefined (not infinity).")
        
    # If the try block succeeds without errors, run this block
    else:
        print(answer)

```

### Catching Unknown Errors (Testing Phase Only)

During development, you might not know what errors to expect. You can use a catch-all block to see the exception object without crashing. *(Do not use this in production, as it hides actual bugs!)*

```python
try:
    risky_operation()
except Exception as e:
    print(f"I caught an unknown error: {type(e).__name__}")

```

*Pro Tip: When reading a traceback, always look at the very last line first—that is where the actual error is usually stated.*

### Failing Silently

If you don't want to show the user *any* message when an error occurs, you can use the `pass` keyword to ignore it.

```python
try:
    contents = path.read_text()
except FileNotFoundError:
    pass # Do nothing and move on

```

---

## 5. Storing Data (JSON)

To save structured data (like Lists or Dictionaries) to your hard drive, you should use the JSON (JavaScript Object Notation) format.

```python
from pathlib import Path
import json

# WRITING DATA
numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')

# Convert the Python list into a raw JSON string
contents = json.dumps(numbers) 
path.write_text(contents)

# READING DATA
contents = path.read_text()

# Convert the raw JSON string back into a Python list
numbers = json.loads(contents) 
print(numbers)

```

> **Deep Dive: RAM Pointers vs. Storage Drives**
> A Python List is actually an array of pointers in RAM that point to different pieces of data. Storage drives (HDDs/SSDs) do not understand RAM pointers; they only understand raw data.
>
> * **`json.dumps()` (Dump String):** Takes the complex RAM structure, strips away all the Python-specific memory pointers, and flattens it into a raw, standardized string of text characters.
> * **`json.loads()` (Load String):** The exact reverse. It reads the raw text string from the hard drive, parses the brackets and commas, and physically re-allocates new C-memory structures in RAM to rebuild the list pointers.
>
>

### A Note on Race Conditions

In modern production code, checking if a file exists using `path.exists()` right before reading it can cause a **Race Condition**. What if, in the exact millisecond between your program checking `path.exists()` (which returns True) and `read_text()`, another program deletes the file? Your program will crash. This is why `try-except` blocks are often safer than `if` statements for file operations!
