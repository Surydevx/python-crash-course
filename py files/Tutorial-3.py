# This is the 3rd tutorial, and this would be covering topics like "statements"
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars: # for loop, with looping variable looping on car names.
# the we work towards if-else statements.
 if car == 'bmw': 
  print(car.upper())
 else:
  print(car.title())

# i willl clear your doubts once for all, so listen carefully and don't zone out in middle.
""" 
"Statements" are basically "assertions" made by someone, such that it can either be true or false not both at the same time.
The if-else statements inherently works on this simple principle, they evaluate the statement  written, if it evaluates to a 'True' bool value then that code block will get executed other wise it won't.
"""

# assignment vs comparison
"""
assignment operator is used  to  assign value to some object...
comparison operator is used to compare the values stored in both objects
for ex.
x = y # this is an assignment operator
x == y # this is an comparison operator.
"""
#note- Comparison operator is case sensitive when it comes to compare string values of both variables.
# To check if a value is not equal to other use "!=" operator, this is similar in practice to the comparison operator we used earlier.

# using keyword - "and" & "or" to evaluate two conditions simultaneously in statements.
# example for "and " statement
"""
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
#output - "False
age_1 = 22
age_0 >= 21 and age_1 >= 21
# output - "True"
"""
#  example for "or" statement
"""
age_0 = 22
age_1 = 18
x = age_0 >= 21 or age_1 >= 21
print(x)
# output -"True"
age_0 = 18
x = age_0 >= 21 or age_1 >= 21
print(x)
#output - "False"
"""
# Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
# output- "True"
print('pepperoni' in requested_toppings)
# output-"False"
# the above syntax works like "desired_thing in example_list" yep, this is it, you try to check if your desired thing is in list or not.


# Checking Whether a Value Is Not in a List

#This works in same spirit as it does just now the syntax changes to "desired_thing not in example_list", this works by checking if the desired_thing is in example_list or not, if it is then it returns False and if it doesn't it returns True value. 
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.")

#  booolean values.
# "True" & "False" are two values understood as boolean values in programming, Expressions which get evaluated as "True" or "False" not both at the same time though are called as boolean expression,Variables which hold boolean values are called as boolean variables, Boolean expressions are fundamental in evaluating while loops, if statements, if-elif statements, if-else statements these are the some examples i know about.

################################################################
# control flow statements #

# if statements.
"""
These are simple statements  using "if" keyword, Syntax of initiating an if statement is "if some_condition:" the condition gets evaluated as one of the two boolean values,
if it evaluates to "False", the code block doesn't executes.
if it evaluates to "True", the code block gets executed.
btw the colon (:) tells the interpreter that next line of code should be treated as start of if - code block.
"""
age = 19
if age >= 18:
 print("You are old enough to vote!")
print("thank you")
# A simple example of if statement, the lifecycle of this code would be exactly  like this - if the condition for "if" statement gets evaluated as false the programme exits the if block and goes on to run whateever instruction written,if the condition for "if" statement gets evaluated as true then  the programme runs the block of code under if block and then exits the block of code to run whatever instructions written after that.
# don't zone out

#if-else statement. 
#
# these are if statements with an catch-all statement(don't get buried in jargon, it simply means that to handle all other cases aside than what if statement is handling.)
age = 17
if age >= 18:
 print("You are old enough to vote!")
 print("Have you registered to vote yet?")
else:# notice that how we are using else statement that is aside from when you are older than 18 or equal to 18, this else statement catches all other cases.
 print("Sorry, you are too young to vote.")
 print("Please register to vote as soon as you turn 18!")
print("thank you for your time")

# btw i think ? technically else should handle bigger pool of cases as if statement handles smaller pool of cases?  right? let me demonstrate what i mean.
# before working our way forward we will see some basic functions
# the typecasting function- "δ()" this is a function which changes the data type of whatever the input data or variable is passed to whatever "δ" represents, δ can be equal to int float etc...(we will take a dediccated tutorial to this function.)
# The function "input("placehplder_string")" takes an input from user supplementing this "placeholder_string".

age = int(input("please enter your age"))# I gave an hint how to use composition of functions in earlier tutorials, here you go for a full blown example, here you can see that our δ function is equal to int and hence effectively typecasting the answer to integer data type.

if age < 18:
 print("you are under age")
 print("find your dad and go away")
else:
 print("you are elgible to vote, congrats.")
print("thank you")
#  that's what we did here now, else is handling bigger pool of cases, though as a dev(yes you are levelling up yayyy), you are allowed to proceed upto your own dsicretion though just make sure that any production code is read more times than it was written, so readability is atmost importance and make sure that you follow guideline zen of python....written below..
import this # you could import something in middle of code ? damn,  btw this isn't readable and this makes code look messy, in reality avoid this practice.

# if-elif-else statement.
# this statement works by first evaluating "if statement's" condition if that fails then "elif statement's" condition gets evaluated and if that fails then our catch-all block of code gets executed(notice that else block doesn't have any mathematical condition written on it)
# if our "if statement's" condition is evaluated to true and then the programme will exit control-flow statements, and if "if statement" fails then next "elif statement's" gets evaluated and if it's evaluates to true then programme will exit the control-flow statement after executing the elif code block.
age = 12
if age < 4:
 print("Your admission cost is 0 INR.")
elif age < 18:
 print("Your admission cost is 25 INR.")
else:
 print("Your admission cost is 40 INR.")

# multiple elif statements.
# the logic here is similar, the interpreter will evaluate if block if finds it to be false, then move to the next elif block, if elif statement is false then move to next elif and so on, though it will execute else block at the end after checking every if and elif statements.
# if at any stage of checking if  and elif statements if the condition becomes true then the code block under that if or elif would e executed and the interpreter would exit the control-flow-satetment.

age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 25
elif age < 65:
 price = 40
else:
 price = 20
print(f"Your admission cost is ₹{price}.")
# one special note is that you can omit to use else block in your code it is not necessary if you have dealt all the cases in your if and elif statements
# Right upto this point we used a three type of control-flow statements and all of them had one common thing that only one valid case would execute and all other cases would not, so if you have some mental model which has multiple valid cases then use if-if statement.
# if - if statement.
# the flow of this statement is...interpreter would check first if statement's condition then if it is true then execute that block of code and then move on to next if statement to evaluate and so on....
# at each level it doesn't matter if the "if statement" evaluates to true or false, the next if statement will get evaluated nonetheless. 
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")

print("\nFinished making your pizza!")
# in short we use if-if statements when there are many possible cases and we would want to act on each of those cases if they are true.
#<---------------end of document---------------->