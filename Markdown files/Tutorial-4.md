# Tutorial 4

This tutorial covers **Dictionaries**, including how to access, modify, and deeply understand how they manage data under the hood.

## 1. Simple Dictionaries

A dictionary is a collection of key-value pairs. Each key is associated with a value, and that value can be anything: a string, integer, float, another dictionary, or even a custom object.

```python
# Syntax for a simple dictionary
temp_dict = {"key-1": "value-1", "key-2": "value-2", "key-3": "value-3"}

```

### Accessing Values

You access values using the syntax `dict_name[key]`. You use the key as your identifier.

```python
colors = {'color': 'green'}
print(colors['color']) # Output: "green"

```

## 2. Modifying Dictionaries

Dictionaries are **mutable** and (as of recent Python versions) they **respect order**—meaning key-value pairs stay in the order they were assigned.

### Adding & Editing Key-Value Pairs

You can add new pairs or edit existing ones using the syntax `dict[key] = value`.

Keys must be unique. If you assign a new value to a key that already exists, it simply overwrites the old value. Keys behave a lot like variables in this regard.

```python
temp_dict = {'blue': 10, 'red': 9, 'brown': 5, "maroon": 11, "burgundy": 8.5}
print(temp_dict)

# Overwriting the value of an existing key
temp_dict["brown"] = 9 
print(temp_dict) 
# Output: {'blue': 10, 'red': 9, 'brown': 9, 'maroon': 11, 'burgundy': 8.5}

# Adding a completely new key
colors["fav"] = "blue"

```

*Note: It is common to define an empty dictionary (`empty_dict = {}`) when you expect your program to add and remove contents over time.*

### Removing Key-Value Pairs

Use the `del` statement to permanently delete a key and its associated value.

```python
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0) # Output: {'color': 'green'}

```

## 3. The `get()` Method

If you ask a dictionary for a key that doesn't exist using the standard `dict[key]` bracket syntax, the Python interpreter will crash with a `KeyError`.

To prevent this, use the `.get()` method. It gives a graceful message or a `None` value instead of crashing.

```python
alien_0 = {'color': 'green', 'speed': 'slow'}

# Syntax: dict_name.get("searched_key", "Fallback message")
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value) 

```

*Note: If you leave out the second argument and the key doesn’t exist, Python returns `None` (a special value meaning “no value exists”).*

## 4. Looping Through Dictionaries & Sequence Unpacking

By default, looping through a dictionary only loops through its **keys**. To loop through both keys and values simultaneously, use the `.items()` method along with **sequence unpacking**.

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# Sequence unpacking: assigning two variables at once from an iterable
for key, value in user_0.items(): 
    print(f"\nKey: {key}")
    print(f"Value: {value}")

```

### Basic Unpacking Example

Unpacking works on any iterable data type (like tuples, lists, etc.), provided the number of variables matches the number of elements.

```python
student_info = ("Alice", 24, "Computer Science")
name, age, major = student_info

print(name)  # Output: Alice
print(age)   # Output: 24

```

## 5. Deep Dive: Dictionary View Objects (The Conspiracy Board)

When you call dictionary methods like `.keys()`, `.values()`, or `.items()`, they do *not* return static lists. They return **Dictionary View Objects** (`dict_keys`, `dict_values`, `dict_items`).

* None of these view objects actually hold data. They only hold memory addresses pointing to the actual dictionary.
* They dynamically access the dictionary. If the main dictionary updates, the view object reflects the change instantly.

```python
user_env = {
    'os': 'Arch Linux', # Yes, I use Arch btw.
    'shell': 'Zsh',
    'editor': 'Nvim'
}

# view is a dynamic reference, not a static copy!
view = user_env.items() 

user_env['terminal'] = 'Alacritty'

print(view)
# Instantly reflects the change:
# dict_items([('os', 'Arch Linux'), ('shell', 'Zsh'), ('editor', 'Nvim'), ('terminal', 'Alacritty')])

```

### Why does `.items()` use Tuples?

When `.items()` serves you a key-value pair, it does so inside a **Tuple**. Out of all data types, the tuple is the only one that is both **ordered** (so index 0 is always the key, index 1 is always the value) and **immutable**.

Immutability saves us from side effects. If `.items()` returned a mutable list, you could accidentally overwrite your data mid-iteration!

```python
# Imagine if it gave you a list instead of a tuple...
# pair[0] = 'hacked_key' -> This would be disastrous!

```

### The Hash Table Danger Zone

Dictionaries are fundamentally hash tables. Because of this, you should **never** change the size of a dictionary (adding or removing keys) *while* iterating over it.

```python
my_dict = {"A": 1, "B": 2}

for key, value in my_dict.items():
    my_dict["C"] = 3  # Triggers dynamic hash table resizing in RAM!
    print(key, value)

# Throws: RuntimeError: dictionary changed size during iteration

```

## 6. Sorting and Unique Values

### Using `sorted()`

Because dictionaries use an iterator protocol, you can wrap a dictionary in the `sorted()` function to loop through its keys in alphabetical order, regardless of how they were originally entered.

```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")

```

### Using `set()` with `.values()`

If you want to pull only the values out of a dictionary, use `.values()`. If you expect duplicate values and want to filter them out, wrap it in the `set()` function.

*Tradeoff: Sets enforce uniqueness, but they do **not** respect order.*

```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

for language in set(favorite_languages.values()):
    print(language.title())

# Output (Unordered, but unique):
# C
# Python
# Ruby

```
