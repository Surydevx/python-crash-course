# Using Python as a Calculator
 we can do all sort of mathematical operations in print function itself, and we can assign output of complex expressions to a variable
 as '=' operator have very low precedence `x=5/2` is interpreted by python such that first right hand expression is evaluated and then the ouptut of that expression is assigned to a variable, technically in between python calls the constructor method of certain class type according to our data outputs from right hand side expression.
 
 

## Arithmetic Operators

---

## 1. The Basic Operators

### Addition (`+`)
The addition operator adds two operands together. In many programming languages, if the operands are strings instead of numbers, this operator performs *concatenation* (joining them together).

* **Mathematical Formula:** `A + B`
* **Example:**

```python
  result = 5 + 3  # result is 8
```

### Subtraction (`-`)

The subtraction operator subtracts the right operand from the left operand. It can also be used as a unary operator to indicate a negative number (e.g., `-5`).

* **Mathematical Formula:** `A - B`
* **Example:**
```python
result = 10 - 4  # result is 6
```


### Multiplication (`*`)

The multiplication operator multiplies two operands. In programming, the asterisk (`*`) is universally used instead of the traditional `x` to avoid confusion with variables.

* **Mathematical Formula:** `A * B`
* **Example:**
```python
result = 7 * 6  # result is 42
```

### Division (`/`)

The division operator divides the left operand (dividend) by the right operand (divisor).
*Note: In some strictly typed languages (like C or Java), dividing two integers might automatically drop the decimal. However, in modern languages like Python or JavaScript, standard division always results in a floating-point number (a decimal).*

* **Mathematical Formula:** `A / B`
* **Example:**
```python
result = 20 / 4  # result is 5.0
result = 5 / 2   # result is 2.5
```
---

## 2. Specialized Arithmetic Operators

### Modulo / Remainder (`%`)

The modulo operator divides the left operand by the right operand, but instead of returning the quotient, it **returns the remainder**. This is exceptionally useful in programming for determining if a number is even or odd, keeping numbers within a certain bounds (like a clock face), or parsing data.

* **Mathematical Concept:** Remainder of `A / B`
* **Example:**

```python
result = 10 % 3  # result is 1 (because 10 divided by 3 is 9, with 1 left over)
is_even = 14 % 2 # result is 0 (no remainder means it's an even number)
```



### Exponentiation (`**`)

The exponentiation operator raises the left operand (base) to the power of the right operand (exponent).

* **Mathematical Concept:** `A**B` (A to the power of B)
* **Example:**
```python
result = 2 ** 3  # result is 8 (2 * 2 * 2)
```

### Floor Division / Integer Division (`//`)

Floor division divides the two operands and then automatically rounds the result *down* to the nearest whole integer. It effectively chops off the decimal portion.

* **Mathematical Concept:** `⌊A / B⌋`
* **Example:**
```python
result = 10 // 3  # result is 3 (10 / 3 is 3.333..., rounded down to 3)
result = 15 // 4  # result is 3 (15 / 4 is 3.75, rounded down to 3)
```
---

## 3. Order of Operations (Precedence)

When we combine multiple arithmetic operators in a single equation, computers follow a strict order of operations, just like in standard mathematics. The universally accepted acronym is **PEMDAS** (or **BODMAS**):

1. **P**arentheses `()` - Operations inside parentheses are evaluated first.
2. **E**xponents `` - Powers and roots are evaluated next.
3. **M**ultiplication `*` & **D**ivision `/`, `//`, `%` - Evaluated from left to right.
4. **A**ddition `+` & **S**ubtraction `-` - Evaluated from left to right.


## Deep Dive: How Python Processes Escape Sequences

To fully grasp how escape sequences function, it is necessary to differentiate between how Python **stores** data in RAM versus how it **renders** data to the terminal.

Python utilizes two distinct representations for strings: the **Developer Friendly View** (`__repr__`) and the **User Friendly View** (`__str__`). The following steps outline exactly what happens under the hood when a string containing an escape sequence is assigned and subsequently outputted.

### 1. Assignment and Storage in RAM

When the Python interpreter reads source code left to right and encounters a backslash (`\`), it triggers an escape routine. It stops reading the characters literally and combines the backslash with the subsequent character to form a single, special byte.

```python
my_string = "Hello\nWorld"

```

In RAM, Python does not store a literal `\` followed by an `n`. Instead, it stores a single, invisible character: the **ASCII Line Feed** character (Byte value `10`).

Consequently, `len(my_string)` evaluates to `11`, not `12`. The escape sequence is processed and converted into a single byte in memory at the exact moment of assignment.

### 2. Inspecting the Variable: The Developer View (`__repr__`)

When evaluating a variable directly within an interactive shell (such as a Zsh terminal running the Python REPL) without using the `print()` function, Python invokes its internal `__repr__()` (representation) method.

```python
>>> my_string = "Hello\nWorld"
>>> my_string
'Hello\nWorld'

```

**Why doesn't the line break?** The Developer View is designed to show exactly what resides in memory in an unambiguous, safe format. If the REPL actually executed the line break, it would disrupt the terminal formatting and obscure the presence of the special character. Therefore, the interpreter artificially reconstructs the `\n` visually so developers know exactly what bytes comprise that string.

### 3. The `print()` Function: The Human View (`__str__`)

Passing the variable to the `print()` function invokes the string's `__str__()` method, shifting to the Human View.

```python
>>> print(my_string)
Hello
World

```

The execution flow proceeds as follows:

1. `print()` accesses the raw bytes from memory and begins streaming them directly to the terminal's standard output (`stdout`).
2. It streams `H`, `e`, `l`, `l`, `o`.
3. It then streams the special ASCII Byte `10`.
4. **The `print()` function itself does not break the line.** The terminal emulator does. When the terminal receives Byte `10`, it physically moves the cursor down to the next line and resets it to the left edge.
5. Finally, it resumes streaming `W`, `o`, `r`, `l`, `d`.

### 4. Bypassing Escape Sequences: Raw Strings

When writing regular expressions, LaTeX formulas, or system file paths, Python's eagerness to process `\` into special bytes will corrupt the intended text.

To bypass the escape sequence parsing engine entirely, prefix the string with an `r` to denote a **Raw String**.

```python
# Standard String: Python parses \n into a line-break byte
normal_string = "C:\new_folder"
print(normal_string)
# Output: 
# C:
# ew_folder

# Raw String: Python treats \ and n as two separate, literal characters
raw_string = r"C:\new_folder"
print(raw_string)
# Output: C:\new_folder

```

By adding the `r` prefix, you instruct the interpreter's parser during the assignment phase to ignore escape sequences and store all backslashes literally.

The print() function writes the value of the argument(s) it is given

# Python Data Structures: Lists, Assignment, and Copying

This part outlines the fundamental properties of Python lists, explains the mechanics of variable assignment, and details the critical differences between shallow and deep copying operations using Python's built-in `copy` module.

---

## 1. Introduction to Lists

In Python, a **list** is a highly versatile, ordered, and mutable data type. Because lists are ordered, they support **indexing** (accessing elements via their position) and **concatenation** (combining lists). Furthermore, the built-in `len()` function can be applied directly to lists to determine the number of elements they contain.

---

## 2. Assignment and Object Binding

A critical concept in Python is understanding how simple variable assignment works. Assignment statements in Python **never copy data**; instead, they create *bindings* (or references) between a target variable and an existing object in memory.

When you assign an existing list to a new variable, the new variable merely refers to the exact same list in memory. Therefore, any in-place changes you make to the list through one variable will be reflected across all other variables that point to it.

### Example: Shared References

```python
rgb = ["Red", "Green", "Blue"]
rgba = rgb

# Check if both variables reference the exact same object in memory
print(id(rgb) == id(rgba))  
# Output: True

# Modifying the 'rgba' variable...
rgba.append("Alph")

# ...also affects the 'rgb' variable
print(rgb)
# Output: ["Red", "Green", "Blue", "Alph"]

```

---

## 3. Creating Copies

For collections that are mutable or contain mutable items, creating a true independent copy is often necessary so that modifications to one do not unintentionally mutate the other.

### 3.1 Copying via Slicing

All slice operations in Python return a *new* list containing the requested elements. Therefore, slicing a list from beginning to end acts as a **shallow copy**.

```python
# Create a shallow copy using full slicing [:]
correct_rgba = rgba[:]

# Modifying the copy does not affect the original list
correct_rgba[-1] = "Alpha"

print(correct_rgba) 
# Output: ["Red", "Green", "Blue", "Alpha"]

print(rgba)         
# Output: ["Red", "Green", "Blue", "Alph"]

```

### 3.2 Copying via Built-in Methods

Before bringing in outside tools, it is worth noting that Python's standard collections (like lists, dictionaries, and sets) have built-in ways to copy themselves.

If you have a standard list, you can create a shallow copy simply by calling `.copy()`:

```python
original_list = [1, 2, 3]
new_list = original_list.copy()

new_list.append(4)

print(original_list) # Output: [1, 2, 3]
print(new_list)      # Output: [1, 2, 3, 4]

```

**A quick warning about "Subclasses":** Sometimes programmers create custom, advanced versions of lists (a "subclass"). If you use `.copy()` or slicing (`[:]`) on this advanced list, Python might accidentally return a regular, basic list instead of your advanced version. If you want to be 100% sure you are getting the exact same type of object back, it is better to use the `copy` module explained below.

---

## 4. The `copy` Module: Heavy-Duty Copying

When basic assignment (`=`) or `.copy()` isn't enough, Python provides a built-in library specifically for duplicating things, called the `copy` module. You use it by putting `import copy` at the top of your file.

### 4.1 What's inside the `copy` module?

Here are the main tools this module gives you:

* **`copy.copy(obj)`**: Creates a **shallow copy** of your object.
* **`copy.deepcopy(obj)`**: Creates a **deep copy** of your object.
* **`copy.replace(obj, changes)`**: *(New in Python 3.13)* Imagine this as a "find and replace" for an object. It duplicates the object but swaps out specific fields you ask it to change.

*Note: The `copy` module is smart. If you ask it to copy things that shouldn't or can't be copied—like a live network socket, a running process, or a chunk of core computer memory—it will just return the original item untouched to prevent your program from crashing.*

### 4.2 The Big Concept: Shallow vs. Deep Copy

This distinction only matters for **compound objects**. A compound object is just a container that holds *other* containers—like a list of lists, or a dictionary full of lists.

Imagine a large cardboard box (the outer list) containing several smaller shoeboxes (the inner lists).

#### The Shallow Copy (`copy.copy`)

A shallow copy builds a brand new outer cardboard box. However, instead of making new shoeboxes, it just puts **shortcuts (references)** to the *original* shoeboxes inside the new cardboard box.

Because they share the inner shoeboxes, changing the contents of a shoebox in the copy will magically change the contents of the shoebox in the original!

```python
import copy

# A list containing other lists (a compound object)
original = [[1, 2], [3, 4]]

# Make a shallow copy
shallow_copy = copy.copy(original)

# Let's change an inner list inside the copy
shallow_copy[0][0] = "CHANGED"

# Oh no! The original was changed too!
print(original)      # Output: [['CHANGED', 2], [3, 4]]
print(shallow_copy)  # Output: [['CHANGED', 2], [3, 4]]

```

#### The Deep Copy (`copy.deepcopy`)

A deep copy is a true, 100% independent clone. It builds a new outer cardboard box, and then **recursively** builds brand new, identical shoeboxes to put inside it. Changes to the deep copy will never affect the original.

```python
import copy

original = [[1, 2], [3, 4]]

# Make a deep copy
deep_copy = copy.deepcopy(original)

# Change an inner list inside the copy
deep_copy[0][0] = "CHANGED"

# The original is safe!
print(original)   # Output: [[1, 2], [3, 4]]
print(deep_copy)  # Output: [['CHANGED', 2], [3, 4]]

```

### 4.3 Deep Copy Challenges and Solutions

Because a deep copy tries to copy *everything* inside an object, it can run into two headaches:

1. **Infinite Recursive Loops:** Imagine a list that accidentally contains itself as an item (e.g., `my_list.append(my_list)`). If `deepcopy` tries to copy this, it will look inside the list, see the list, try to copy it, look inside, see the list... and get stuck in an infinite loop until your computer crashes.
2. **Over-copying:** Sometimes you *want* objects to share data. For example, you might want to copy a `Car` object, but you want both cars to point to the exact same `ManufacturingPlant` object in memory. Deep copy might accidentally duplicate the whole factory!

**How Python fixes this:**
`deepcopy()` uses a clever trick called a **`memo` dictionary**. Think of it as a guestbook. As `deepcopy` travels through your data duplicating things, it writes down the ID of every item it copies. If it runs into a list it has already copied (preventing the infinite loop), it stops and just uses the copy it already made.

---

## 5. Customizing Copy Behavior for Your Own Classes

When you write your own Custom Classes in Python, you might want to teach Python exactly *how* it should copy your objects.

For example, if you have a `DatabaseConnection` class, you probably don't want `copy.copy()` to duplicate the actual live connection to the server!

To control this, Python lets you define "magic methods" (sometimes called dunder methods, for double-underscore) inside your class. If Python sees these methods, it will follow your instructions instead of its default behavior.

### `__copy__(self)`

If someone calls `copy.copy(your_object)`, Python looks for this method. You write the code inside this method to define exactly what a shallow copy means for your specific object, and return the new object.

### `__deepcopy__(self, memo)`

If someone calls `copy.deepcopy(your_object)`, Python looks for this method.

* It passes you the `memo` guestbook dictionary. You should pass this along whenever you copy inner components, but you shouldn't mess with it directly (treat it as a "black box" or "opaque object").
* Inside this method, you tell Python exactly which pieces of your object should be deeply copied (using `copy.deepcopy(component, memo)`) and which pieces should be left alone.

### `__replace__(self, /, changes)` *(New in 3.13)*

If someone uses `copy.replace()`, Python looks for this method. Your code here should generate a fresh version of your object, but intelligently swap out the attributes provided in the `changes` dictionary. (This is currently most common in special Python structures like `dataclasses` and `namedtuples`).