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
 return "hellow"
greet_user()# we called the function as you noticed we could standalone directly..

# The text on line 9 is a comment called a docstring, which describes what the function does. When Python generates documentation for the functions in your programs, it looks for a string immediately after the function's definition
# in above example we didn't need it to give some input in parenthesis, though if the function needs some inpt to do it's ork, it would be passed into those parenthesis.
#  this is modified example.
def greet_user1(username):
 """Display a simple greeting."""
 print(f"Hello, {username.title()}!")
greet_user1('jesse')
# i changed the function name as it was overlapping with our previous function,  note that even if we do use conflicting function names(this  prolly would make code less readbale and understandable..) the python interpreter would  literally overwrite whatever code block you wrote under that function earlier,  but remember interpreter reads code from top to bottom....let's  infact use  conflicting functioin name.

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