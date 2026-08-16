# Python Boolean Values

In Python, Boolean values represent one of two states: `True` or `False`.

We frequently evaluate expressions to yield a Boolean value. This typically happens when using comparison operators, membership operators, or when generally evaluating the "truthiness" of data.

```python
# Evaluating comparison operators
print(10 > 9)   # Returns True
print(10 == 9)  # Returns False
print(10 < 9)   # Returns False

```

### Using Booleans in Conditions

Comparison operators returning Booleans are the foundation of conditional logic, such as `if` statements:

```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

```

---

## The `bool()` Function

You can use the built-in `bool()` function to evaluate any object or value. It will return either `True` or `False` based on Python's rules for "truthiness" and "falsiness."

```python
print(bool("Hello"))  # Returns True
print(bool(15))       # Returns True

```

### Truthy Values (Most Values are True)

Almost any value is evaluated to `True` if it contains some sort of content.

* **Strings:** Any string is `True`, except for empty strings.
* **Numbers:** Any number is `True`, except `0`.
* **Collections:** Any list, tuple, set, or dictionary is `True`, except for empty ones.

```python
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

```

### Falsy Values

There are very few values that evaluate to `False`. They generally represent "empty" or "null" concepts:

* The boolean `False`
* The `None` object
* The number `0`
* Empty sequences and collections: `""`, `()`, `[]`, `{}`

```python
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

```

### Objects with Custom Lengths

Another scenario where an object evaluates to `False` is if you are dealing with a custom class that has a `__len__()` method configured to return `0` or `False`.

```python
class MyClass:
    def __len__(self):
        return 0

my_obj = MyClass()
print(bool(my_obj))  # Returns False

```

---

## Booleans as Return Values

Functions can be designed to return Boolean values, which is highly useful for writing clean, readable conditions.

```python
def my_function():
    return True

print(my_function())

```

Here is a practical example of using a Boolean-returning function directly within a conditional statement:

```python
def my_function():
    return True

if my_function():
    print("YES!")
else:
    print("NO!")

```

> **Note:** Python also has several built-in functions that return Boolean values. A common example is the `isinstance()` function, which checks if an object is instance of a class or not.