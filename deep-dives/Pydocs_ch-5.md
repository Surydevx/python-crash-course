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
print(fruits.count('tangerine'))
# 0
print(fruits.index('banana'))
# 3
print(fruits.index('banana', 4))  # Find next banana starting at position 4
# 6
fruits.reverse()
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
# 'pear'
```

*Note: Methods that modify the list (like `sort` or `append`) return `None`, not the list itself.*

### Lists as Stacks and Queues

* **Stack (Last-In, First-Out):** Lists work great as stacks. Use `append()` to push and `pop()` to pull the top item.

```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
# [3, 4, 5, 6, 7]
stack.pop()
# 7
stack
# [3, 4, 5, 6]
stack.pop()
# 6
stack.pop()
# 5
stack
# [3, 4]

```
* **Queue (First-In, First-Out):** Lists are *terrible* for queues because inserting at the beginning is slow. Instead, import and use `collections.deque` for fast appends and pops from both ends.

```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### List Comprehensions

A concise way to create lists without writing bulky `for` loops.

```python
# The old way:
squares = []
for x in range(10):
    squares.append(x**2)

# The list comprehension way:
squares = [x**2 for x in range(10)]

# With a condition (filter):
evens = [x for x in range(10) if x % 2 == 0]

```

### The `del` Statement

Unlike `remove()` which deletes by *value*, `del` deletes an item by its *index* or slice.

```python
a = [10, 20, 30, 40]
del a[0]    # Removes 10
del a[1:3]  # Removes a slice

```

---

## 2. Tuples (Immutable Sequences)

Tuples are like lists, but they **cannot be changed** after creation. They are written with parentheses `()`.

* **Immutability:** You cannot assign a new value to a tuple index (e.g., `t[0] = 5` causes an error).
* **Ordered:** you can access the elements  using index, supports 0 based indexing.
* **Packing and Unpacking:** You can pack multiple values into a tuple and unpack them into variables.

```python
# Packing
my_tuple = 123, 456, "hello" 

# Unpacking
x, y, z = my_tuple 

```

* **Single-item tuples:** To make a tuple with one item, you *must* include a comma: `singleton = ("hello",)`

---

## 3. Sets (Unordered & Unique)

A set is an unordered collection where **duplicates are automatically removed**. They are created using curly braces `{}` or the `set()` function. *(Note: `{}` creates an empty dictionary, so use `set()` for an empty set).*

Sets are incredibly fast for checking if an item exists ("membership testing") and support math operations:

```python
a = set('abracadabra')
b = set('alacazam')

a - b  # Difference: letters in 'a' but not in 'b'
a | b  # Union: letters in either 'a' or 'b'
a & b  # Intersection: letters in BOTH
a ^ b  # Symmetric Difference: letters in 'a' or 'b' but NOT both

```

---

## 4. Dictionaries (Key-Value Pairs)

Dictionaries store data in `key: value` pairs. They are written with curly braces `{}`.

* **Keys:** Must be unique and **immutable** (strings, numbers, or tuples). You cannot use a list as a key.
* **Values:** Can be anything.
* **Accessing data:** `my_dict['key']` gets the value. If the key doesn't exist, it crashes.
* **Safe access:** Use `my_dict.get('key')` instead. It returns `None` (or a default value you choose) instead of crashing if the key is missing.

```python
user = {"name": "Jack", "age": 25}
user["job"] = "Developer" # Adds a new key-value pair

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



---

## 6. Conditions and Comparisons

* **Chaining:** You can chain math comparisons naturally: `a < b == c`.
* **Membership & Identity:** Use `in` / `not in` to check if an item is inside a collection. Use `is` / `is not` to check if two variables point to the exact same object in memory.
* **Short-Circuiting:** The `and` and `or` operators stop evaluating as soon as they know the answer. In `A and B`, if `A` is False, Python doesn't even look at `B`.
* **Sequence Comparisons:** Lists and strings are compared lexicographically (dictionary order). It checks the first items, then the second items, etc. `[1, 2, 3] < [1, 2, 4]` is True because 3 is less than 4.