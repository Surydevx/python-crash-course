# Tutorial 3

This tutorial covers **Statements**, boolean logic, and **Control Flow** (`if`, `else`, `elif` statements).

## 1. What are Statements?

"Statements" are basically assertions made in your code that evaluate to either `True` or `False` (they cannot be both at the same time). Control flow statements inherently work on this simple principle: they evaluate the statement written, and if it evaluates to `True`, a specific code block gets executed.

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars: 
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

```

### Assignment vs. Comparison

It is crucial not to mix these up:

* **Assignment Operator (`=`):** Used to assign a value to an object/variable.
* **Comparison Operator (`==`):** Used to compare the values stored in two objects. It is case-sensitive when comparing strings!
* **Not Equal Operator (`!=`):** Checks if a value is *not* equal to another.

```python
x = y  # Assignment
x == y # Comparison

```

## 2. Boolean Values & Logical Operators

Expressions that evaluate to `True` or `False` are called **boolean expressions**. Variables holding these are boolean variables. They are the fundamental building blocks of `while` loops and `if` statements.

### Using `and` & `or`

You can evaluate multiple conditions simultaneously using `and` (both must be true) or `or` (at least one must be true).

```python
# The "and" operator
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # Output: False

age_1 = 22
print(age_0 >= 21 and age_1 >= 21) # Output: True

# The "or" operator
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)  # Output: True

```

### Checking if a Value is in a List

Use the `in` and `not in` keywords to verify if a specific item exists inside a list.

```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings) # Output: True
print('pepperoni' in requested_toppings) # Output: False

# Using "not in"
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

```

## 3. Control Flow Statements

### The `if` Statement

Syntax: `if some_condition:`
The colon (`:`) tells the interpreter that the next indented line is the start of the block. If the condition is false, the program skips the block entirely.

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
print("thank you")

```

### The `if-else` Statement

This adds a catch-all block. If the `if` statement handles a specific pool of cases, `else` handles *everything* else.

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

```

> **Dev Tip: Typecasting & User Input**
> You can compose functions together! `input("Prompt")` takes text from the user. You can wrap it in a typecasting function like `int()` to instantly convert that text into an integer.

```python
age = int(input("Please enter your age: "))

if age < 18:
    print("You are under age. Find your dad and go away.")
else:
    print("You are eligible to vote, congrats.")

```

*(Note: As you level up as a dev, prioritize readability. Code is read many more times than it is written! You can actually run `import this` in Python to read the "Zen of Python" guidelines, though avoid putting random imports in the middle of your production code).*

### The `if-elif-else` Statement

When you have multiple mutually exclusive conditions, use `elif` (else-if). The interpreter checks them top-to-bottom. As soon as one evaluates to `True`, it executes that block and exits the entire control flow chain.

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ₹{price}.")

```

*Note: The `else` block at the end is entirely optional. If your `if` and `elif` statements cover all necessary logic, you can omit it.*

### Multiple `if` Statements

Use `if-elif` when only *one* valid case should execute. If your mental model allows for *multiple* valid cases to trigger simultaneously, use a series of independent `if` statements.

```python
requested_toppings = ['mushrooms', 'extra cheese']

# Every single one of these will be checked, regardless of whether 
# the previous ones were True or False.
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

```
