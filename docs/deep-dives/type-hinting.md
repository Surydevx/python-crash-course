# Type Hinting


It’s called Type Hinting, and it was added to Python to make code easier to read and debug. It does not actually change how the code runs. It's just a label telling you what data types to expect.

nums: list[int]: This tells you that the input variable nums is expected to be a list filled with integers (int). If you passed a list of strings, Python wouldn't crash immediately, but your code editor might give you a warning.

-> int: The little arrow at the end tells you what the function is going to return. In this case, it promises to return an integer.

The "Plain English" Translation
If we stripped away the class and the type hints, the function would look like the standard Python function you're already used to:

```
Python
def removeDuplicates(nums):
    # Your code goes here
    return 5  # Returns an integer
```
All the extra syntax is just saying: "This is a method named removeDuplicates. It expects a list of integers as an input, and when it's done running, it will give you back a single integer."

## The Syntax Formula

When writing a function, use a **colon (`:`)** after a variable to state its input type, and a **thin arrow (`->`)** before the final colon to state the return type.

```python
def function_name(parameter: input_type) -> return_type:

```

---

## How to Perform It (Common Examples)

Here is a quick reference guide for the most common data types you will use:

### 1. Basic Data Types

For simple types like integers, strings, floats, and booleans, just use their standard Python names:

```python
def greet_user(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old!"

```

### 2. Lists, Dictionaries, and Sets

When you want to hint at collections, you specify the collection type, and then put the *inner* data type inside square brackets `[]`.

```python
# A list filled with floats
def calculate_average(grades: list[float]) -> float:
    return sum(grades) / len(grades)

# A dictionary with string keys and integer values
def get_user_age(database: dict[str, int], user: str) -> int:
    return database[user]

```

### 3. Multiple Possible Types (Optional / Union)

Sometimes a variable could be a couple of different things. For example, a function might return a `str` if it succeeds, or `None` if it fails. You can use the **pipe symbol (`|`)** to mean "or":

```python
# item can be an integer OR a string; returns a boolean
def check_inventory(item: int | str) -> bool:
    # code here
    return True

```

---

> 💡 **Important reminder:** Python is still a dynamically typed language. Type hints are like **sticky notes** for you and your code editor (like VS Code or PyCharm). If you pass a `float` into a function hinted for an `int`, Python will still run the code—but your editor will highlight it in yellow to warn you that you might be making a mistake!