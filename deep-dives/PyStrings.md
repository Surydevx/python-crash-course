# Python Strings

In Python, a **string** (`str`) is a fundamental data type used to represent text. Under the hood, a string is a sequence of Unicode characters.

One of the most important rules about strings in Python is that they are **immutable**—meaning once a string is created in memory, it cannot be changed. Any operation that modifies a string actually creates a brand-new string behind the scenes.

---

## 1. String Syntax & Creation

You can create strings using single quotes, double quotes, or triple quotes. Python treats single and double quotes exactly the same, which gives you flexibility if your text includes quotes inside it.

```python
# Single and Double Quotes
first_name = 'Alice'
last_name = "Smith"

# Handling quotes inside quotes
sentence = "It's a beautiful day!" 
quote = 'He said, "Python is awesome!"'

# Triple Quotes (for multiline strings or docstrings)
paragraph = """This string
spans across
multiple lines."""

```

---

## 2. Accessing Characters (Indexing & Slicing)

Because a string is a sequence, you can access individual characters using their **index** (position). Python uses zero-based indexing.

### Indexing

You access a single character using square brackets `[]`.

```python
word = "Python"

# Positive Indexing (Left to Right, starts at 0)
print(word[0])  # Output: P
print(word[3])  # Output: h

# Negative Indexing (Right to Left, starts at -1)
print(word[-1]) # Output: n
print(word[-2]) # Output: o

```

### Slicing

You can extract a substring using the slicing syntax: `[start:stop:step]`. Note that the `stop` index is *exclusive* (it stops before that number).

```python
word = "Programming"

print(word[0:7])   # Output: Program (Indices 0 through 6)
print(word[:4])    # Output: Prog (Defaults to start at 0)
print(word[7:])    # Output: ming (Defaults to end of string)
print(word[::2])   # Output: Pormig (Skips every second character)
print(word[::-1])  # Output: gnimmargorP (Reverses the string!)

```

---

## 3. String Formatting (f-strings)

The most modern, readable, and efficient way to inject variables into strings in Python is by using **f-strings** (formatted string literals). Just put an `f` before the opening quote and wrap variables in curly braces `{}`.

```python
name = "Surya"
age = 20

# Using f-strings
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# You can even do math or call functions inside the braces
print(f"In 5 years, I will be {age + 5}.")
print(f"My name uppercase is {name.upper()}.")

```

---

## 4. String Methods

**Important Note for All Methods:** Strings in Python are **immutable**. None of these methods alter the original string; they all return a *new* string (or a boolean/integer).

---

## 1. Case Conversion Methods

* **`capitalize()`**
* **How it works:** Converts the first character of the string to uppercase and forces all remaining characters to lowercase.
* **Example:** `"hello WORLD".capitalize()` returns `"Hello world"`.
* **When it fails/Gotchas:** If the first character is a number or symbol, it does nothing to the first character but still lowercases the rest (e.g., `"1st PLACE".capitalize()` returns `"1st place"`).


* **`casefold()`**
* **How it works:** Similar to `lower()`, but much more aggressive. It is designed to remove all case distinctions for unicode strings (useful for matching strings in different languages).
* **Example:** `"Fluß".casefold()` returns `"fluss"` (German esszet becomes 'ss').
* **When it fails/Gotchas:** It doesn't "fail," but it shouldn't be used for standard display formatting, only for behind-the-scenes string comparisons.


* **`lower()`**
* **How it works:** Converts all uppercase characters to lowercase.
* **Example:** `"PYTHON".lower()` returns `"python"`.


* **`upper()`**
* **How it works:** Converts all lowercase characters to uppercase.
* **Example:** `"python".upper()` returns `"PYTHON"`.


* **`swapcase()`**
* **How it works:** Inverts the case of every character. Upper becomes lower, lower becomes upper.
* **Example:** `"PyThOn".swapcase()` returns `"pYtHoN"`.


* **`title()`**
* **How it works:** Capitalizes the first letter of every word.
* **Example:** `"hello world".title()` returns `"Hello World"`.
* **When it fails/Gotchas:** It uses simple rules and will capitalize letters following an apostrophe. `"they're".title()` returns `"They'Re"`.



---

## 2. Trimming and Justifying Methods

* **`strip()`**, **`lstrip()`**, **`rstrip()`**
* **How it works:** Removes characters from both ends (`strip`), just the left (`lstrip`), or just the right (`rstrip`). By default, it removes whitespace. You can pass a string of characters to remove instead.
* **Example:** `"   hello   ".strip()` returns `"hello"`. `"xxoxx".strip("x")` returns `"o"`.
* **When it fails/Gotchas:** It removes *combinations* of characters, not exact substrings. `"banana".strip("na")` returns `"b"`, not `"ba"`.


* **`center(length, character)`**, **`ljust(length, character)`**, **`rjust(length, character)`**
* **How it works:** Pads the string with a specified character (default is space) to make it a certain length. `center` puts the string in the middle, `ljust` aligns it left, `rjust` aligns it right.
* **Example:** `"hi".center(6, "-")` returns `"--hi--"`.
* **When it fails/Gotchas:** If the specified length is less than or equal to the string's current length, it does nothing and returns the original string.


* **`zfill(length)`**
* **How it works:** Pads the string on the left with zeros to reach a specified length. It smartly places zeros *after* a `+` or `-` sign.
* **Example:** `"-42".zfill(5)` returns `"-0042"`.


* **`expandtabs(tabsize)`**
* **How it works:** Replaces all tab characters (`\t`) with whitespaces. Default tabsize is 8.
* **Example:** `"a\tb".expandtabs(4)` returns `"a   b"`.



---

## 3. Searching and Replacing Methods

* **`count(value)`**
* **How it works:** Returns the number of non-overlapping occurrences of a substring.
* **Example:** `"apple".count("p")` returns `2`.


* **`find(value)`** & **`rfind(value)`**
* **How it works:** Searches for a substring and returns the starting index. `find` gets the first occurrence (left to right), `rfind` gets the last occurrence (right to left).
* **Example:** `"hello".find("l")` returns `2`.
* **When it fails/Gotchas:** If the substring is not found, it returns `-1`.


* **`index(value)`** & **`rindex(value)`**
* **How it works:** Exactly the same as `find` and `rfind`.
* **When it fails/Gotchas:** Unlike `find`, if the substring is not found, it **crashes** with a `ValueError`. Use this only when you are 100% sure the substring exists.


* **`replace(old, new, count)`**
* **How it works:** Replaces occurrences of `old` with `new`. You can optionally specify how many occurrences to replace.
* **Example:** `"cat cat cat".replace("cat", "dog", 2)` returns `"dog dog cat"`.


* **`startswith(value)`** & **`endswith(value)`**
* **How it works:** Returns `True` if the string starts or ends with the specified value, otherwise `False`.
* **Example:** `"hello.txt".endswith(".txt")` returns `True`.



---

## 4. Splitting and Joining Methods

* **`split(separator)`** & **`rsplit(separator)`**
* **How it works:** Breaks a string into a List of strings based on a separator. If no separator is provided, it splits on all whitespace. `rsplit` splits from the right (only matters if you limit the number of splits).
* **Example:** `"a,b,c".split(",")` returns `['a', 'b', 'c']`.
* **When it fails/Gotchas:** Passing an empty string `""` as a separator will throw a `ValueError`.


* **`splitlines()`**
* **How it works:** Splits a string at line breaks (`\n`, `\r`) and returns a List.
* **Example:** `"line1\nline2".splitlines()` returns `['line1', 'line2']`.


* **`partition(separator)`** & **`rpartition(separator)`**
* **How it works:** Splits the string at the *first* (or last for `rpartition`) occurrence of the separator and returns a Tuple with exactly 3 elements: `(before_sep, sep, after_sep)`.
* **Example:** `"I+love+math".partition("+")` returns `('I', '+', 'love+math')`.
* **When it fails/Gotchas:** If the separator is not found, it returns the whole string as the first item and two empty strings: `("Ilovemath", "", "")`.


* **`join(iterable)`**
* **How it works:** Takes an iterable (like a List) and joins its elements into one single string, using the string you called the method on as the glue.
* **Example:** `"-".join(["a", "b", "c"])` returns `"a-b-c"`.
* **When it fails/Gotchas:** It will throw a `TypeError` if the iterable contains non-string elements (like integers).



---

## 5. Formatting and Translation Methods

* **`format()`** & **`format_map()`**
* **How it works:** Injects values into string placeholders `{}`. `format_map()` takes a single dictionary instead of individual arguments.
* **Example:** `"My name is {name}".format(name="John")` returns `"My name is John"`.
* **When it fails/Gotchas:** Throws a `KeyError` or `IndexError` if you have `{}` placeholders that you forget to provide values for.


* **`maketrans(x, y)`** & **`translate(table)`**
* **How it works:** Used together. `maketrans` creates a mapping dictionary mapping character `x` to character `y`. `translate` applies that dictionary to the string.
* **Example:** ```python
table = str.maketrans("aeiou", "12345")
"hello".translate(table) # Returns "h2ll4"
```

```


* **When it fails/Gotchas:** `maketrans` will throw a `ValueError` if the two strings provided to it are not the exact same length.


* **`encode(encoding)`**
* **How it works:** Converts a string (which is text) into a `bytes` object (raw computer data), usually using "utf-8".
* **Example:** `"hello".encode("utf-8")` returns `b'hello'`.
* **When it fails/Gotchas:** Can throw a `UnicodeEncodeError` if the string contains a character that the target encoding format doesn't understand.



---

## 6. Validation Methods (The `is...` Methods)

*All of these methods return either `True` or `False`. They all return `False` if the string is completely empty `""`.*

* **`isalnum()`:** `True` if all characters are letters OR numbers. Fails if there are spaces or punctuation.
* **`isalpha()`:** `True` if all characters are letters (A-Z). Fails on numbers or spaces.
* **`isascii()`:** `True` if all characters are standard ASCII (values 0-127). Fails on emojis or special foreign characters.
* **`isdecimal()`:** `True` if all characters are standard numbers (0-9).
* **`isdigit()`:** `True` for 0-9, but also allows superscript digits like `²` or `³`.
* **`isnumeric()`:** `True` for 0-9, superscripts, AND fraction characters like `½` or Roman numerals.
* **`isidentifier()`:** `True` if the string is a valid Python variable name (contains only letters, numbers, underscores, and does not start with a number).
* **`islower()` / `isupper()`:** `True` if all cased characters are lower/upper. Ignores numbers/symbols.
* **`isprintable()`:** `True` if the string contains no hidden control characters. Fails on things like `\n` (newline) or `\t` (tab).
* **`isspace()`:** `True` if the string is *entirely* made of whitespace (spaces, tabs, newlines). Fails if even one letter/number is present.
* **`istitle()`:** `True` if every word starts with an uppercase letter and the rest are lowercase. Fails if any word breaks the rule.


## 7. Python String Concatenation: A Complete Guide

**String concatenation** is the process of joining two or more strings together end-to-end to form a single, new string.

Because strings in Python are **immutable** (unchangeable), concatenating strings never modifies the original strings. Instead, it asks the Python interpreter to allocate new memory and create a brand-new string that contains the combined text.

Here are the different ways to concatenate strings in Python, how they work, and when to use them.

---

### 1. The `+` Operator (Standard Concatenation)

The most common and intuitive way to join strings is by using the `+` addition operator.

```python
word1 = "Hello"
word2 = "World"

# Joining strings directly
combined = word1 + word2
print(combined)  # Output: HelloWorld

# Adding a space between them
spaced_combined = word1 + " " + word2
print(spaced_combined)  # Output: Hello World

```

#### ⚠️ The Type Trap

You **cannot** use the `+` operator to combine a string with a non-string data type (like an integer). Python does not implicitly guess that you want the number to become text.

```python
age = 20
# print("I am " + age + " years old.")  # Throws TypeError!

# You must cast the integer to a string first:
print("I am " + str(age) + " years old.") 

```

---

### 2. The `*` Operator (String Repetition)

You can concatenate a string to *itself* multiple times using the `*` multiplication operator.

```python
cheer = "Hip "
print(cheer * 3 + "Hooray!") 
# Output: Hip Hip Hip Hooray!

# Useful for creating visual dividers in terminal outputs
print("-" * 25)
# Output: -------------------------

```

---

### 3. Implicit Literal Concatenation

If you place two string **literals** (raw text in quotes) next to each other with nothing but spaces or newlines between them, Python's parser will automatically glue them together before the code even runs.

```python
# Useful for breaking up very long lines of text
long_message = (
    "This is a very long sentence that we want to break "
    "across multiple lines in our code editor so it is "
    "easier to read without scrolling."
)

print(long_message)

```

*Note: This **only** works with literals. You cannot place a variable next to a literal without a `+` operator.*

---

### 4. The `.join()` Method (For Collections)

If you have a list, tuple, or any iterable full of strings that you want to glue together, using the `+` operator in a `for` loop is incredibly inefficient. Instead, use the `.join()` string method.

You call `.join()` on the string you want to use as the **separator** (the glue), and pass the list of strings as the argument.

```python
words = ["Python", "is", "awesome"]

# Join with a space
print(" ".join(words)) 
# Output: Python is awesome

# Join with a comma
print(", ".join(words)) 
# Output: Python, is, awesome

# Join with nothing
print("".join(words)) 
# Output: Pythonisawesome

```

> **Deep Dive: Why is `.join()` faster than `+=`?**
> If you loop through a list of 10,000 words using `string += word`, Python has to create 10,000 brand-new strings in RAM, destroying the old one each time. This causes massive memory overhead.
> `.join()` calculates exactly how much memory the final string will need *before* it builds it, allocates that RAM exactly once, and writes the text directly into it.

---

### 5. f-Strings (The Modern Alternative to `+`)

Since Python 3.6, the preferred way to concatenate variables, numbers, and text together is by using **f-strings** (formatted string literals).

Instead of dealing with messy `+` signs, quote management, and manual `str()` casting, you prefix the string with an `f` and put your variables inside curly braces `{}`.

```python
name = "Alice"
score = 95.5

# The old, messy way:
# result = "User " + name + " achieved a score of " + str(score) + "!"

# The modern f-string way:
result = f"User {name} achieved a score of {score}!"

print(result)
# Output: User Alice achieved a score of 95.5!

```

Here is a comprehensive Markdown guide explaining the different ways to use f-strings in Python. You can copy and paste this directly into a `.md` file to add to your Python Crash Course notes.

---

## 8. Python f-strings

Introduced in Python 3.6, **f-strings** (formatted string literals) completely revolutionized how developers format text. They are faster, more readable, and less prone to errors than older methods like `%`-formatting or `.format()`.

To create an f-string, simply prefix your string with an `f` or `F` and place your variables or expressions inside curly braces `{}`.

---

### 1. Basic Variable Interpolation

The most common use case. You just drop the variable name straight into the braces.

```python
name = "Surya"
role = "Developer"

print(f"My name is {name} and I am a {role}.")
# Output: My name is Surya and I am a Developer.

```

### 2. Inline Math and Expressions

You don't need to calculate variables beforehand. F-strings can evaluate math and logical expressions directly inside the braces.

```python
x = 10
y = 5

print(f"Ten plus five is {x + y}.")
# Output: Ten plus five is 15.

print(f"Is x greater than y? {x > y}")
# Output: Is x greater than y? True

```

### 3. Calling Functions and Methods

You can call string methods, custom functions, or built-in functions directly inside an f-string.

```python
message = "hello world"

print(f"Loud message: {message.upper()}")
# Output: Loud message: HELLO WORLD

def double(num):
    return num * 2

print(f"Double of 21 is {double(21)}.")
# Output: Double of 21 is 42.

```

### 4. The Debugging `=` Feature (Python 3.8+)

If you add an `=` sign after your variable inside the braces, Python will print the variable name *and* its value. This is a massive time-saver for debugging.

```python
user_id = 404
status = "Not Found"

# Instead of writing: f"user_id={user_id}, status={status}"
print(f"{user_id=}, {status=}")
# Output: user_id=404, status='Not Found'

```

### 5. Number Formatting

F-strings have a built-in mini-language for formatting numbers. You access it by adding a colon `:` after your variable.

**Decimal Places (`.nf`)**

```python
pi = 3.14159265
print(f"Pi rounded to two decimal places: {pi:.2f}")
# Output: Pi rounded to two decimal places: 3.14

```

**Comma Separators (for large numbers)**

```python
money = 1000000000
print(f"I have ${money:,}")
# Output: I have $1,000,000,000

```

**Percentages (`%`)**

```python
success_rate = 0.875
print(f"Success Rate: {success_rate:.1%}")
# Output: Success Rate: 87.5%

```

### 6. Padding and Alignment

You can format strings into neat columns by using alignment operators:

* `<` (Left align)
* `>` (Right align)
* `^` (Center align)

```python
word = "Test"

print(f"|{word:<10}|")  # Left align within 10 spaces
# Output: |Test      |

print(f"|{word:>10}|")  # Right align within 10 spaces
# Output: |      Test|

print(f"|{word:^10}|")  # Center align within 10 spaces
# Output: |   Test   |

print(f"|{word:_^10}|") # Center align, fill empty space with underscores
# Output: |___Test___|

```

### 7. Formatting Dates and Times

If you pass a `datetime` object into an f-string, you can use standard strftime format codes directly after the colon.

```python
import datetime
now = datetime.datetime.now()

print(f"Today is {now:%B %d, %Y}.")
# Output: Today is June 24, 2026. (Output depends on current date)

print(f"The time is {now:%H:%M}.")
# Output: The time is 12:33.

```

### 8. Multiline f-strings

If you need to format a large block of text, you can use triple quotes `"""` combined with the `f` prefix.

```python
name = "Surya"
os = "Arch Linux"

profile = f"""
--- USER PROFILE ---
Name: {name}
OS:   {os}
--------------------
"""
print(profile)

```

*(Alternatively, you can put an `f` in front of multiple standard strings wrapped in parentheses).*

### 9. Escaping Curly Braces

Because `{}` are special characters in f-strings, if you actually want to print literal curly braces (like when writing JSON or CSS inside Python), you just double them up `{{ }}`.

```python
value = 42
print(f"We use {{}} to format variables, like this: {{{value}}}")
# Output: We use {} to format variables, like this: {42}

```