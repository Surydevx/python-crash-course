# Tutorial 7 (Part 2)

Welcome to Part 2 of the Object-Oriented Programming (OOP) deep dive. In this section, we continue exploring Inheritance, the power of `super()`, and a concept called Composition (using instances as attributes).

## 1. Inheritance and the `super()` Function

To truly understand why `super()` is so useful, let's look at what happens when you *don't* use it versus when you do.

### The Parent Class

```python
class StandardCoffee:
    """The Parent Class. Knows how to make a basic black coffee."""
    
    def __init__(self, size):
        self.size = size

    def make_drink(self):
        print(f"--- Starting a {self.size} order ---")
        print("1. Grinding fresh coffee beans...")
        print("2. Brewing the espresso shot...")

```

### The "Bad" Way (Without `super()`)

If we override the parent method completely, we have to manually re-type all the steps. This is bad practice and leads to redundant code.

```python
class BadMocha(StandardCoffee):
    """The Child Class WITHOUT super()."""
    
    def make_drink(self):
        print(f"--- Starting a {self.size} Mocha order ---")
        print("1. Grinding fresh coffee beans...") # ❌ Repeated code
        print("2. Brewing the espresso shot...")   # ❌ Repeated code
        print("3. Adding rich chocolate syrup...") # ✅ The only new step!
        print("4. Pouring steamed milk...\n")

```

### The "Good" Way (With `super()`)

Whenever we invoke the `super()` function inside a child class, our intent is to be efficient (or lazy!). It fetches the definition from the parent class, runs that code, and then lets us add our new functionality on top.

```python
class GoodMocha(StandardCoffee):
    """The Child Class WITH super()."""
    
    def make_drink(self):
        # 1. Call the Parent on the hotline.
        super().make_drink()

        # 2. The Parent is done. Now we add our Mocha-specific steps.
        print("3. Adding rich chocolate syrup...")
        print("4. Pouring steamed milk...\n")

```

## 2. The `__init__()` Method in Child Classes

You might notice that some child classes don't have an `__init__()` function.

* **If you aren't declaring any new attributes:** You don't need a separate `__init__()` function. Python will automatically fetch it from the parent class.
* **If you *are* declaring new attributes:** You must define an `__init__()` function in the child class, use `super()` to handle the parent's attributes, and then define your new ones.

```python
class ElectricCar(Car): # Assuming 'Car' is our parent class
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        # 1. Initialize attributes of the parent class
        super().__init__(make, model, year)
        
        # 2. Initialize attributes specific to this child class
        self.battery_size = 40

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.describe_battery()

```

## 3. Instances as Attributes (Composition)

What if you realize that your class is getting too massive, and a piece of it could actually be its own class? This technique is called **Composition**. It saves lines of code and reduces redundancy (just like composition of functions in math).

Let's pull the battery logic out of `ElectricCar` and into its own `Battery` class.

```python
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car): # Assuming 'Car' is our parent class
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        
        # We instantiate a Battery object and store it as an attribute!
        self.battery = Battery() 

# Using the composed classes
my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.describe_battery()

```

### Breaking Down the "Onion Peeling" Concept

How does `my_leaf.battery.describe_battery()` actually work under the hood?

1. Look at `self.battery = Battery()`. We are creating a new key named `battery` inside the `__dict__` of the `ElectricCar` object.
2. The *value* assigned to that key is a brand-new object instantiated from the `Battery` class.
3. So, the structure in RAM looks something like: `{'battery': <Battery object>}`.
4. When we call `my_leaf.battery.describe_battery()`, we are peeling the onion layer by layer:

* `my_leaf` (Access the ElectricCar object)
* `.battery` (Access the Battery object stored inside it)
* `.describe_battery()` (Call the method belonging to that Battery object)

## 4. Importing Classes

Just like importing functions, you can import classes from other Python files (modules) to keep your main script clean.

* Put the module file in the same directory as your main file.
* Use `from module_name import ClassName`.
* *Don't forget to use docstrings at the top of your module files!*

You can import a single class, multiple classes, an entire module, or even a module into another module. Python allows you to manage your code architecture however you see fit.
