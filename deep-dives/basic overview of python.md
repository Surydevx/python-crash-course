# basic overview of python.
In this document we would be covering asic overview of python.

## Variable names are case-sensitive.
```python
a = 4
A = "Sally"
#A will not overwrite a
```

Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any 
other identifiers:

```
Keyword	    Description
and	        A logical operator
as	        To create an alias
assert	    For debugging
async	    Define an asynchronous function
await	    Wait for and get a result from an awaitable
break	    To break out of a loop
case	    Pattern in a match statement
class	    To define a class
continue	To continue to the next iteration of a loop
def	        To define a function
del	        To delete an object
elif	    Used in conditional statements, same as else if
else	    Used in conditional statements
except	    Used with exceptions, what to do when an exception occurs
False	    Boolean value, result of comparison operations
finally	    Used with exceptions, a block of code that will be executed no  matter if there is an exception or not
for	        To create a for loop
from	    To import specific parts of a module
global	    To declare a global variable
if	        To make a conditional statement
import	    To import a module
in	        To check if a value is present in a list, tuple, etc.
is	        To test if two variables are equal
lambda	    To create an anonymous function
match	    Start a match statement (compare a value against cases)
None	    Represents a null value
nonlocal	To declare a non-local variable
not	        A logical operator
or	        A logical operator
pass	    A null statement, a statement that will do nothing
raise	    To raise an exception
return	    To exit a function and return a value
True	    Boolean value, result of comparison operations
try	        To make a try...except statement
while	    To create a while loop
with	    Used to simplify exception handling
yield	    To return a list of values from a generator
```
## Unpack a Collection

If you have a collection of values in a list, tuple etc. Python allows you to extract the values in collection object into variables. This is called unpacking.

> Note- that this works only if both number of values in collection is same  as number of variables. but we can use asterisk operator to catch all left values into a seperate variables as a list.

Example
Unpack a list:
```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```
## Global Variables

Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

If we create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value, and that function or class would continue to use the variable in local scope w/o any knowledge of the variale defined in global scope with the same name.

```python
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

```
> note: The mere action of accessing a global variable in local scope doesn't need any special keywords, but if we surely need to use keyword's like "global" if we want to declare and initialize a variable into global scope from under a local scope & we need to follow the same procedure if we are just trying to overwrite a global variable froom under a local scope.

## The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the "global" keyword.

```python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

Also, use the global keyword if you want to change a global variable inside a function.

Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword:
```python
# variable 'x' defined in global scope.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
# data types in python.

Python has the following data types built-in by default, in these categories:

```
Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
```

``Note=You can get the data type of any object by using the type() function``

# Python Data Types:

In Python, every value is an object, and every object has a specific data type. Because Python is dynamically typed, you don't need to explicitly declare a variable's type; the interpreter figures it out automatically when you assign a value.

Here is how the core data types operate under the hood.

---

## 1. Text Type

### `str` (String)

* **How it works:** A string is an immutable (unchangeable) sequence of Unicode characters. Because it is ordered, you can access specific characters using indexing or slicing.
* **Syntax:** Enclosed in single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`"""..."""` for multiline strings).

```python
# String examples
greeting = "Hello, World!"
single_quote_string = 'Python is fun'
multiline_string = """This string
spans multiple
lines."""

print(greeting[0])  # Output: H

```

---

## 2. Numeric Types

### `int` (Integer)

* **How it works:** Represents whole numbers (positive, negative, or zero). In Python, integers have unlimited precision, meaning they can be as long as your machine's memory allows.

```python
x = 10
large_number = 999_999_999  # Underscores can be used for readability

```

### `float` (Floating Point)

* **How it works:** Represents real numbers with a decimal point. They can also be written in scientific notation using `e` or `E` to indicate the power of 10.

```python
pi_value = 3.14159
scientific_float = 2.5e3  # Equals 2500.0

```

### `complex`

* **How it works:** Represents complex numbers, containing a real part and an imaginary part. The imaginary part is denoted by the letter `j` (instead of the `i` used in mathematics).

```python
z = 3 + 4j
print(z.real)  # Output: 3.0
print(z.imag)  # Output: 4.0

```

---

## 3. Sequence Types

Sequence types store multiple values in an organized, indexed format.

### `list`

* **How it works:** Ordered and mutable. You can change, add, or remove items after creation. Lists can hold a mix of different data types.
* **Syntax:** Square brackets `[]`.

```python
my_list = ["apple", 42, 3.14, True]
my_list.append("banana") # Modifies the list

```

### `tuple`

* **How it works:** Ordered and **immutable**. Once created, you cannot change its contents. This makes tuples faster and safer for data that shouldn't be altered.
* **Syntax:** Parentheses `()`. A single-element tuple must have a trailing comma.

```python
my_tuple = (10, 20, 30)
single_element_tuple = (5,) 

```

### `range`

* **How it works:** An immutable sequence of numbers. It is highly memory efficient because it doesn't store all the numbers in memory; it just calculates them on demand. Primarily used in `for` loops.
* **Syntax:** `range(start, stop, step)`

```python
# Generates numbers 0, 1, 2, 3, 4
my_range = range(5) 

for num in my_range:
    print(num)

```

---

## 4. Mapping Type

### `dict` (Dictionary)

* **How it works:** A mutable collection of key-value pairs. Modern Python dictionaries preserve the order in which items are inserted. Keys must be unique and immutable (like strings, numbers, or tuples), while values can be anything.
* **Syntax:** Curly braces `{}` with keys and values separated by a colon `:`.

```python
user_profile = {
    "username": "admin",
    "access_level": 5,
    "is_active": True
}

print(user_profile["username"])  # Output: admin

```

---

## 5. Set Types

Sets are heavily inspired by mathematical sets.

### `set`

* **How it works:** An unordered, mutable collection of **unique** elements. It automatically removes duplicates. Because it is unordered, you cannot use indexing (like `my_set[0]`).
* **Syntax:** Curly braces `{}` (but without key-value pairs).

```python
my_set = {1, 2, 2, 3, 4, 4}
print(my_set)  # Output: {1, 2, 3, 4}

```

### `frozenset`

* **How it works:** The immutable version of a `set`. Once created, you cannot add or remove elements. Because it is immutable, a `frozenset` can be used as a dictionary key (unlike a regular `set`).
* **Syntax:** Created using the `frozenset()` function.

```python
locked_set = frozenset([1, 2, 3])

```

---

## 6. Boolean Type

### `bool`

* **How it works:** Represents truth logic. It can only hold one of two values: `True` or `False`. Under the hood, Python treats `True` as `1` and `False` as `0`.

```python
is_admin = True
is_logged_in = False

# Evaluates to True
print(10 > 5) 

```

---

## 7. Binary Types

These are advanced data types used for handling raw binary data, like reading images, network packets, or interacting with C libraries.

### `bytes`

* **How it works:** An immutable sequence of single bytes (integers in the range 0 <= x < 256).
* **Syntax:** A string prefixed with `b`.

```python
raw_data = b"Hello"

```

### `bytearray`

* **How it works:** The mutable counterpart to `bytes`. You can change individual bytes after creation.
* **Syntax:** Created using the `bytearray()` function.

```python
mutable_data = bytearray(b"Hello")
mutable_data[0] = 74 # Changes 'H' to 'J'

```

### `memoryview`

* **How it works:** Allows Python code to access the internal data of an object that supports the buffer protocol (like `bytes` or `bytearray`) without copying it. Highly efficient for large datasets.
* **Syntax:** Created using the `memoryview()` function.

```python
data = bytearray(b"XYZ")
view = memoryview(data)
print(view[0])  # Output: 88 (ASCII value of 'X')

```

---

## 8. None Type

### `NoneType`

* **How it works:** Represents the intentional absence of a value. It is Python's equivalent of "null." Functions that don't explicitly `return` a value return `None` by default.
* **Syntax:** The keyword `None`.

```python
empty_variable = None

if empty_variable is None:
    print("This variable has no value yet.")

```
# Python Type Casting: The "δ()" Functions

In programming, you often need to change a value from one data type to another. This is called **Type Casting** (or Type Conversion). In Python, this is done using built-in constructor functions.

---

## 1. Integer Casting: `int()`

* **How it works:** It takes a number or a string and attempts to convert it into a whole integer. If you pass it a float, it cuts off the decimal portion. If you pass it a string, it parses the string for digits.
* **Limitations & Traps:**
* **It truncates, it doesn't round:** `int(3.99)` becomes `3`, not `4`.
* **Base-10 strictness:** It will throw a `ValueError` if a string contains anything other than whole numbers (no letters, no decimal points). `int("3.14")` will crash.



```python
print(int(3.99))       # Output: 3
print(int("42"))       # Output: 42

# print(int("hello"))  # ValueError: invalid literal for int()
# print(int("3.14"))   # ValueError: invalid literal for int()

```

## 2. Float Casting: `float()`

* **How it works:** Converts an integer or a string into a floating-point (decimal) number.
* **Limitations & Traps:**
* Like `int()`, passing a non-numerical string will trigger a `ValueError`.
* Floating-point arithmetic in computers has inherent precision limits. Casting very large integers to floats can result in a loss of exact precision.



```python
print(float(5))        # Output: 5.0
print(float("3.14"))   # Output: 3.14
print(float("-89.5"))  # Output: -89.5

```

## 3. String Casting: `str()`

* **How it works:** Converts absolutely any Python object into a string. Under the hood, it asks the object, *"How do you represent yourself as text?"* (by calling the object's `__str__()` dunder method).
* **Limitations & Traps:**
* **One-way street for collections:** While `str([1, 2, 3])` easily becomes `"[1, 2, 3]"`, converting that string *back* into a list is incredibly difficult and requires specific modules (like `ast.literal_eval` or `json`). It doesn't cast back intuitively.



```python
print(str(3.14))       # Output: "3.14"
print(str([1, 2]))     # Output: "[1, 2]"

```

## 4. Collection Casting: `list()`, `tuple()`, and `set()`

* **How it works:** These functions require an **iterable** (something that can be looped over, like a string, dictionary, or another list). They iterate through the data and dump the elements into the new container.
* **Limitations & Traps:**
* **Requires Iterables:** You cannot cast an integer to a list. `list(5)` will throw a `TypeError: 'int' object is not iterable`.
* **Dictionary Data Loss:** If you cast a dictionary to a list or tuple, **it only grabs the keys**. The values are completely left behind unless you explicitly cast `my_dict.values()` or `my_dict.items()`.
* **Set Destruction:** Casting to a `set()` automatically permanently deletes all duplicate values and completely scrambles the order of the elements.



```python
# String to List
print(list("Python")) 
# Output: ['P', 'y', 't', 'h', 'o', 'n']

# Dictionary to List (Notice the values are lost)
my_dict = {"a": 1, "b": 2}
print(list(my_dict)) 
# Output: ['a', 'b']

# List to Set (Destroys duplicates and order)
print(set([1, 2, 2, 3, 1])) 
# Output: {1, 2, 3}

```

## 5. Dictionary Casting: `dict()`

* **How it works:** Converts an iterable into a dictionary.
* **Limitations & Traps:**
* **Strict Structural Requirements:** You cannot just pass a flat list to `dict()`. The iterable *must* consist of pairs (like a list of two-item tuples or a list of two-item lists). If any element has 3 items or 1 item, the interpreter throws a `ValueError`.



```python
# Valid structural casting (List of Tuples)
pairs = [("name", "Alice"), ("age", 25)]
print(dict(pairs)) 
# Output: {'name': 'Alice', 'age': 25}

# invalid_list = ["name", "Alice"]
# dict(invalid_list) # ValueError: dictionary update sequence element #0 has length 4; 2 is required

```

## 6. Boolean Casting: `bool()`

* **How it works:** Evaluates the "truthiness" of an object.
* **Limitations & Traps:**
* It is absolute. You don't get to decide what is True or False.
* In Python, **everything** evaluates to `True` *except* for a very specific list of empty or zero values: `0`, `0.0`, `""` (empty string), `[]`, `{}`, `()`, `None`, and `False`.



```python
print(bool(1))         # Output: True
print(bool("Hello"))   # Output: True
print(bool([1, 2]))    # Output: True

# The Falsey Values
print(bool(0))         # Output: False
print(bool(""))        # Output: False
print(bool([]))        # Output: False
print(bool(None))      # Output: False

```
