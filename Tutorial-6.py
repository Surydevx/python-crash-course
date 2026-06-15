#Hello Fellas,
#this is the 6th tutorial and we will learn about functions.
# so what are actually functions?, defined formally as...
"""
A function is a self-contained block of parameterized, reusable code designed to perform a single, specific operation. It encapsulates a sequence of statements, accepts optional input data (arguments) via designated variables (parameters), and optionally yields a computed value back to the caller while terminating its own execution.
"""
# let me explain what above definition actually mean through code.
def greet_user():# defining a function named "greet_user" and we generally pass input of a function in those brackets..
 """Display a simple greeting."""
 print("Hello!")# whenever this function would be initiated,  this block of code will get executed.
greet_user()# we called the function as you noticed we could standalone directly..

# The text on line 9 is a comment called a docstring, which describes what the function does. When Python generates documentation for the functions in your programs, it looks for a string immediately after the function's definition
# in above example we didn't need it to give some input in parenthesis, though if the function needs some input to do it's work, it would be passed into those parenthesis.
#  this is modified example.
def greet_user1(username):
 """Display a simple greeting."""
 print(f"Hello, {username.title()}!")
greet_user1('jesse')
# i changed the function name as it was overlapping with our previous function,  note that even if we do use conflicting function names(this  prolly would make code less readable and understandable..) the python interpreter would  literally overwrite whatever code block you wrote under that function earlier,  but remember interpreter reads code from top to bottom....let's  infact use  conflicting functioin name.

def greet_user1():
 """Display a simple greeting."""
 print("Hello surya")
greet_user1()
# output -
"""
Hello!
Hello, Jesse!
Hello surya
"""# see the output...the code block under the function with same name written below overwrote the previous code block of the same function name.we can conclude that in Python, a function name is just a variable pointing to a block of code. When you use def greet_user1() a second time, you are simply pointing the greet_user1 variable to a brand new block of code, erasing the connection to the old one.
# Arguments vs. Parameters:
# At the very basic level, a "Parameter" is a variable defined in the function's declaration (it acts as a placeholder for the actual input needed by the function). 
# An "argument" is the actual value you pass into that parameter when you call the function.(remember during call of the function.)
# how to pass arguments to functions.
# there are mainly two ways you can do this,
#1. positional arguments - sometimes function needs multiple arguments, then we create placeholders in function and give argument to function in the same order as we created our parameter. and changing the order may cause absurd behaviour..(it would literally take anything you give it happily)
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')# passing the arguments in same order  as we intend to give to each parameter, be absolutely concered that the order in which you give argument to parameters matters.
#2. keyword arguments- This style of passing multiple arguments is more structured and doesn't depends on you to remember the order(now you have to remember whole names of parameters hehe), what you do here is assign values to parameters in the function call, synntax is "function_name(parameter-1="some random  value",  parameter-2="some more random value")" this is the syntax here goes our example.
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')# you get the syntax right? that's all this topic is.
# note(not really an imp. one)- see you can calll function multiple times with passing same or different arguments each time.(common sense no?)
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
# calling the function two times with different arguments.
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# see above example, the main reason the whole concept of defining functions in your code exists cuz of this. apparently save redundancy in your code.
# apparently soon we will learn about modules  and we will import modules and learn how to use functions of modules in our code.
# default value
#When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value, examaple for this is given below..
def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
# default value is just us giving some value to function during time of definition of the concept, and this is pretty striaghtforward.
describe_pet(pet_name='willie')
# let;'s try with our diff function this concept and experiment with it.
# now pay attention(or pay me) that this function absolutely needs argument ordered, you will ignore this thing and your  output will be messed up..
def create_character( name ="john doe", role = "npc", weapon="none", level="he is everywhere"):# passing default values in function.
 
 """Creates a profile for a new video game character."""
 print(f"--- Character Profile ---")
 print(f"Name:   {name.title()}")
 print(f"Role:   {role.title()}")
 print(f"Weapon: {weapon.title()}")
 print(f"Level:  {level}")
 print("-------------------------\n")

# example 1: positional arguments (order is strictly matched)
create_character('shadow', 'assassin', 'twin daggers', 15)

# example 2: keyword arguments (order doesn't matter)
create_character(level=99, name='gandalf', weapon='staff', role='mage')

# example 3: mixing both type of argument passing.. (positional argument's must come first)
create_character('arthur', 'knight', level=25, weapon='excalibur')
# example 4: understanding default values.'
create_character()# passing nothing,  now function will use default values.
# example 5: if i give some argument but doesn't give some..then?
create_character( "surya" , "admin" )# lmao this works. 

# one very obvious thing you may encounter is that pizza without coke is impossible(not really but my personal preference.) in a similar manner you need to give function all the arguments it needs to work, in mundane words "the number of argument and number of parameters must be same."

## return values of the function..
# let me put in very brief, you call function directly...if you want to save the output of a function? how do u do that?
# you may think ohh, we just have to do ...
def some_function():
 """literally this function will add 2+2"""
 print(2+2)
some_function()# will print 4
# now try this
supposed_to_be_4 = some_function()
print(supposed_to_be_4)
#output-
"""
4
4
None
"""
# wait how one extra 4 came? and why is it "none"? i iterally asssigned the output of the function to the variable? this  is # 1'st  rookie  mistake.(i did this so u don't have to)
# explanation-
# first  4 came  from literally calling the  function.
# second 4 came due to a more interesting behaviour of python interpreter - listen python f]processes the assignment operator a bit differenntly, it first evaluates the right hand side and then after evlauating the right side assigns the value to the left side, so  as soon as python went to left side  it encountered a function, it went to definition of the function and there python just saw the print(2+2), see  on line 104, and it just blasted the output on the terminal. and actually since in function we haven't used return keyword and thus function returns none and saves this in variable and thus the mystery is resolved.
# what is return? - The value that the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function.

# returning a simple value
def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""

 full_name = f"{first_name} {last_name}"

 return full_name.title()

musician = get_formatted_name('suryansh', 'sharma')
print(musician)
# The function returns a string to the variable "musician", when argument "suryansh" and "sharma" were passed to the function, mainly return is used  for taking output from a function to capture, store, or manipulate that data.
#When you call a function that returns a value, you need to provide a variable that the return value can be assigned to.
# Optional arguments in the function,,
# making arumments optional is not very native to python language but is an engineered workaround, see the code below
# observe how we just assigned an default empty string to middle name(ofc middle name aren't necessary and you would find ppls with no middle name), and thus if you don't give function any middle name string it would go on and work without that.
def get_formatted_name(first_name, last_name, middle_name=''):
 """Return a full name, neatly formatted."""

 if middle_name:
  full_name = f"{first_name} {middle_name} {last_name}"

 else:
  full_name = f"{first_name} {last_name}"
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
