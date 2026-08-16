# Python Tutorial 2: Classes & OOP

Unlike languages like C++ or Java that force you into massive boilerplate to do Object-Oriented Programming, Python’s class mechanism adds a minimum of new syntax. Classes in Python are extremely dynamic—they are created at runtime, and you can modify them on the fly.

Here is how Python actually handles objects, memory, and inheritance behind the scenes.

---

## 1. The Pre-Requisite: Namespaces and Scopes

Before you understand classes, you have to understand how Python stores variables.

A **namespace** is literally just a mapping from names to objects. Under the hood, almost all namespaces in Python are implemented as dictionaries. The built-in functions (`len()`, `print()`) live in one dictionary, your module's global variables live in another, and a function's local variables live in a temporary one.

**The Golden Rule of Namespaces:** There is absolutely no relation between names in different namespaces. Two different modules can both have a variable named `x` and they will never collide.

### The LEGB Scope Resolution (Again)

When you reference a variable, Python searches through namespaces in this exact order:

1. **L**ocal (inside the current function)
2. **E**nclosing (inside any wrapping functions)
3. **G**lobal (the module level)
4. **B**uilt-in (Python's core functions)

### `global` vs `nonlocal`

Because assignment (`=`) creates a local variable by default, you have to explicitly tell Python if you want to modify a variable sitting in a higher scope:

* `global spam`: Tells Python "When I say `spam`, I mean the one at the module level."
* `nonlocal spam`: Tells Python "When I say `spam`, I mean the one in the immediately enclosing function." (Used heavily in closures/nested functions).

---

## 2. Anatomy of a Class

A class is essentially an object factory. When you define a class, you create a brand new namespace.

```python
class MyClass:
    """A simple example class"""
    i = 12345           # Class variable
    
    def f(self):        # Method
        return 'hello world'

# Instantiation: Creating the actual object
x = MyClass()

```

### The Truth About `self`

In C++ or Java, the "current object" is hidden behind keywords like `this`. Python is explicit.
When you call `x.f()`, Python secretly translates it to `MyClass.f(x)`. It takes the instance (`x`) and shoves it in as the very first argument of the method. That’s why every method definition must have `self` as its first parameter.

> **Nerd Note:** `self` is **not** a reserved keyword in Python. It is purely a convention. You could name it `surya`, `this_object`, or `pizza`, and Python would execute it perfectly. But if you change it, other Python developers will hate you.

### Initialization (`__init__`)

When you instantiate a class (`x = MyClass()`), Python creates an empty object. If you want it to have a specific starting state, you define the `__init__()` dunder method. Python automatically funnels your arguments into it.

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

surya_math = Complex(3.0, -4.5)

```

---

## 3. The Mutable Class Variable Trap (Crucial)

**Instance variables** are for data unique to a specific object. **Class variables** are shared across *all* instances of the class.

If you use a mutable object (like a list) as a class variable, you will create a catastrophic bug where every instance shares the exact same list in memory.

```python
# THE TRAP (Dangerous!)
class Dog:
    tricks = []             # Class variable: Shared by ALL dogs

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')

print(e.tricks) # Output: ['roll over'] <-- Wait, Buddy didn't learn this!

```

**The Fix:** Always declare mutable data inside `__init__` as an instance variable (`self.tricks = []`).

---

## 4. Inheritance & Multiple Inheritance

Python fully supports inheritance, allowing a new class to absorb the attributes and methods of an existing one.

```python
class DerivedClassName(BaseClassName):
    pass

```

* To check an instance's type: `isinstance(obj, BaseClassName)`
* To check class hierarchy: `issubclass(DerivedClassName, BaseClassName)`

### Multiple Inheritance & MRO

Python allows a class to inherit from multiple parents (`class Child(Base1, Base2):`).
If both parents have a method named `do_work()`, which one does Python use? It uses the **Method Resolution Order (MRO)**.

Python searches:

1. The Child class itself.
2. `Base1` (Left-most parent).
3. `Base2` (Right-most parent).
It searches depth-first, left-to-right, but uses a dynamic linearization algorithm to ensure no parent is searched twice in a "diamond" inheritance structure.

---

## 5. "Private" Variables and Name Mangling

Python does **not** have true private variables. Nothing in the language enforces data hiding. We rely entirely on convention.

* `_spam`: A single leading underscore tells other programmers, "This is internal. Do not touch this. If it breaks your code later, it's your fault."
* `__spam`: Two leading underscores trigger **Name Mangling**.

**What is Name Mangling?**
If you define `__update()` inside a class named `Mapping`, Python secretly renames that function to `_Mapping__update`.
This isn't for security; it's a safety bumper. It prevents a subclass from accidentally overriding a critical internal method of the parent class if they happen to use the same variable name.

---

*(Tired? Jal lijiye! 🥛 Let's talk about looping mechanics.)*

---

## 6. Iterators: How `for` Loops Actually Work

When you write `for char in "123":`, a lot of mechanical gymnastics happen under the hood. The `for` loop secretly calls the built-in `iter()` function on the string. This returns an **Iterator Object**.

The loop then repeatedly calls `next()` on that object, grabbing one item at a time. When the container is empty, the iterator raises a `StopIteration` exception, which the `for` loop catches to know it's time to stop.

You can make your own custom objects iterable by giving them an `__iter__()` method (which returns the object itself) and a `__next__()` method (which spits out the next value or raises `StopIteration`).

---

## 7. Generators: The Magic "Pause" Button

Writing custom iterator classes is clunky. **Generators** are a much simpler way to create iterators.

A generator looks like a normal function, but instead of using `return`, it uses `yield`.

* `return` destroys the function's local variables and ends it forever.
* `yield` hits a "pause" button. It spits out the value, freezes its state in memory, and waits. The next time `next()` is called, it unpauses right where it left off.

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index] # Pauses here!

for char in reverse('golf'):
    print(char)
# Output: f l o g

```

Generators automatically handle `__iter__()`, `__next__()`, and `StopIteration` for you. They are vastly more memory-efficient than returning full lists because they only generate one value at a time.

### Generator Expressions

You can write generators on a single line, exactly like a list comprehension, but using parentheses `()` instead of square brackets `[]`.

```python
# List Comprehension: Builds the entire list in memory right now.
squares_list = [x*x for x in range(10)] 

# Generator Expression: Creates an object that will calculate squares later, one by one.
squares_gen = (x*x for x in range(10))  
print(sum(squares_gen)) # Output: 285

```

---

## 8. Odds and Ends

* **Empty Data Structures:** Need a quick C-style "struct" or Pascal "record" to just hold data? The modern, idiomatic way is to use `@dataclass`.

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)

```


* **Methods are Objects:** Because everything in Python is an object, methods can be detached from their instances and passed around like variables:

```python
xf = x.f          # Detach the method and store it in a variable
print(xf())       # Run it later

```
