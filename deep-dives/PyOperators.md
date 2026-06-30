## Arithmetic Operators

---

## 1. The Basic Operators

### Addition (`+`)
The addition operator adds two operands together. In many programming languages, if the operands are strings instead of numbers, this operator performs *concatenation* (joining them together).

* **Mathematical Formula:** `A + B`
* **Example:**

```python
  result = 5 + 3  # result is 8
```

### Subtraction (`-`)

The subtraction operator subtracts the right operand from the left operand. It can also be used as a unary operator to indicate a negative number (e.g., `-5`).

* **Mathematical Formula:** `A - B`
* **Example:**
```python
result = 10 - 4  # result is 6
```


### Multiplication (`*`)

The multiplication operator multiplies two operands. In programming, the asterisk (`*`) is universally used instead of the traditional `x` to avoid confusion with variables.

* **Mathematical Formula:** `A * B`
* **Example:**
```python
result = 7 * 6  # result is 42
```

### Division (`/`)

The division operator divides the left operand (dividend) by the right operand (divisor).
*Note: In some strictly typed languages (like C or Java), dividing two integers might automatically drop the decimal. However, in modern languages like Python or JavaScript, standard division always results in a floating-point number (a decimal).*

* **Mathematical Formula:** `A / B`
* **Example:**
```python
result = 20 / 4  # result is 5.0
result = 5 / 2   # result is 2.5
```
---

## 2. Specialized Arithmetic Operators

### Modulo / Remainder (`%`)

The modulo operator divides the left operand by the right operand, but instead of returning the quotient, it **returns the remainder**. This is exceptionally useful in programming for determining if a number is even or odd, keeping numbers within a certain bounds (like a clock face), or parsing data.

* **Mathematical Concept:** Remainder of `A / B`
* **Example:**

```python
result = 10 % 3  # result is 1 (because 10 divided by 3 is 9, with 1 left over)
is_even = 14 % 2 # result is 0 (no remainder means it's an even number)
```



### Exponentiation (`**`)

The exponentiation operator raises the left operand (base) to the power of the right operand (exponent).

* **Mathematical Concept:** `A**B` (A to the power of B)
* **Example:**
```python
result = 2 ** 3  # result is 8 (2 * 2 * 2)
```

### Floor Division / Integer Division (`//`)

Floor division divides the two operands and then automatically rounds the result *down* to the nearest whole integer. It effectively chops off the decimal portion.

* **Mathematical Concept:** `⌊A / B⌋`
* **Example:**
```python
result = 10 // 3  # result is 3 (10 / 3 is 3.333..., rounded down to 3)
result = 15 // 4  # result is 3 (15 / 4 is 3.75, rounded down to 3)
```
---

## Python Assignment Operators

Assignment operators are used to assign values to variables in Python.

## List of Assignment Operators

Here is a complete list of Python assignment operators, showing how they are used and what they are equivalent to:

| Operator | Example | Same As | Description |
| :--- | :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` | Assigns a value to a variable. |
| `+=` | `x += 3` | `x = x + 3` | Adds and assigns. |
| `-=` | `x -= 3` | `x = x - 3` | Subtracts and assigns. |
| `*=` | `x *= 3` | `x = x * 3` | Multiplies and assigns. |
| `/=` | `x /= 3` | `x = x / 3` | Divides and assigns. |
| `%=` | `x %= 3` | `x = x % 3` | Calculates the modulus and assigns. |
| `//=` | `x //= 3` | `x = x // 3` | Calculates the floor division and assigns. |
| `**=` | `x **= 3` | `x = x ** 3` | Calculates the exponentiation and assigns. |
| `&=` | `x &= 3` | `x = x & 3` | Performs Bitwise AND and assigns. |
| `\|=` | `x \|= 3` | `x = x \| 3` | Performs Bitwise OR and assigns. |
| `^=` | `x ^= 3` | `x = x ^ 3` | Performs Bitwise XOR and assigns. |
| `>>=` | `x >>= 3` | `x = x >> 3` | Performs Bitwise right shift and assigns. |
| `<<=` | `x <<= 3` | `x = x << 3` | Performs Bitwise left shift and assigns. |

---

## The Walrus Operator (`:=`)

Introduced in Python 3.8, the `:=` operator is officially known as the **assignment expression**, but is commonly called the **walrus operator** because it resembles the eyes and tusks of a walrus on its side. 

It allows you to assign a value to a variable as part of a larger expression.

### Example:

| Operator | Example | Same As |
| :--- | :--- | :--- |
| `:=` | `print(x := 3)` | `x = 3`<br>`print(x)` |

**Why is it useful?**
It helps you avoid writing the same expression twice, often making loops and `if` statements much cleaner.

```python
# Without the walrus operator
word = "Hello"
n = len(word)
if n > 3:
    print(f"The word has {n} letters.")

# With the walrus operator
word = "Hello"
if (n := len(word)) > 3:
    print(f"The word has {n} letters.")

> note - Summary of the rule
Use = when you just need to store a value for later.
Use := when you need to store a value and immediately feed that value into an if statement, while loop, or list comprehension on the exact same line.