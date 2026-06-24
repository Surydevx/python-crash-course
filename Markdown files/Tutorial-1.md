# Python Crash Course: Chapters 1, 2 & 3

These notes cover the fundamentals of Python, including variables, data types, loops, and lists.

## 1. Variables and Print Function

Variables aren't just containers for data in Python; they are mere labels (names) you can assign to a container in RAM storing certain values.

```python
print("hello world")

x = "hello surya"
print(x) # The print function prints values of variables too.

```

## 2. Strings

Strings must be enclosed in quotes (both single `''` or double `""` quotes work). They function like an array, storing data as a sequence of characters, python ignores string literals which aren't assigned to any values, we can use this fact to comment on code.

```python
x = "hello the string must be encoded in quotes, both single or double quotes works"
print(x[0]) # Prints the first character of the string

```

### Looping Through Strings

Looping variables can take any values as long as the looping data type is iterable. The keyword `in` literally assigns values of each character in the string to the looping variable as for loops uses iterator protocol.

```python
# Iterating over the length of the string
for _ in range(len(x)):
    print(x[_]) # For loops are inherently made to traverse linear data types.

```

*(Note: While loops evaluate a condition each time and don't modify the looping variable automatically, whereas `for` loops do modify the variable by asking "what is the next value?" and the last assignment to looping variable is saved in the memory during runtime of programme.)*

### The `range()` Function

It formally takes input as `range(start, stop, step)` with a default start of 0 and step size of 1, if the only input is an integer number. `range()` function works on lazy evaluation of the values saving memeory space.

```python
z = range(7) # 7 is a prime no. fun fact :)
print(z) # Prints "range(0,7)" because it generates numbers only when asked, i.e lazy evaluation.

for _ in z:
    print(_) # "_" takes values in "z" starting at "0", "1", up to "n-1"

```

## 3. String Methods

Generally, methods on strings don't change the original string (since strings are **immutable**). They just give a new output. The syntax is `variable_name.method_name()`. Methods are actions that Python can perform on objects in memory using syntax `object_name.method_name()`.

```python
yapping = "yadayada blabla"
print(yapping.title()) # Capitalizes the first letter of words separated by a space.

dumb_string = " some dumb text placeholder        "
print(dumb_string.strip()) # Removes whitespaces from both ends.
print(dumb_string) # Original string remains unchanged!

```

*Note: Varieties of `strip()` include `lstrip()` (left) and `rstrip()` (right). Another method is `removeprefix("prefix")` which removes specific starting values.*

### Formatted Strings (f-strings) & Escape Sequences

Traditionally, concatenating strings with integers was messy and caused errors. Formatted strings let you insert variables directly.

```python
stupid_string = "some placeholder string"
stupid_numerical_value = 3 # 3 is a prime number fun fact :)

print(f"hello this is a formatted string and here is your another string {stupid_string} and some stupid numerical value {stupid_numerical_value}")

```

Use **escape sequences** (`\t`, `\n`, `\\`, `\'`, `\"`) to include special or illegal characters inside a string.

```python
x = "hello this is a \"demo\" of escape sequences."
print(x)

```

## 4. General Notes on Variables & Math

* **Smart Variables:** You can assign mathematical operations (like `x = 3*2` or `3/2`). Python follows the order of operations (BODMAS or PEMDAS).
* **Large Numbers:** Underscores can be used to make large numbers readable without affecting compilation (e.g., `10_000_000_000`).
* **Multiple Assignments:** * `x, y, z = 1, 2, 3`
* `x = y = z = 1`


* **Constants:** Python doesn't have a built-in constant type. Programmers use ALL_CAPS (e.g., `MY_CONSTANT`) to denote a variable that should never be changed.

## 5. Lists

Lists are a linear, ordered data type that can hold multiple data types. Since they are ordered, you can access elements using an index (starting at 0).

```python
stupid_list = ["hello", 2, 3.5, 2+3j] # Python has an inbuilt data type for complex numbers!
print(stupid_list[0])

# Looping through a list
for _ in stupid_list:
    print(_)

```

### Indexing and Slicing

You can chain string methods onto list elements if they are strings. You can also use negative indexing to access elements from the end of the list. Btw this operation is defined for both strings and lists.

```text
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
   0   1   2   3   4   5  
  -6  -5  -4  -3  -2  -1    
# consider indexes as pointing between characters, the main reason for this is to ensure the fluidity of concept s[:i] + s[i:] is always equal to s, where 's' is some string.
```

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-1].title()) # Prints the last element
print(f"My first bicycle was a {bicycles[0].title()}.")

```

### Modifying Lists (Mutable Nature)

Unlike strings, lists are mutable. You can change, add, or remove elements.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

# Modifying an element
motorcycles[0] = 'ducati'

# Appending to the end
motorcycles.append("ducati")

# Inserting at a specific index
motorcycles.insert(0, 'ducati')

```

### Removing Elements

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

# 1. Using the 'del' statement (by index)
del motorcycles[0]

# 2. Using the 'pop()' method (removes and returns the element)
# Assumes list is a stack i.e. the last element is on the top of the stack. pop() removes the top (last element of list) element of stack by default.
popped_motorcycle = motorcycles.pop() 
first_owned = motorcycles.pop(0) # Pops specific index

# 3. Using the 'remove()' method (by value)
motorcycles.remove('ducati') 
# Note: remove() only deletes the first occurrence of the value!

```

## 6. Organizing a List

### Sorting Permanently (`sort` method)

Changes the original list to a sorted list alphabetically or numerically.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
cars.sort(reverse=True) # Sorts in reverse alphabetical order

```

### Sorting Temporarily (`sorted` function)

Returns a sorted version of the list without modifying the original.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))

mynumbers = [1,2,3,9,5,7,6,8,0,3,4,5,2,86,4,788,57,3,545]
print(sorted(mynumbers))

```

*Note: You cannot sort a list containing a mix of integers and strings. This will throw a `TypeError: '<' not supported between instances of 'int' and 'str'`.*

### Reversing a List

The `reverse()` method flips the order of the list permanently (not backward-alphabetical, just reverse order).

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse() 
# You can reverse it again to restore the original order.

```

### Finding Length

Use the `len()` function to find how many elements are in a list.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # Output: 4

```
**Thank you**