# hello Fellas,
# we  will conitnue our discussion in this  2nd part, had to spllit the tutorioal as it got  too long to actually read adn i wasn't seeing it end anytime  soon.
#we  were learning about inheritance, let's analyse this example bbelow to enhance our undertsanding of the topic .. 
class StandardCoffee:
    """
    The Parent Class.
    This knows how to make a basic black coffee.
    """
    def __init__(self, size):# only one instannce variable named "size"
        self.size = size

    def make_drink(self):
        print(f"--- Starting a {self.size} order ---")#  we accessd the instence variable named "size" here..
        print("1. Grinding fresh coffee beans...")
        print("2. Brewing the espresso shot...")


class BadMocha(StandardCoffee):
    """
    The Child Class WITHOUT super().
    Because we don't use super(), we have to manually re-type 
    all the grinding and brewing steps. This is bad practice!
    """
    def make_drink(self):#   the "make_drink" function is originally defined in the parent class "StanndardCoffee", by providing a brand new definition of the same function,, it was already explained that we can access and manipulate the parent class method in child class. 
        # We overrode the parent, but we are doing all the work ourselves.
        print(f"--- Starting a {self.size} Mocha order ---")
        print("1. Grinding fresh coffee beans...") # ❌ Repeated code
        print("2. Brewing the espresso shot...")   # ❌ Repeated code
        print("3. Adding rich chocolate syrup...") # ✅ The only new step!
        print("4. Pouring steamed milk...\n")

# we will define this child class with super()

class GoodMocha(StandardCoffee):
    """
    The Child Class WITH super().
    We let the Parent do steps 1 and 2, and we only code steps 3 and 4.
    """
    def make_drink(self):
        # 1. Call the Parent on the hotline. 
        # This automatically prints the "Grinding" and "Brewing" steps.
        super().make_drink()
        
        # 2. The Parent is done. Now we add our Mocha-specific steps.
        print("3. Adding rich chocolate syrup...")
        print("4. Pouring steamed milk...\n")


# ==========================================
# Let's run the code and see what happens!
# ==========================================

print("=== ORDER 1: Standard Coffee ===")
my_coffee = StandardCoffee("Medium")
my_coffee.make_drink()
# Output: Grinds and brews.

print("=== ORDER 2: Bad Mocha (No super) ===")
my_bad_mocha = BadMocha("Large")
my_bad_mocha.make_drink()
# Output: Does exactly what we want, but the programmer had to type out 
# the grinding and brewing logic all over again.

print("=== ORDER 3: Good Mocha (Using super) ===")
my_good_mocha = GoodMocha("Large")
my_good_mocha.make_drink()
# Output: Does exactly what we want, but the programmer only had to 
# write the chocolate and milk steps. The Parent handled the rest!

# "super().method_name(arguments)"" this is the exact syntax used to invoke this super function, super is a built in class in python and "super()" a method of that class, listen whenever we invoke super() function inside a child class, what we intend to do is be lazy  that we don't have to write parent's class code again, and if  we use the function name from parent class to add a new functionality, we would have to write all the code  with adding more functionaliity and thus we call super function, which goes to original parent method despite having closest instruction rule, and fetches the earlier definition of function and pastes the code here in child class function (metaphorically atleast.)  and then you can add more code to add some more  functionality....
# but i suspects something, at the end of the day we  are overriding the function, either doing the lazy way by using super() funnction or doing it the redundant way....what do u say?
class Car:
 """A simple attempt to represent a car."""
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

 def update_odometer(self, mileage):
  """Set the odometer reading to the given value."""
  if mileage >= self.odometer_reading:
   self.odometer_reading = mileage
  else:
   print("You can't roll back an odometer!")

 def increment_odometer(self, miles):
  """Add the given amount to the odometer reading."""
  self.odometer_reading += miles

class ElectricCar(Car):
 """Represent aspects of a car, specific to electric vehicles."""
 def __init__(self, make, model, year):
  """Initialize attributes of the parent class."""
  super().__init__(make, model, year)

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
#notice that the examples we used earlier didn't had "__init__()" function at start of the child class but this example does, we will resolve this  doubt in a minute.
# The reason child classes in earlier eamples dind't had "__init__()"  is because if you are'nt declaring any new attribute in the child class then you prolly don't need a seperate function "__init__()" because python will fetch the __init__() function from the parent class if it doesn't find __init__() function in the  child class. but if you want to declare any new attriute which wasn't in parent class but you need it in the child clas, you must define an __init__() function though you can use super() to reduce redundancy in the code.
# we defined another  class  with same name so it woul overwrite the previous class completely.
# and this is how we define a new attribute in child class when we need to.
class ElectricCar(Car):
 """Represent aspects of a car, specific to electric vehicles."""
 def __init__(self, make, model, year):
  """ Initialize attributes of the parent class. Then initialize attributes specific to an electric car. """
  super().__init__(make, model, year)
  self.battery_size = 40

 def describe_battery(self):
  """Print a statement describing the battery size."""
  print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

#Instances as Attributes
# basically what if ? while writing a class you get a sudden stroke of intuition you think that this  class can be written with using some other classes? saves lines of code and improves redundancy, this technique is called composition.(makes sense, we  learned composiition of functions in maths, you didn't ? that's  bad :(.)

#see this brilliant example.
"""
class Car:
 # A simple attempt to represent a car.
 def __init__(self, make, model, year):
  #Initialize attributes to describe a car.
  self.make = make
  self.model = model
  self.year = year
  self.odometer_reading = 0

 def get_descriptive_name(self):
  #Return a neatly formatted descriptive name.
  long_name = f"{self.year} {self.make} {self.model}"
  return long_name.title()

 def read_odometer(self):
  #Print a statement showing the car's mileage.
  print(f"This car has {self.odometer_reading} miles on it.")

 def update_odometer(self, mileage):
  #Set the odometer reading to the given value.
  if mileage >= self.odometer_reading:
   self.odometer_reading = mileage
  else:
   print("You can't roll back an odometer!")

 def increment_odometer(self, miles):
  #Add the given amount to the odometer reading.
  self.odometer_reading += miles

class Battery:
 #A simple attempt to model a battery for an electric car.

 def __init__(self, battery_size=40):
  #Initialize the battery's attributes.
  self.battery_size = battery_size

  def describe_battery(self):
   #Print a statement describing the battery size.
   print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
 #Represent aspects of a car, specific to electric vehicles.

 def __init__(self, make, model, year):
  #Initialize attributes of the parent class. Then initialize attributes specific to an electric car.#
  super().__init__(make, model, year)
  self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

"""
# Notice two lines in code, everything else is reproduceable and disposable, line 183 and line 179, understand the key of understanding composition, notice on line 179 you have "self.battery = Battery()" what does this mean is assign the key = battery and value is from the "Battery()", and store this in __dict__  of an object created by the class "ElectricCar". what is "Battery()" ? look at line 162, Battery is a class. and here the value is "Battery()" that is oject of class "Battery", but without any parameter, the class "Battery" needs  one parameter at defining an object from it, but it was given means? the structure of __dict__ in object of class "ElectricCar",  is like this {'battery'=object_created_from_class_Battery} and since no paramater was passed in line of code 179, only self was passed automatically,but i would like you to notice that on the line 165,  the parameter we defined was a default parameter so it wasn't a necessary paramater. but when did we createed object from class "Battery", ? haha, see line 179 closely,  we actually created that object right then and there and stored that value under variabled name "battery".
# look at line 181 and 183, we created an object named "my_leaf" from class "ElectricCar" and then on line 183 we accessed attribute 'battery' of the object "my_leaf" created from class "ElectricCar" and battery attribute  has a value stored as object of the class "Battery", and  that object of Battery has an method named "describe_battery", kind of like onion we just peeling layer by layer and giving the reference of first layer to the second and second to the third.
# remember whenever we call a method from an object we use the syntax "object_name.methodname()" yep parethesis are necessary. and to call an attribute we use the syntax "object_name.attribute_name"
# i explained the above example well upto my level of coginitive ability, any more is i expect that you should try to learn from yourself as i am not capable of going more beyond than this at this time, and anyone below my cognitive ability, i made sure that you could read code,if you followed uptil now you shouldn't have much problems, yet. spoon feeding is what i dislike.
