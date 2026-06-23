# Tutorial 2

This portion covers **Loops**, working with built-in list functions, list slicing, and Tuples.

## 1. `for` Loops

A `for` loop is generally used to loop through a sequence. The interpreter automatically assigns the next value in the sequence to the looping variable for each iteration. You do not manually modify the looping variable.

```python
magicians = ['alice', 'david', 'carolina']

# The interpreter takes the first value in "magicians" and assigns it to "magician".
for magician in magicians: 
    print(magician)

```

### Indentation and Loop Scope

Python doesn't use curly brackets to define loop boundaries; it uses **indentation**. The colon (`:`) indicates that the next indented block is the start of the loop.

```python
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    # This print statement will run each time the loop runs.
    print(f"{magician.title()}, that was a great trick!")

# After the loop terminates, the looping variable is still in memory!
print(f"I can't wait to see your next trick, {magician.title()}.\n")

```

## 2. The `range()` and `list()` Functions

### The `range()` Function

The `range(start, stop, step)` function takes three inputs. By default, it starts from `0`, uses a step size of `1`, and stops *before* the exact number specified as the "stop" input.

```python
for value in range(1, 5):
    print(value) # This will only print values 1, 2, 3, and 4

```

### The `list()` Function

By default, `range()` just stores variables and doesn't generate a raw list in memory. You can force it to generate a list using the `list()` function.

```python
numbers = list(range(1, 6))
print(numbers) # Output: [1, 2, 3, 4, 5]

```

You can use the `list()` function to convert strings, tuples, sets, and dictionaries into lists:

```python
# Strings
print(list("Any string written inside quotes would become a list"))

# Tuples (Since tuples are immutable, converting them to lists lets you modify their contents)
my_tuple = ("apple", "banana", "cherry")
print(list(my_tuple))

# Sets (Note: Order of the new list isn't guaranteed since sets are unordered)
my_set = {10, 20, 30}
print(list(my_set)) # Output: [10, 20, 30]

# Dictionaries (By default, it only extracts the keys)
my_dict = {"name": "Alice", "age": 25}
print(list(my_dict)) # Output: ['name', 'age']

```

## 3. Simple Statistical Functions

You can use built-in functions to easily perform calculations on a list of numbers.

```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits)) # Finds the minimum digit in a list
print(max(digits)) # Finds the maximum digit in a list
print(sum(digits)) # Finds the sum of digits in a list

```

## 4. List Slicing and Copying

### Slicing a List

Syntax: `list_name[starting_index:stopping_index]`

**Important Rule:** Lists flow left to right. Even with negative indexing, the start index must represent an element geographically to the left of the stop index.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

# Empty string as output because start index (-1) is to the right of stop index (-4)
print(players[-1:-4]) 

# Correct flow: Left to Right
print(players[-4:-1]) 

```

### Copying a List

If you slice a list without specifying a start or stop index `[:]`, it creates an entirely independent copy of the list.

```python
my_foods = ['pizza', 'falafel', 'carrot cake']

# This creates an independent copy
friend_foods = my_foods[:] 

# If you used "friend_foods = my_foods", both names would point to the exact same 
# object in memory, meaning appending to one would append to both!

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

```

## 5. Tuples

Tuples are essentially glorified lists with two main rules:

1. **Immutable:** You cannot change the original tuple once you declare it.
2. **Ordered:** Like lists, you can access elements using their indexes.

```python
example_tuple = (20, 30, 40, 's', 'b', 'd', "surya", "sury")

# Looping through tuples works the same way as lists
for _ in example_tuple:
    print(_) 

```

### Tuple Syntax and "Modifying" Tuples

Tuples are technically defined by the presence of a comma; the parentheses just make them look neater. To define a tuple with one element, you **must** include a trailing comma: `my_t = (3,)`.

Because they are immutable, to "edit" a tuple, you actually have to make a new instance of a tuple object in memory and assign the same name to it. Python's garbage collector then clears the old, unreferenced object.

```python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Overwriting the variable with a completely new tuple object
dimensions = (400, 100) 
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

```
