# Python Data Structures: A Simplified Guide

This guide breaks down Python's core data structures, how to use them, and the best techniques for iterating and comparing data.

---

## 1. Lists (Mutable Sequences)

Lists are ordered collections of items that you can change (mutable).

### Common List Methods

* **`append(x)`**: Adds `x` to the end.
* **`extend(iterable)`**: Adds all items from another collection to the end.
* **`insert(i, x)`**: Inserts `x` at index `i`.
* **`remove(x)`**: Removes the *first* item matching `x`.
* **`pop([i])`**: Removes and returns the item at index `i` (defaults to the last item).
* **`clear()`**: Empties the entire list.
* **`index(x)`**: Finds the index of the first `x`.
* **`count(x)`**: Returns how many times `x` appears.
* **`sort()`**: Sorts the list in place.
* **`reverse()`**: Reverses the list in place.

```python
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
# 2
fruits.sort()
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']

```

> *Note: Methods that only modify the list (like `sort`, `append`, `reverse`) return `None`, not the list itself. This is a strict design principle across all mutable data structures in Python.*

### Lists as Stacks and Queues

* **Stack (Last-In, First-Out):** Lists work great as stacks. Use `append()` to push and `pop()` to pull the top item.
* **Queue (First-In, First-Out):** Lists are *terrible* for queues because inserting at the beginning is slow (all other elements must shift by one in memory). Instead, import and use `collections.deque` for fast appends and pops from both ends.

```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           
queue.popleft() # Instantly removes and returns 'Eric'                

```

### List Comprehensions (and Nesting)

A concise way to create lists without writing bulky `for` loops.

```python
# Standard comprehension with a filter condition:
evens = [x for x in range(10) if x % 2 == 0]

# Nested comprehension (e.g., flattening a 2D list):
vec = [[1,2,3], [4,5,6], [7,8,9]]
flat = [num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

```

### The `del` Statement

Unlike `remove()` which deletes by *value*, `del` deletes an item by its *index* or slice without returning it.

```python
a = [10, 20, 30, 40]
del a[0]    # Removes 10
del a[1:3]  # Removes a slice
del a[:]    # Clears the entire list

```

---

## 2. Tuples (Immutable Sequences)

Tuples are like lists, but they **cannot be changed** after creation. They are written with parentheses `()`.

* **Immutability:** You cannot assign a new value to a tuple index (e.g., `t[0] = 5` causes a `TypeError`). However, if a tuple contains a mutable object (like a list), you *can* change the contents of that list.
* **The Philosophy (Tuples vs. Lists):**
* **Lists** are usually homogeneous (store multiple items of the *same* type) and are accessed by looping.
* **Tuples** are usually heterogeneous (store *different* types of data, like a single database record: `("Alice", 25, "Engineer")`) and are accessed by unpacking.


* **Packing and Unpacking:** You can pack multiple values into a tuple and unpack them into variables.

```python
# Packing
my_tuple = 123, 456, "hello" 

# Unpacking
x, y, z = my_tuple 

```

> *Quirk: To make a tuple with one item, you must include a trailing comma: `singleton = ("hello",)*`

---

## 3. Sets (Unordered & Unique)

A set is an unordered collection where **duplicates are automatically removed**. They are incredibly fast for "membership testing" (`in` / `not in`).

* **Creation:** Created using curly braces `{}` or the `set()` function. *(Note: `{}` creates an empty dictionary, so use `set()` for an empty set).*
* **Math Operations:** Sets support union, intersection, and differences.
* **Set Comprehensions:** Just like lists, you can generate sets on the fly.

```python
a = set('abracadabra')
b = set('alacazam')

a - b  # Difference: letters in 'a' but not in 'b'
a | b  # Union: letters in either 'a' or 'b'
a & b  # Intersection: letters in BOTH
a ^ b  # Symmetric Difference: letters in 'a' or 'b' but NOT both

# Set Comprehension:
unique_consonants = {x for x in 'abracadabra' if x not in 'abc'}

```

---

## 4. Dictionaries (Key-Value Pairs)

Dictionaries store data in `key: value` pairs.

* **Keys:** Must be unique and **immutable** (strings, numbers, or tuples). You cannot use a list as a key.
* **Accessing data:** `my_dict['key']` gets the value. If the key doesn't exist, it raises a `KeyError`.
* **Safe access:** Use `my_dict.get('key')` instead. It returns `None` (or a default value you choose) instead of crashing if the key is missing.

### Dictionary Comprehensions and Merging

```python
# Dict Comprehension:
squares_dict = {x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}

# Merging (Python 3.9+):
user = {"name": "Jack"}
job_info = {"job": "Dev", "age": 25}

combined = user | job_info 
# {"name": "Jack", "job": "Dev", "age": 25}

```

---

## 5. Pro Looping Techniques

Python has built-in functions to make `for` loops cleaner and more powerful:

* **Looping Dictionaries (`items`):** Gets both the key and the value.
```python
for key, value in my_dict.items():

```


* **Getting the Index (`enumerate`):** Gets both the index number and the value of a sequence.
```python
for index, value in enumerate(['a', 'b', 'c']):

```


* **Looping Multiple Lists at Once (`zip`):** Pairs up items from two or more lists.
```python
for question, answer in zip(questions, answers):

```


* **Looping Backwards (`reversed`):**
```python
for item in reversed(my_list):

```


* **Looping in Order (`sorted`):** Returns a temporary sorted version without changing the original data.
```python
for item in sorted(my_list):

```


* **Looping Unique Items in Order:** Combine `sorted()` and `set()`.
```python
for item in sorted(set(my_list)):

```



---

## 6. Conditions and Comparisons

* **Chaining:** You can chain math comparisons naturally: `a < b == c`.
* **Membership & Identity:** Use `in` / `not in` to check if an item is inside a collection. Use `is` / `is not` to check if two variables point to the exact same object in memory.
* **Short-Circuiting:** The `and` and `or` operators stop evaluating as soon as they know the answer. In `A and B`, if `A` is False, Python doesn't even look at `B`.
* **Sequence Comparisons:** Lists and strings are compared lexicographically (dictionary order). It checks the first items, then the second items, etc. `[1, 2, 3] < [1, 2, 4]` is True because 3 is less than 4.
* **The Walrus Operator (`:=`):** In Python, unlike C, you cannot accidentally type `=` when you meant `==` inside an `if` statement because assignment inside an expression is explicitly banned. If you *want* to assign a variable inside an expression, you must explicitly use the walrus operator `:=`.