# Tutorial 7 (Object-Oriented Programming)

Welcome to the deep trenches! We are moving towards the end of syntax learning and covering Object-Oriented Programming (OOP).

Making an object from a class is called **instantiation**, and you work with **instances** of a class. Let's start without further delay.

## 1. Creating and Using a Class

A class is essentially a blueprint. Functions defined under a class are called **methods**; they behave exactly like normal functions, but they are attached to a specific class and its objects.

```python
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Instantiating an object
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Accessing methods
my_dog.sit()

```

*(Note: By convention, class names are written in PascalCase—capitalizing the first letter of each word.)*

### The `__init__()` Method and `self`

Whenever you instantiate an object from a class, Python automatically runs the `__init__()` method under the hood.

* `self` **must** be the first parameter in your class methods.
* When you create the object (e.g., `Dog('Willie', 6)`), you do *not* pass an argument for `self`. Python handles this automatically.

---

## 2. Deep Dive: The Lifecycle of Object Creation

What is actually happening in RAM when you write `self.name = name`?

1. **`__new__()` Allocation:** When an object is created, the hidden dunder method `__new__()` asks the operating system for memory in RAM for a new object. It allocates that memory and returns a pointer (reference) to that address.
2. **Passing the Pointer:** This pointer is passed to the `__init__()` method as the argument for the `self` parameter.
3. **The Hidden Dictionary (`__dict__`):** Instead of rigid memory blocks, almost all Python objects have a hidden dictionary named `__dict__` at that memory address.
4. **Dynamic Storage:** When you write `self.name = name`, Python goes to the memory address stored in `self`, accesses the `__dict__` hash map, and creates a new key-value pair (`{'name': 'Willie'}`).

*Essentially, `self.` means: "Access the permanent, hidden dictionary (`__dict__`) attached to this specific object in RAM."*

---

## 3. Working with Classes and Attributes

Instance variables (attributes) define the unique properties of an object. You can set default values for attributes directly in the `__init__()` method without requiring them as parameters.

```python
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Setting a default value for an attribute
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

```

### Modifying Attribute Values

You have two main ways to update an attribute's value:

**1. Modifying Directly:**

```python
my_new_car.odometer_reading = 23

```

**2. Modifying Through a Method:**
You can define a new method inside your class specifically to update the value.

```python
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car.update_odometer(23)

```

---

## 4. Inheritance and `super()`

You don't always have to write a class from scratch. If the class you want to make is a subset of another existing class, you can use **Inheritance** to reduce redundancy.

* **Parent Class:** The original, base class.
* **Child Class:** The new class that inherits attributes and methods from the Parent, but can also define its own unique features.

Imagine building a music app. Every track is a "Song," but some songs have special rules.

```python
# The Parent Class
class Song:
    """Every single track on the app will share these basic features."""
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        print(f"▶️ Playing: '{self.title}' by {self.artist}...")

# A Child Class
class ClassicHindiSong(Song):
    """Inherits the basics, but adds a vintage touch."""
    def __init__(self, title, artist, year):
        # super() grabs the title and artist setup from the Parent.
        super().__init__(title, artist)
        self.year = year # Adding a new attribute specific to classic songs

    def play(self):
        # Method Overriding
        print(f"📻 [Crackling radio static] Playing the {self.year} classic '{self.title}' by {self.artist}...")

# Another Child Class
class KaraokeTrack(Song):
    """Perfect for practicing vocals. Same setup, different play method."""
    def play(self):
        # Method Overriding
        print(f"🎤 Playing the instrumental for '{self.title}'. Your turn to sing!")

# --- Let's see it in action ---

print("--- Standard Song ---")
regular_track = Song("Hasi Ban Gaye", "Ami Mishra")
regular_track.play()

print("\n--- Classic Song ---")
vintage_track = ClassicHindiSong("Ye Raatein Ye Mausam", "Kishore Kumar", 1958)
vintage_track.play()

print("\n--- Karaoke Track ---")
practice_track = KaraokeTrack("Hasi Ban Gaye", "Ami Mishra")
practice_track.play()

```

### Method Overriding vs. `super()`

* **Method Overriding:** Putting a method in the Child class with the *exact same name* as a method in the Parent class. Python always checks the Child class first. If it finds the method there, it intercepts the command and ignores the Parent's version. It replaces the behavior completely.
* **`super()`:** This is a built-in shortcut that temporarily bypasses the override rule. It acts as a direct hotline to the Parent class. It tells Python: *"Go run the Parent's version of this method right now, then come back here so I can finish my specific task."* This allows you to reuse the parent's code without completely overwriting it.
