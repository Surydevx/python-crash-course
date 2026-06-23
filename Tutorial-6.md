# Tutorial 6

This tutorial covers **Functions**: what they are, how to pass arguments to them, returning values, and how they interact with lists in memory.

## 1. What are Functions?

> "A function is a self-contained block of parameterized, reusable code designed to perform a single, specific operation. It encapsulates a sequence of statements, accepts optional input data (arguments) via designated variables (parameters), and optionally yields a computed value back to the caller while terminating its own execution."

Here is what that definition actually means in code:

```python
# Defining a function named "greet_user"
def greet_user():
    """Display a simple greeting."""
    print("Hello!") # This block executes whenever the function is called.

# Calling the function standalone
greet_user() 

```

*Note: The text enclosed in triple quotes `"""` right after the definition is called a **docstring**. Python uses this to generate documentation for your code.*

### Function Names are Just Variables

If you define two functions with the exact same name, the Python interpreter won't crash—it will simply overwrite the first one.

In Python, a function name is just a variable pointing to a block of code in memory. When you use `def` a second time with the same name, you point that variable to a brand new block of code, erasing the connection to the old one.

## 2. Arguments vs. Parameters

* **Parameter:** A variable defined in the function's declaration (it acts as a placeholder for the actual input).
* **Argument:** The actual value you pass into that parameter when you *call* the function.

### How to Pass Arguments

**1. Positional Arguments:** You provide arguments in the exact same order as the parameters were defined. Order matters strictly.

```python
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') 

```

**2. Keyword Arguments:**
This style is more structured and doesn't rely on order. You explicitly assign values to the parameter names in the function call.

```python
describe_pet(animal_type='hamster', pet_name='harry')

```

**3. Default Values:**
You can assign a default fallback value during the function's definition. If the caller provides an argument, it overwrites the default. If they provide nothing, the function uses the default.

```python
# 'level' and 'weapon' have default values
def create_character(name="john doe", role="npc", weapon="none", level="unknown"):
    print(f"Name: {name.title()} | Role: {role.title()} | Weapon: {weapon.title()} | Level: {level}")

# Mixing positional and keyword arguments (positional MUST come first)
create_character('arthur', 'knight', level=25, weapon='excalibur')

# Using the default values entirely
create_character() 

```

*Rule of thumb: Unless there are default values, the number of arguments passed must exactly match the number of parameters required.*

## 3. Return Values (and a Rookie Mistake)

If you want to save the output of a function to a variable, you might intuitively try to just `print` the output inside the function and assign the function call to a variable.

**The Rookie Mistake:**

```python
def some_function():
    print(2+2)

supposed_to_be_4 = some_function()
print(supposed_to_be_4)

# Output:
# 4
# None

```

**Why did it print `None`?** Python processes assignments by evaluating the right side first. It ran the function, saw `print(2+2)`, and blasted `4` to the terminal. But because there was no `return` keyword, the function officially gave back `None` to the variable.

**The Fix: Use `return**`
The `return` statement takes a value from inside a function and sends it back to the line that called it.

```python
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('suryansh', 'sharma')
print(musician) # Outputs: Suryansh Sharma

```

### Engineering Optional Arguments

You can use empty strings or the `None` keyword to make certain parameters optional without breaking the code.

```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    
    # 'None' evaluates to False in a boolean context
    if age: 
        person['age'] = age
        
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

```

## 4. Passing Lists to Functions

Whenever you pass a list to a function as an argument, **the function gets direct access (a reference pointer) to that actual list in memory.** It does *not* create a backup copy. Because of this, any modifications made to the list inside the function are permanent to the original list.

```python
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design and moving it to a completed list."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

# These lists will be permanently modified by the functions
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

```
