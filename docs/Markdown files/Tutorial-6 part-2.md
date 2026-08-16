# Tutorial 6 (Part 2)

This continuation covers more advanced function concepts, including preventing list modification, handling arbitrary arguments, and importing modules.

*Golden Rule: Write and design your functions so that they do exactly one job. Nobody likes spaghetti code!*

## 1. Preventing a Function from Modifying a List

As learned in Part 1, passing a list to a function allows the function to modify the original list permanently. If you want to protect your original list, you can pass a **copy** of it using slice notation `[:]`.

```python
# The [:] makes a copy of the list to send to the function
print_models(unprinted_designs[:], completed_models)

```

**Developer Note:** Even though you *can* do this, you should generally pass the original list unless you have a specific reason not to. Passing copies of large lists eats up time and memory.

## 2. Passing an Arbitrary Number of Arguments (`*args`)

Sometimes you don't know ahead of time how many arguments a user will pass to your function. You can use the `*` operator to tell Python to collect as many arguments as provided and pack them into a **Tuple**.

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Output:
# ('pepperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')

```

*Note: You will often see developers use the generic parameter name `*args` for this.*

### Mixing Positional and Arbitrary Arguments

If your function needs to accept different kinds of arguments, the arbitrary parameter (`*toppings`) must be placed **last** in the function definition. Python matches positional arguments first, then tosses everything else into the tuple.

```python
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

```

## 3. Using Arbitrary Keyword Arguments (`kwargs`)

If you expect extra data from the user but aren't sure exactly what *kind* of data it will be (like a user profile where some people provide ages, others provide locations), you can use the `` operator.

This tells Python to create an empty **Dictionary** to hold all the extra key-value pairs the user provides.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    
    # We add the mandatory positional arguments into the dictionary
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# Output:
# {'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}

```

*Note: You will often see the generic parameter name `kwargs` (keyword arguments) used for this.*

> **Addressing Your Doubt:** Why is the dictionary showing `location` and `field` *before* `first_name` and `last_name`?
> Modern Python *does* remember the order items are added to a dictionary. When you called the function, `location` and `field` were instantly packed into the `**user_info` dictionary. *After* that happened, your code explicitly added `first_name` and `last_name` to that existing dictionary. Since they were added last, they show up at the end!

## 4. Using Modules

A module is just a normal `.py` file. A package is a collection of modules, and a library is a collection of packages. Modules allow you to reuse functions without writing them from scratch every time.

Assume we have a file called `pizza.py` containing our `make_pizza` function. We can import it into a new file, `making_pizzas.py`, located in the same folder.

### Importing an Entire Module

This imports the whole file. You must use dot notation (`module_name.function_name()`) to use its functions.

```python
import pizza

pizza.make_pizza(16, 'pepperoni')

```

### Importing Specific Functions

This imports just the function you need. You no longer need to use dot notation.

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')

```

### Using `as` to Give an Alias

If a function or module name is too long (or conflicts with something else in your code), you can give it a nickname using the `as` keyword.

**Aliasing a Function:**

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')

```

**Aliasing a Module:**

```python
import pizza as p

p.make_pizza(16, 'pepperoni')

```

### Importing All Functions (Be Careful!)

You can import every single function from a module using the `*` operator.

```python
from pizza import *

make_pizza(16, 'pepperoni')

```

**Danger:** Avoid this in production code! If you import a large module this way and it happens to have a function with the exact same name as a function you already wrote, Python will silently overwrite yours, causing massive bugs.

## 5. Styling Conventions for Functions

When specifying a default value for a parameter, or when passing keyword arguments during a function call, **do not** use spaces on either side of the equal sign (`=`).

```python
# CORRECT
def function_name(parameter_0, parameter_1='default_value'):

# CORRECT
function_name(value_0, parameter_1='value')

```
