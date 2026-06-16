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
  # so what we did here is we made an class named "dog", and we used def keyword to define three funtios, "__init__()" , "sit()" and "roll_over()".
  # functions defined under a class are said as methods, they work and bheave exactly the same but they are special to an class and their object.
  # so, important things is whenever we try to instanntiate an object from a class, an under the hood method that python uses is called "__init__()" function, which ahs three parameters, self, name and age  in the above example,  bbut understand that  self must be the first parameter and whenever you will instantiate an object you won't be giving self parameter as argument, reasons is python uses a dunder method also known as double underscore method.