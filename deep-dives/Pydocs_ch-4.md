# Python Control Flow & Function Mechanics: Advanced Study Guide

## 1. Advanced Loop Mechanics

While standard `for` and `while` loops are straightforward, Python implements several specific behaviors and constructs designed for optimized iteration and control.

**Basic Rules:**

* A `for` statement loops through items of a sequence in the exact order they appear.
* **Warning:** Modifying a collection while looping over it creates dangerous issues. If you delete an element in a list mid-loop, subsequent elements shift left, causing the loop to skip items entirely.
* **The Fix:** To manipulate a collection safely during iteration, use one of these two official strategies:
1. **Loop over a copy:** `for user, status in users.copy().items():` (allows you to safely delete from the original `users` dict).
2. **Create a new collection:** Build a brand-new, empty collection and append only the items you want to keep.



### 1.1 The `range()` Object and Iterables

The `range()` function does not generate a list of numbers in memory. Instead, it returns an **iterable** object. For example, `range(5)` generates `0, 1, 2, 3, 4` (note that 5 is not in the sequence).

* **Space Efficiency:** It calculates and yields successive items only when iterated over, significantly saving memory compared to a populated list.
* **Iterable Concept:** An iterable is any object in memory that returns successive items until the sequence is exhausted. Functions like `sum()` also take iterables as arguments.

### 1.2 `enumerate()` and Lazy Evaluation

There is a built-in function called `enumerate()` which enables us to loop over a sequence while getting both the index and the value of the item simultaneously.

```python
meow = "catcatcatcatcatcatcat"

# enumerate returns the index and value using lazy evaluation
for index, value in enumerate(meow):
    print(f"{index} : {value}")

```

Proof that `enumerate` uses lazy evaluation (it doesn't build a list in memory, it just creates an iterable object):

```text
surya: print(enumerate(meow))
<enumerate object at 0x7fc1bacf8c70>
surya:

```

*(Changed the interpreter prompt to "surya: " — cool, isn't it?)*

### 1.3 `break`, `continue`, and the `else` Clause on Loops

* `break`: Breaks completely out of the `for` or `while` loop.
* `continue`: Skips the rest of the current iteration and moves to the next one, but it does *not* stop the loop entirely.

A highly unique feature of Python is the ability to attach an `else` clause to `for` and `while` loops.

* **Execution Condition:** The `else` block executes **only if the loop completes its iterations normally** without encountering any interruption. Interruptions include `break` statements, `return` statements, or raised exceptions.
* **Mental Model:** Think of it as a "no break" clause.

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break # If we break, the else clause below is skipped
    else:
        # Executes ONLY if the inner loop finishes without breaking
        print(f"{n} is a prime number")

```

### 1.4 The `pass` Statement

The `pass` statement does absolutely nothing. It is a null operation used when Python's syntax requires an indented block, but your program requires no action. You'll typically use this for minimal empty classes, infinite wait loops (`while True: pass`), or as a placeholder for a function you haven't written yet.

> *Fun Fact:* Many Python developers conventionally use the Ellipsis literal `...` instead of `pass` as a placeholder body (e.g., `def my_unwritten_function(): ...`).

---

## 2. The `match` Statement: The "Shape Sorter"

Before Python 3.10, if you wanted to check a variable against many possibilities, you had to write a long chain of `if/elif/else` statements (note: the number of `elif` or `else` parts is totally optional in an `if` block). The `match` statement replaces this by checking the **shape/pattern** of the data.

### 2.1 Basic Pattern Matching & Piping

You can match literal values and use the piping operator `|` (which translates to `or`) to merge various cases:

```python
def http_error(status):
    match status: 
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not allowed"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

```

The `_` covers all miscellaneous cases, just like an `else` block. If no case matches, no branch is executed.

### 2.2 Pattern Unpacking

Think of `match` like a mold. If your data fits the mold, Python runs that block of code while automatically unpacking the data into new variables.

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}") # Binds the second tuple value to 'y'
    case (x, 0):
        print(f"X={x}") # Binds the first tuple value to 'x'
    case (x, y):
        print(f"X={x}, Y={y}") # Conceptually similar to unpacking: (x, y) = point
    case _:
        raise ValueError("Not a point")

```

### 2.3 Matching Custom Objects (The "Constructor Lookalike")

If you are using classes to structure your data, you can use the class name followed by an argument list resembling a constructor. It acts in reverse: instead of putting data *into* an object, it extracts data *out* of it.

```python
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Extracting data instantly:
match some_data:
    case Point2D(x=a, y=b):
        print(f"2D point at coordinates: {a}, {b}")
    case Point3D(z=depth):
        print(f"3D point with a depth of: {depth}")
    case _:
        print("Unknown data structure")

```

Before this feature, you had to write multiple lines of messy code using `isinstance()` and manual attribute fetching.

### 2.4 The `__match_args__` Special Attribute

When you create an instance of a class, you often pass values by position (`Point(1, 2)`). However, during a match statement, Python needs to know exactly which attribute comes first. By default, custom classes do not have a built-in order for their attributes.

The `__match_args__` attribute acts as a lookup map for the match engine.

```python
class Point:
    __match_args__ = ("x", "y") # Tells Python the exact order for positional matching

    def __init__(self, x, y):
        self.x = x
        self.y = y

```

Because `__match_args__ = ("x", "y")` locks in the order, the match engine interprets positions and keyword arguments identically. The following cases all do the exact same thing (they match `x` to `1` and bind `y` to `var`):

* `case Point(1, var):` Uses pure position.
* `case Point(1, y=var):` Mixed position and keyword.
* `case Point(x=1, y=var):` Pure keyword.
* `case Point(y=var, x=1):` Pure keyword (order doesn't matter for keywords).

**Built-in Automation:** If you use a `@dataclass`, Python automatically generates the `__match_args__` tuple for you based on the order you declare the fields.

---

## 3. Function Mechanics: Under the Hood

In Python, "procedures" do not exist. Even if a function doesn't have a `return` statement—or if execution simply falls off the end of the block—it silently returns the built-in `None` object.

When you pass data into a Python function, you are not passing a copy of the data. Arguments are passed by **Object Reference**—meaning you are passing a direct link to the object in memory.

### 3.1 Symbol Tables & Scope (The LEGB Rule)

When a function executes, it introduces a new "symbol table" (a hidden dictionary used strictly for local variables). When you reference a variable inside a function, Python searches for its value in a strict, unchangeable order known as the LEGB rule:

1. **L**ocal symbol table (inside the current function).
2. **E**nclosing functions' symbol tables (if it's a nested function).
3. **G**lobal symbol table (the module-level variables).
4. **B**uilt-in names (like `print` or `len`).

Because of this order, you can easily *read* global variables inside a function, but you cannot directly *reassign* them unless you explicitly use the `global` statement. Otherwise, assigning a value simply creates a brand-new local variable that masks the global one.

### 3.2 The Mutable Default Trap

If you define a function with a default mutable object like a list (`def f(a, L=[]):`), Python evaluates that default value **exactly once** when the `def` line is first executed. It creates that empty list in memory at that exact moment. Every subsequent time you call the function, it uses that **exact same list**.

```python
# THE TRAP (Dangerous!)
def add_item_bad(item, box=[]):
    box.append(item)
    return box

print(add_item_bad("apple"))   # Output: ['apple']
print(add_item_bad("banana"))  # Output: ['apple', 'banana']  <-- Where did apple come from?!

# THE FIX (Safe!)
def add_item_good(item, box=None):
    if box is None:
        box = []
    box.append(item)
    return box

```

### 3.3 Forcing How Arguments are Passed (`/` and `*`)

Before using advanced controls, remember the absolute golden rule of Python functions: **Positional arguments must always precede keyword arguments in a function call.** (e.g., `f(10, x=5)` is valid, but `f(x=5, 10)` will trigger a syntax error).

To gain even stricter control over your APIs, you can place "barriers" in your argument list:

* **The Slash `/`:** Anything to the left is *strictly positional*. The caller cannot use the parameter's name. (e.g., `f(10)` is allowed, `f(x=10)` will crash).
* **The Asterisk `*`:** Anything to the right is *strictly keyword-only*. The caller must name the argument.

```python
def setup_server(ip_address, /, port, *, secure):
    print(f"IP: {ip_address}, Port: {port}, Secure: {secure}")

# VALID: IP is positional, port is either, secure is keyword-only
setup_server("192.168.1.1", 8080, secure=True)

```

### 3.4 Catch-All Buckets (`*args` and `**kwargs`)

* `*args`: Catches any extra positional arguments and bundles them into a **Tuple**.
* `**kwargs`: Catches any extra named keyword arguments and bundles them into a **Dictionary**.

```python
def order_pizza(size, *toppings, **delivery_details):
    print(f"Toppings: {toppings}")          # Becomes a Tuple
    print(f"Details: {delivery_details}")   # Becomes a Dictionary

order_pizza("Large", "Pepperoni", "Extra Cheese", tip=5, driver="Dave")

```

### 3.5 Exploding Data into Functions (Unpacking)

If you have a list or dictionary, you can "explode" it directly into a function's arguments. This is the exact reverse of the buckets above. Use `*` to unpack lists/tuples and `**` to unpack dictionaries.

```python
# Unpacking a List
numbers = [3, 6]
print(list(range(*numbers)))  # Turns range([3, 6]) into range(3, 6)

# Unpacking a Dictionary
settings = {"sep": "---", "end": "!!!\n"}
print("Hello", "World", **settings) 
# Output: Hello---World!!!

```

---

## 4. Functional Tools

### 4.1 Lambda Expressions

A `lambda` is a small, anonymous "throwaway" function restricted to a single expression. They are syntactic sugar for a normal function definition.

```python
# Real-world use case: Custom sorting
# Sort this list of tuples based on the SECOND number, not the first
points = [(1, 5), (3, 2), (2, 8)]
points.sort(key=lambda pair: pair[1])

print(points) # Output: [(3, 2), (1, 5), (2, 8)]

```

### 4.2 Function Annotations

You can attach expected types to your functions (e.g., `def f(name: str) -> str:`). Python’s engine **completely ignores these** when the code runs. They are essentially just metadata stored in a hidden dictionary (`__annotations__`) to help us and code editors (linters) catch mistakes.

```python
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

# Python runs this fine, even though it breaks the "rules" of the annotations!
print(greet(99, "Frank")) 

```

---

## 5. Coding Style (PEP 8 Highlights)

Writing idiomatic Python means adhering to PEP 8, the standard style guide:

1. **Indentation:** Exactly 4 spaces per indentation level. Never use tabs.
2. **Line Length:** Limit lines to 79 characters.
3. **Whitespace:** Use spaces around operators (`a = f(1, 2) + g(3, 4)`), but avoid spaces directly inside brackets (`[1, 2]`, not `[ 1, 2 ]`).
4. **Naming Conventions:**
* Classes: `UpperCamelCase`
* Functions & Methods: `lowercase_with_underscores`


5. **Documentation:** Utilize docstrings immediately following the `def` statement to explain purpose, side-effects, and calling conventions. Ensure the first line is a standalone summary sentence.