# Tutorial 5

This tutorial covers **User Inputs**, the modulo operator, and deep dives into **`while` Loops**—specifically how to safely use them to modify lists and dictionaries without breaking Python's iterator protocol.

---

## 1. User Inputs

The `input()` function pauses your program and waits for the user to enter text. It takes one argument: a **prompt** string that tells the user what kind of information to enter.

```python
name = input("Enter your name: ")
print(name)

```

### Multiline Prompts

If your prompt spans multiple lines, you can assign it to a variable using triple quotes (`"""`), and then pass that variable to the `input()` function.

```python
prompt = """If you share your name, we can personalize the messages you see.
What is your first name? """

name = input(prompt)
print(f"\nHello, {name}!")

```

### The String Trap & Typecasting

The `input()` function **always** converts whatever the user enters into a string (`str`). If you expect a number, this can cause critical bugs.

```python
age = input("How old are you? ") # Let's say the user types 20
print(type(age))                 # Output: <class 'str'>

# print(age >= 18) 
# ERROR: TypeError: '>=' not supported between instances of 'str' and 'int'

```

To fix this, use the `int()` function to **typecast** the string into an integer. You can even use function composition to do this in one line:

```python
# Taking input and converting to integer simultaneously
age = int(input("How old are you? "))
print(type(age)) # Output: <class 'int'>
print(age >= 18) # Output: True

```

---

## 2. The Modulo Operator

The modulo operator (`%`) divides one number by another and returns the **remainder**.

```python
print(5 % 3) # Output: 2

```

---

## 3. `while` Loops

A `while` loop essentially keeps looping until its conditional statement evaluates to `False`. Unlike a `for` loop, you must increment or decrement the looping variable manually.

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 # Manual increment

```

### Flags

Flags are a concept where you use a standard boolean variable (`True` or `False`) to act as a master signal that controls the overall state of your program. This keeps your `while` loop conditions clean instead of stringing together massive `and`/`or` statements.

```python
prompt = "\nEnter 'quit' to end the program. "
active = True # This is our Flag

while active:
    message = input(prompt)
    if message == 'quit':
        active = False # Flips the flag, killing the loop on the next check
    else:
        print(message)

```

### `break` and `continue`

* **`break`**: Immediately kills the loop and transfers the program's control flow to the next line of code outside the loop.
* **`continue`**: Immediately kills the *current iteration* of the loop, skipping any code below it, and jumps back up to the loop header to re-evaluate the condition.

```python
# Example of break
number = 1
while number <= 5:
    if number == 3:
        break  # Loop completely terminates after printing 1 and 2
    print(number)
    number += 1

# Example of continue
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue  # Skips the print statement for 3 and jumps back to the top
    print(number)

```

---

## 4. Modifying Lists and Dictionaries in Loops

> **🚨 DANGER ZONE:** You should **never** modify a list or dictionary inside a `for` loop.
>
> * With dictionaries, changing the size triggers a `RuntimeError`.
> * With lists, it causes silent bugs because `for` loops blindly follow an internal counter (the iterator protocol). If you delete index 1, the memory shifts left. The next item slides into index 1, but the loop counter moves to index 2, completely skipping an element!
>
>

To safely modify data structures as you work through them, use a `while` loop. A `while` loop does not rely on the iterator protocol; it just checks a boolean condition each time.

*(Note: Any list or dictionary evaluates to `True` until it is completely empty, at which point it evaluates to `False`.)*

### Transferring Items Between Lists

```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Runs until unconfirmed_users is completely empty
while unconfirmed_users: 
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

```

### Removing All Instances of a Value

The `.remove()` method only removes the *first* instance of a value. To remove them all, combine it with a `while` loop.

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat') 

print(pets) 
# Output: ['dog', 'dog', 'goldfish', 'rabbit']

```

### Populating a Dictionary on the Fly

You can collect, store, and organize user input directly into a dictionary using a flag.

```python
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Check if we should keep the loop running
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

```
