# Hello Fellas,
# This would be our 5th tutorial covering topics like user inputs and while loops.

name = input("enter your name.") 
print(name)

# Assigning output of "input()" function to the variable "name",
# Input function works by taking one input argument "prompt", prompt is the thing that we want to display to the user so that they know what kind of info programme exepcts from them.
# some times you want to display prompts which spans multiple line in that case declare a variable and assign the prompt you want to show to that variable and then pass that variable as argument to "input()" functions, here is a little demonstration of the concept..
prompt = """If you share your name, we can personalize the messages you see.
What is your first name? """ 

name = input(prompt)
print(f"\nHello, {name}!")
# look how on line 7, we used triple quotes to define multiline strings.

"hello"
# the above string written on line 17 will be ignored by interpreter as pythons interpreter ignores any string written out of context.
# Important note- the "input()" function converts evrything which enntered via user to string, for more clarity see example below.
age = input("How old are you? ")
# let's assumme you wrote some  integer 20, as your age.

print(type(age))
# output- "<class 'str'>"

# This inherent behaviour of input function could cause bugs if you aren't careful,  one instance where things could possible go wrong is desribed below..
"""
print(age >= 18)
"""
"""
Traceback (most recent call last):
  File "/home/surya/python-project/python-crash-course/Tutorial-5.py", line 27, in <module>
    print(age >= 18)
          ^^^^^^^^^
TypeError: '>=' not supported between instances of 'str' and 'int'
"""
# the error above generated is ofc, you  can't compare an english word(string) with a number(particularly integer) to see which one is greater..and thus interpreter threw this error.
# we can use "int()" function to typecast the string output of "input()"" function
age = int(age) # typecasts string data type using "int()" function
print(type(age)) # returns data tpe of age.
print(age >= 18) # returns  "True " boolean value

#you could also do the function composition to reduce redundancy.
"""
age = int(input("How old are you?"))
"""
# here we took input from user and also convert the data type into integer in one line.

# The modulo operator (%) returns the remainder when divided by certain nummber., syntax is "a % b", essnetially will return remainder when "a" is divide by "b"..
print(5%3)  # will output equal to 2.  

# ======================================================================
# LOOPs
#=======================================================================
# while loops essentially keeps looping until the mathematical conditional statement evaluates to false that is before every iteration while loop evaluates the mathematical statements.
current_number = 1
while current_number <= 5:
 print(current_number)
 current_number += 1
# the conditional statement  is "current_number <= 5" basically gets re-evaluated after each iteration of loop if output is "True" boolean value the block of code under loop would be re-executed and if it's output is "False" the loop exits silently.
# one more thing is in while loop is you must increment or decrement the looping variable manually.

# Flags- flags are just a concept in python of using a standard boolean variable (True or False) to act as a signal that controls the overall state of your program, example below.
prompt = """\nTell me something, and I will repeat it back to you: \nEnter 'quit' to end the program. """
active = True
while active:
 message = input(prompt)
 if message == 'quit':
  active = False
 else:
  print(message)
# We set the variable "active" to True so the program starts in an active state, and whenever the user types 'quit', the flag variable updates to false and while loop exits on next iteration.
# why do we need flags?
# say you have a system in which you hav only one condition to check, you can simply write a condition like "while user_input != "quit":", but if you are making a complex game then you as a dev would be tired writing behemoth's like this "while user_input != 'quit' and health > 0 and time_left > 0:" every time or atleast this makes code less readable, and hence we use flags to let  loop running until one  condition fails, that's  what we kind of did in code from line -64 to 71.

# break and continue
# break - The break keyword terminates the execution of the loop. It immediately transfers the program's control flow to the statement strictly following the terminated loop block.(basically whenever inside a loop it encounters break keyword. it just killls  the execution of current loop and  immediately starts executing the next  instructions written in programme.)
# examples.

number = 1
while number <= 5:
    if number == 3:
        break  # Loop completely terminates here, after printing 1,2.
    
    print(number)
    number += 1

print("Loop finished!")

# continue- The continue statement terminates the execution of the current iteration of the loop. It immediately transfers the program's control flow back to the loop's header to evaluate the boolean condition (in a while loop) or to request the next item from the iterator protocol (in a for loop),  well loop header is nothing but the very first line of loop.
# example

number = 0

while number < 5:
    number += 1
    
    if number == 3:
        continue  # Skips the print statement and jumps back to the top and while loops evaluates condition once more.
        
    print(number)

print("Loop finished!")

# using a while loop with dictionaries and lists.
#A for loop is effective for looping through a list or dictionaries, but we shouldn’t modify a list or dictionaries inside a for loop(see line 107) because Python will have trouble keeping track of the items in the list.To modify a list as you work through it, use a while loop. Using while loops with lists and dictionaries allows you to collect, store, and organize input to examine and report on later.

# in tutorial 4 we saw an example where we tried to add a key-value pair in dictioanry in middle of a for loop but it ended with a catastrophic error "RuntimeError: dictionary changed size during iteration"

# and  if we modify a list in middle of a for loop, theres not that much catastrophic error but it creates bugs by skipping data silently and you would never know what is going wrong.
# see this example.
# We want to remove all 'banned' users from the list.

users = [ 'alice', 'banned_user_1', 'banned_user_2', 'charlie' ]
banned = [ 'banned_user_1', 'banned_user_2' ] 
for user in users:
    if user in banned:
        users.remove(user)

print(users)
# OUTPUT: ['alice', 'banned_user_2', 'charlie'] 
# explanation of the anomaly- the for loop uses iterator protocol and which is the main reason this cause issues here's how,
#1. The loop starts and goes through index 0 without any issues.
#2. The loop checks index 1 ('banned_user_1') and removes it.
#3. Because a list is a contiguous block of memory, the moment index 1 is deleted, everything shifts to the left to fill the gap. 'banned_user_2' slides into the index 1 spot.
#4. But the for loop's internal counter blindly moves forward to check index 2 as . It completely skips over 'banned_user_2'!

# one more thing to note that when evaluating statements while  loop only cares about the boolean value of the  statement. if it's "True" the loop will execute and if it's "False" and any dictionary or list will  be evalluates as "True" until it is empty whence empty it will  be evaluated as "False"

# how using while loops saves us, since while loop deosn't relies on iterator protocol it just checks the condition each time for "True" or "False" it is less prone to errors and hidden bugs

# Transferring the content of one list into another.

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users: # this loop evvaluates to true until "uncomfirmed_users" list becomes empty.

 current_user = unconfirmed_users.pop()# using pop methhod we already learnt.

 print(f"Verifying user: {current_user.title()}")
 confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
 print(confirmed_user.title())
