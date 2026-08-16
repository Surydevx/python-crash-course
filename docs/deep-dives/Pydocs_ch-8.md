# Python Tutorial 8: Exceptions

Even if your code is syntactically perfect, it will eventually break. A file might be missing, a user might type a word instead of a number, or the internet might drop. This chapter is about how to handle those crashes without your entire program crashing.

---

## 1. Syntax Errors vs. Exceptions

* **Syntax Errors (Parsing Errors):** You forgot a colon, a parenthesis, or misspelled a keyword. Python can't even *begin* to read your code. It stops immediately and points a little arrow `^` at the exact spot you messed up, this is called as syntax error.

* **Exceptions (Runtime Errors):** Your syntax is perfect, but the *action* is impossible. Examples: Dividing by zero (`ZeroDivisionError`), adding a string to an integer (`TypeError`), or calling a variable that doesn't exist (`NameError`).

---

## 2. The `try...except` Block

You can intercept exceptions using a `try` block. If the code inside the `try` block crashes, Python instantly jumps to the `except` block instead of killing the program.

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break # This only runs if the line above succeeds!
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

```

### The Rules of Catching:

1. **Be Specific:** You can catch multiple specific errors. If an exception happens that you *didn't* explicitly catch, the program still crashes.

```python
except (RuntimeError, TypeError, NameError):
    pass

```

2.**Order Matters:** If you have multiple except blocks, Python checks them top-to-bottom. If you try to catch a Parent class before a Child class, the Parent class will intercept the error, and the Child block will never run.

```python
class B(Exception): pass
class C(B): pass

try:
    raise C()
except B:
    print("Caught by B!") # THIS RUNS! C is a subclass of B, so B intercepts it.
except C:
    print("Caught by C!") # This is dead code and will never run.

# The Fix: Always put your most specific (child) exceptions at the top!
```


3. **The Wildcard Trap:** You can catch *any* non-fatal error by catching the base `Exception` class.

```python
except Exception as e:
    print(f"the porgramme has following exception raised at runtime: {e}")
```

> **Warning:** Always catch `Exception`, never `BaseException`. `BaseException` is the granddaddy of all errors, including `KeyboardInterrupt` (when a user hits Ctrl+C to force-quit). If you catch `BaseException`, you might accidentally make an unkillable zombie program!, this could make a legit malicious programme.

4. **Grabbing the Error Object:** You can assign the error to a variable using `as` to print its details.

> *Aliasing*: This behaviour can be understood by basically understanding aliases.

```python
try:
    1 / 0
except ZeroDivisionError as err:
    print(f"I caught an error: {err}") 

```
> *Note:* When you grab an error object using as e, you aren't just getting a string. You are getting a full object that stores all the arguments passed to it inside a special tuple called .args

```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(inst.args)     # Output: ('spam', 'eggs')
    x, y = inst.args     # You can unpack the error arguments!
    print(f'x = {x}')    # Output: x = spam
```

---

## 3. The `else` and `finally` Clauses

A full exception handling block actually has four parts: `try`, `except`, `else`, and `finally`.

> *OF these 4 blocks only first two are necessary, Other 2 provides extra functionality but aren't required.*

### The `else` Clause (The "Success" Block)

The `else` block runs **only if the `try` block succeeds completely** without throwing any exceptions.

* *Why not just put that code in the `try` block?* To protect yourself. If you put too much code in the `try` block, you might accidentally catch an error triggered by code you didn't intend to protect. Keep your `try` blocks as short as possible.

### The `finally` Clause (The "Cleanup" Block)

The `finally` block executes **no matter what happens**.

* If the `try` succeeds, `finally` runs.
* If the `try` fails and is caught, `finally` runs.
* If the `try` fails and is *not* caught, `finally` runs right before the program crashes.
It is perfectly designed for closing files or network connections.

```python
try:
    f = open('data.txt')
except OSError:
    print('Failed to open!')
else:
    print('File opened successfully!')
finally:
    print('This prints literally no matter what.')

```

> **The Cursed `finally` Quirk:** If you put a `return` statement inside a `finally` block, it will **overwrite** the `return` statement of the `try` block. Python 3.14 actually issues a `SyntaxWarning` for this because it is so confusing. Just don't do it.

> *Note on Predefined Cleanups:* While finally is great, objects like files or network locks have built-in cleanup actions. Using the with keyword (e.g., with open("file.txt") as f:) is effectively a microscopic try...finally block that guarantees the file closes even if the code inside the block crashes.

---

## 4. Raising Exceptions manually

Sometimes, the user does something stupid and you want to crash the program on purpose. You do this using the `raise` keyword.

```python
age = -5
if age < 0:
    raise ValueError("Age cannot be negative!")

```

If you catch an exception, log it, but realize you don't know how to fix it, you can just type `raise` by itself to pass the exact same exception up the chain.

### Exception Chaining (`from`)

If you catch a database error and want to translate it into a custom application error, Python will print both errors to show the sequence of events. You can explicitly link them using `from`.

```python
try:
    open("database.sqlite")
except OSError as exc:
    # "from exc" chains them together in the traceback
    raise RuntimeError("Failed to open database") from exc 

```

*TIP:* If you want to hide the original error entirely and pretend only your new error happened, use `raise RuntimeError from None`.

---

*(Tired? Jal lijiye! 🥛 The next part gets a little wild with modern Python features.)*

---

## 5. Modern Features (Python 3.11+)

As Python handles more async and parallel processing, a single operation might actually trigger *multiple* errors at the exact same time.

### 5.1 Exception Groups and `except*`

You can bundle multiple errors into an `ExceptionGroup` and raise them all at once. To catch them, you use the new `except*` syntax.

`except*` is special because it doesn't just stop at the first match. It filters the group, extracts the errors it knows how to handle, and lets the rest of the unhandled errors continue crashing up the chain!

```python
try:
    # Simulating multiple simultaneous network failures
    raise ExceptionGroup("Network issues", [OSError("Failed"), TypeError("Bad data")])
except* OSError as e:
    print("Handled the OS Errors!")
except* TypeError as e:
    print("Handled the Type Errors!")

```

### 5.2 Enriching Exceptions (`add_note()`)

Sometimes an error happens, and you catch it, but you want to attach a sticky note to it with some extra context before raising it again. You can do this with `.add_note()`.

```python
try:
    1 / 0
except Exception as e:
    e.add_note("This happened while calculating the user's tax return.")
    raise

```

The traceback will now print your custom note at the very bottom, making debugging significantly easier.

---

## 6. Custom/User-Defined Exceptions

You can invent your own errors. All you have to do is create a class that inherits from the built-in `Exception` class. By convention, you should name it with "Error" at the end.

```python
class InsufficientFundsError(Exception):
    pass # You don't even need to write any code inside it!

balance = 10
if balance < 20:
    raise InsufficientFundsError("You are too broke to buy this.")

```
