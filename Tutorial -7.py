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
#by default the name of class is written with capital first letter, maybe what we call as camel casing
#This code is writeen by me on my phone, with termux, and proot-distro environment with fedora, i installed starship and nvim along with lazyvim for lazy coding.:)
#how much overengineering u like? yess!
# back to the topic.
# instance variable vs vlass variable.
# instance variables are variables whoch defines thr unique properties of an object.and on the other hand each object created from an class gets a copy of class variables, what are they? they are variables which are defined outside the  "__init__()" fnction.
# any instance variable under "__init__()" function must be declared using the syntax "self.instance_variable_name"
# Any instance variable is acessible throught all tje functions created under class.
#and instance variables can be accessed by objects and thus are called attributes (man, this makes sense, these variables defines the objects uniqueness so these must be attribites of the object.)
# self.name = name, is kinda sus, i will go deep down this topic.
# the whole lifecycle of object creations. sit back and read.
#Whenever an object is created, the dunder mthod "__new__()" asks the operating system for memory in ram for a new object and  allocates that memory and returns a pointer(reference) to that memory address. This pointer is passed to "__init__()""as a variable named as an argument of parameter named as "self". Writing "self.instance_variable = value"
#Instead of rigid memory blocks almost all python objects have a hidden dictionary named as "__dict()__" on that memory address.
#so whenever we are writing 
# takes that parameter and stores it dynamically inside the object's internal dictionary (__dict__) located at that memory address.
