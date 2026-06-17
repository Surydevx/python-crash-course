# hello Fellas,
# we would be covering OOP's in this tutorial.
# we are moving towards end of syntax learning.
#Making an object from a class is called instantiation, and you work with instances of a class.
# let's start without further delay.
## Creating and Using a Class
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

# so what we did here is we made an class named "dog", and we used def keyword to define three functions which are technnically called as methods, "__init__()" , "sit()" and "roll_over()".
# functions defined under a class are said as methods, they work and bheave exactly the same but they are special to an class and their object.
# so, important things is whenever we try to instanntiate an object from a class, an under the hood method that python uses is called "__init__()" function, which ahs three parameters, self, name and age  in the above example,  bbut understand that  self must be the first parameter and whenever you will instantiate an object you won't be giving self parameter as argument, reasons is python uses a dunder method also known as double underscore method.
#by default the name of class is written with capital first letter, maybe what we call as pascalcase
#This code is writeen by me on my phone, with termux, and proot-distro environment with fedora, i installed starship and nvim along with lazyvim for lazy coding.:)
#how much overengineering u like? yess!
# back to the topic.
# instance variable vs vlass variable.

# instance variables are variables whoch defines thr unique properties of an object.and on the other hand each object created from an class gets a copy of class variables, what are they? they are variables which are defined outside the  "__init__()" method.

# any instance variable under "__init__()" function must be declared using the syntax "self.instance_variable_name"

# Any instance variable is acessible throught all the functions created under class.

#and instance variables can be accessed by objects and thus are called attributes (man, this makes sense, these variables defines the objects uniqueness so these must be attribites of the object.)

# self.name = name, is kinda sus, i will go deep down this topic.
# the whole lifecycle of object creations. sit back and read.

#Whenever an object is created, the dunder mthod "__new__()" asks the operating system for memory in ram for a new object and  allocates that memory and returns a pointer(reference) to that memory address. This pointer is passed to "__init__()""as a variable named as an argument of parameter named as "self". Writing "self.instance_variable = value"
#Instead of rigid memory blocks almost all python objects have a hidden dictionary named as "__dict__" on that memory address.

#so whenever we are writing "self.name=name" what are we doing is it goes to the memory address reference stored in self, and accesses the  __dict__ hash map at that address and then it creates new key-value pair inside this dictionary, notice that in right side "name" is parameter and whenever an argument is passed for object creating then this argument value is assigned to the variable "self.name"(specifically, the variable_name will be written with self)

#Essentially, self.balance = 100 translates internally to: self.__dict__['balance'] = 100,(we can notice that this key value pair is "instance_variable"= 100).

# takes that parameter and stores it dynamically inside the object's internal dictionary (__dict__) located at that memory address.

# I must look into __dict__, for now  we continue  with the rest of the topic.

#object creation..
# "object_name = class_name(argument-1, argument-2)"
# whenever we create an object, the arguments passed for instance variables are stored in __dict__ of that  object in key-value pair format. under the memory issued by __new___ method.
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# to access the attributes use the syntax  "object_name.atrribute_name", (remember we were using this all along....haha). and to access the methods of an object. use syntax "object_name.method_name(some_argument_if required)".
# as understandable we can create as  many objects froma class we wannt.
# "self. means: "Access the permanent, hidden dictionary (__dict__) attached to the specific object in RAM.""
# i kinda realised that every method defined in a class must have atleast first parameter named as self, why so ? i am not  sure rn either.

# working with classes and instances.
class Car:
 """A simple attempt to represent a car."""
 def __init__(self, make, model, year):
  """Initialize attributes to describe a car."""
  self.make = make
  self.model = model
  self.year = year
 def get_descriptive_name(self):
  """Return a neatly formatted descriptive name."""
  long_name = f"{self.year} {self.make} {self.model}"
  return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
# output- "2024 audi a4".

# Setting a Default Value for an Attribute
#When an object is created, attributes(simply means variables) can be defined without being passed in as parameters. These attributes can be defined in the __init__() method, where they are assigned a default valuue, example?
class Car:

 def __init__(self, make, model, year):
  """Initialize attributes to describe a car."""
  self.make = make
  self.model = model
  self.year = year
  self.odometer_reading = 0
 def get_descriptive_name(self):
  """Return a neatly formatted descriptive name."""
  long_name = f"{self.year} {self.make} {self.model}"
  return long_name.title()

 def read_odometer(self):
  """Print a statement showing the car's mileage."""
  print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# to define an attribute with default value, don't assign it as a parameter in the __init()__ method, instead define it under __init__() method's code block with default value just as how we did it on line 91.
# btw notice that above code snippet has a function named as "get_descriptive_name(self)" and it's return output is defined with return "keyword" and it's return value is "long_name.title()" and "long_name" itself is an variable of the function. if you don't know retrun keyword is used to define that what function will retrun to variiables or whenn print it....like basicallly what output it will give.
# Modifying Attribute Values
# We have three methods to modfy attribute values.
# Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# you just update that attribute value with a new value overwriting previous value.
# general syntax would be, "my_object.attribute_name = some_new_modified_value" keep in mind that, since this only focuses on the name of function inside a class...you can not prolly create two functions with same name under one class.

# Modifying an Attribute’s Value Through a Method
"""
def update_odometer(self, mileage):
 # Set the odometer reading to the given value.
 self.odometer_reading = mileage
"""
# my_new_car.update_odometer(23) this updates the odometer_reading attribute.
# this is how you define one more method under definition of class.  so that you can access this method  later to modify value of an attribute, in line 118, you access the attribute "odometer_reading" using self parameter meaning accessing the specific __dict__ data of the object.
# question? does if i create a 1000, objects from a class, all will try to ceate their own __dict__ hidden data, and since it is memory hungry. my ram would be fillled in no time, cuz to define objects you must define attributes  (or you can say instance variables.)
# my mental map of class is that to instantiate an object from a class you must define core instance variables, or otherwise the meaning object is invalid. and whenever accessing the instance variables we use the syntax "self.attribute_name=some_parameter_name or some_value", understand that this syntax must be followed everytime we use instance  variables under all methods in class definitiion. due to  a very specific reason is python doesn't know where the specific objects attributes in ram are? since at times there can be  many objects in memory. to locatinbg specific attribute of on object.

# INHERITANCE
# we are in deep trenches with this topic.
# we don't have to write a class from scratch always, if we undersand that the class we wannt to make is a subset of another class already defined. we can use that class to save up space and reduce redundancy.
# the original class is called parent class and the class which will inherit the parent class is called child class(pretty straighhtforward naming)
# The child class can inherit any or all of the attributes and methods of its parent class, but it’s also free to define new attributes and methods of its own.
# Imagine we are building a music app or setting up a karaoke session. Every track on your app is a "Song," but some songs have special rules. Inheritance lets us set up the basic rules for all songs once, and then tweak them for specific types of tracks.
# The parent class is defined as "Song"
class Song:
    """
    The Parent Class. 
    Every single track on the app will share these basic features.
    """
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        # The standard way to play a song
        print(f"▶️ Playing: '{self.title}' by {self.artist}...")

# the child class "ClassicHindiSong" and we will pass the name of parent class in parenthesis follwing the name of child class.
class ClassicHindiSong(Song):
    """
    A Child Class. 
    Inherits the basics, but adds a vintage touch.
    """
    def __init__(self, title, artist, year):
        # super() automatically grabs the title and artist setup from the Parent.
        # We don't have to rewrite that code!
        super().__init__(title, artist)
        self.year = year # Adding a new attribute called "year", specific feature just for classic songs.

    def play(self):
        # We override the original play method to give it a vintage vibe
        print(f"📻 [Crackling radio static] Playing the {self.year} classic '{self.title}' by {self.artist}...")

# another child class named "KaraokeTrack" with passing parent class "Song" in parenthesis following the name of class we are defining.
# man, i assumed you would know about karaoke...it just means sinnging w/o vocals, and you would be singing over original instrumental music.
class KaraokeTrack(Song):
    """
    Another Child Class. 
    Perfect for practicing vocals. It uses the exact same setup as 'Song', 
    but changes how it plays.
    """
    def play(self):
        # Overriding the play method again—no lead vocals this time!
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
# function(method) over-riding in child class.

# calling a method of a class, it is to be understood that python checks the deffinition of that method in a very specific order, it first checks the child class for the definition, and if it not found, it will go and check the parent class fro the definition of the method you called and we can use this behaviour to override a function
# Overriding is simply the act of putting a method in the Child class that has the exact same name as a method in the Parent class. Because Python always checks the Child first, it intercepts the command. The Child is effectively saying to the Parent, "I know you have a way of doing this, but I'll take it from here."
# what is "super()"????
#In short: * Overriding is a complete replacement of a behavior.super() is a delegation. It asks the parent to run its version of the code before (or after) the child runs its own unique steps.
# super() is a built-in shortcut that temporarily bypasses the "Closest Instruction" rule (this is exactly whatt we just talked about a few lines ago in function overriding). It acts as a direct hotline to the Parent class. It means: "Go run the Parent's version of this method right now, then come back here so I can finish my specific task.
# why use super(), cuz it basicallly allows us to reuse  the parent  class code without completely overwriting the when a new functionality is needed.