# This is Tutorial 6 part 2.
# The first part got a lot lengthy and i wasn't seeing it ending anytime soon so splitted this tutorial into two parts.
# okay? one more tip is write and design your functions so that they are doing exactly one job, you wouldn't want a spaghetti code, would you?
# preventing a functtion from modifying a list.
# very simple logic, function will change the list and if you don't want that your oriiginal list get changed just pass a copy of the original list as an argument to function.? simple! syntax - "function_name(list_name[:])",the slice notation [:] makes a copy of the list to send to the function
"""
print_models(unprinted_designs[:], completed_models)
"""
#Even though we can preserve the contents of a list by passing a copy of it to functions, we should pass the original list to functions unless we have a specific reason to pass a copy. It’s more efficient for a function to work with an existing list, because this avoids using the time and memory needed to make a separate copy. This is especially true when working with large lists.
# you would notice that as we proceed further just the complexity of code increases and concepts are just those basic ones we already learned.
# Passing an Arbitrary Number of Arguments
# why do we need this? sometimes  we don't know ahead of time how much arguments of a function we would need..? and thus we need this concept. see  example.

#consider a function that builds a pizza. It needs to accept a number of toppings, but we can’t know ahead of time how many toppings a person would choose. The function in the following example has one parameter, "*toppings", but this parameter collects as many arguments as the calling line provides:
def make_pizza(*toppings):
 """Print the list of toppings that have been requested."""
 print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#  what does this * operator does? basically whenever we define a prameter of a function using "*parameter_name" the function would create a tuple and of name "paramater_name",and tuple recieves all the values we gave,
# outputs of code above-
"""
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
"""
# notice how  even if we provide on argument, it would be stored in a tuple now.
# coming to think of it we can use loops to print each member of the tuple precisely.
# only natural condition we can ponder rn is..
# Mixing Positional and Arbitrary Arguments
# If we want that a function accepts several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.
# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.
def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print(f"\nMaking a {size}-inch pizza with the following toppings:")
 for topping in toppings:
  print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#output-
"""
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
"""
#we will often see the generic parameter name *args, which collects arbitrary positional arguments.

# Using Arbitrary Keyword Arguments

# same idea as above but we will use dictionary instead of tuple.
#use case of this? if you expect some kind of data from your programme but not sure exactly what kind of data would be passed ahead of time? in that case we provide a way for user to pass to as many key-value pair as they want..
# we are seeing this example  where we would let user add as much as info about them as they want..

def build_profile(first, last, **user_info):
 """Build a dictionary containing everything we know about a user."""

 user_info['first_name'] = first
 user_info['last_name'] = last
 return user_info

user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)
# ouput- 
"""
{'location': 'princeton', 'field': 'physics',
'first_name': 'albert', 'last_name': 'einstein'}
"""
# my doubt why the  dictionary isn't showing the data in the order we gave the passed the argument to function.

# "**user_info" generate a dictionary named as "user_info" whichh will contain any extra information given by user.
#we  will often see the parameter name "**kwargs" used to collect nonspecific keyword arguments.

# using modules.
# A module is a normal ".py" file we write, a package is a collection of modules. and a library is a collection of packages.
#we can use these  modules writtenn to use the functions written in them to reuse in our code w/o wriing everythimg from scratch by ourselves.
# let's assume we write  a file called pizza.py
"""
def make_pizza(size, *toppings):
    
\"""Summarize the pizza we are about to make\"""

 print(f"\nMaking a {size}-inch pizza with the following toppings:")
 for topping in toppings:
  print(f"- {topping}")
"""
# let's use a seperate file..named as "making_pizzas.py" in the same directory(can call it folder) as the pizza.py
"""
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
# yes, we imported the module and used the function of module named pizza and passed the argument in function directly, what is "pizza.make_pizza()" since "make_pizza()" is a method of "pizza" module,  we can use the function from an imprted library like this..
# When Python reads the code in file "making_pizzas.py", the line import pizza tells Python to open the file pizza.py and copy all the functions from it into this ""making_pizzas.py"" programme.
# if we used this approach to import whole module "import module", all of it's functions gets imported to the current programme and we can use  all of it's function using "module_name.function_name()" this syntax.

# Importing Specific Functions
# yes, we can also do this, using the syntax "from module_name import function_name" and we can also import multiple functions from the same module using syntax "from module_name import function_0, function_1, function_2", when we use this  appproach to import function we can directly use the function name to pass the argument no need to use the dot operator.
# Using as to Give a Function an Alias
#If the name of a function we’re importing might conflict with an existing name in our program, or if the function name is long, you can use a short, unique alias (an alternate name similar to a nickname) for the function. we’ll give the function this special nickname when you import the function.
# see example.
"""
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
# the general syntax to give an allias is "from module_name import function_name as fn"

# Using as to Give a Module an Alias
# we can give module an alias too.
#see the code
"""
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
#general syntax for aliasing module name "import module_name as mn"
# the reason to give alias to an module is because when we we use "pizza.make_pizza()" and when we use "p.make_pizza()", the second one seems better for lazy ppls like me.
# note the giving module name an alias doesn't changes the name of functions in module.
# Importing All Functions in a Module
# we can import every function from module using * operator.
"""
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
# and since all function would be imported we can use those functions natively without the dot operator, but the risk is the functions in that module is of same name as a function in our code, that could cause unexpected behaviour in code.. and we should generally avoid this habit when writing code in production.

# btw, when we import large modules which we didn't wrote, it is possile that both module and your code has conflicting name of a function and then python will literally overwrite function.
# some general note
#1. If we specify a default value for a parameter, no spaces should be used on either side of the equal sign in the function definition.
"""
def function_name(parameter_0, parameter_1='default value')
"""
#2.The same convention should be used for keyword arguments in function calls:
"""
function_name(value_0, parameter_1='value')
"""
<-----------------end of document---------------->