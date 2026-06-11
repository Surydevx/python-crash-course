# This is tutorial 2, this portion will cover chapter 4 named as "LOOPS"

magicians = ['alice', 'david', 'carolina']

for magician in magicians: # this line tells interpreter to take first value in the variable "magicians" and assign it to our looping variable and after that in the first iteration (understand that when loops evaluates 2nd time then we say that loop's iterating 1st time), the looping variable gets next value in the avriable "magician".
 print(magician) 
# for loop is generally used to loop throgh a sequence, note that here you aren't modifying the looping variable each time, the interpreter automatically asigns next value in the "magician" to looping variable for each iteration after the last iteration the loop exits and interpreter starts reading the next line in the source code.
# See this.
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
 
 print(f"{magician.title()}, that was a great trick!") # this print statement will run each time this loop runs and each time it will use "title()" of strings to modify the names of the  magicians, and we used formatted strings to print those values into a string.
 
 # one more thought is python doesn't uses curly brackets it just use indentation( it's  upto you how much indentation you want to give though just make it constant for the whole file...)

magicians = ['alice', 'david', 'carolina']

for magician in magicians:# the colon indicates the loop to consider next line as start fo loop.
 print(f"{magician.title()}, that was a great trick!")

print(f"I can't wait to see your next trick, {magician.title()}.\n")
# this is another code snippet which basically demonstrated how even after loop terminates the looping variable still is in memory.fantastic.

# use of range() function in for loop.
for value in range(1, 5):
 print(value)# this would only print values upto 4.
# range function- "range(start,stop,step)" are three required input needed to range function, by default it coniders to start from 0, and step size 1, and it stops after spitting out exact no. of values specified as an input for "stop".
#Use of list function to generate a list using output of range function.
numbers = list(range(1, 6))# it forces the range function to gennerate a list out of it, since by defualt it doesn't creates a list just stores three variables.
print(numbers)
# more use of list() function.
print(list("Any string written inside quotes wouldd become a list"))
#the output of list function is a list.
#we can convert even a tuple into in list, since tuples are immutable we can convert them into list using list funcyion and then can use it's contents.

my_tuple = ("apple", "banana", "cherry")

print(list(my_tuple))# there you go. and if you want to save the output, assign the output to a variable and then you can change use list built-in methods to modify or use at your own discretion.


# we can use list function to convert the set and dictionaries into lists...

# Converting a Set
my_set = {10, 20, 30}
set_to_list = list(my_set)
print(set_to_list)
# Output: [10, 20, 30] though order of the new list formed isn't guaranteed to be same as of set since set is an unordered data type itself.

# Converting a Dictionary
my_dict = {"name": "Alice", "age": 25}
dict_to_list = list(my_dict)
print(dict_to_list)  
# "Output: ['name', 'age']" be defualt list function only extracts "key"'s to form a list.

# functions that maybe use of statistical inference.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)# finds minimum digit in a list ?since it's a function this might work with more data types.

max(digits)# finds maximum digit in a list ? also must support other data type though i am just predicting..

sum(digits)# finds sum of digit in a list also must supoprt other data type.
# These above functions take name of variables to find the maximum, minimum and sum of the numbers...
#list comprehension.
# pending

#slicing of list..
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# syntax is "list_name[starting_index,stopping_index]"
print(players[-1:-4])# empty string as output.
print(players[-4:-1]) # got it! the start index must represent element on left side compared to stop index, though whatever indexing method you use, stop element must be on right side of the start element, the primaary reason is that lists are unidirectioal, that is they flow left to right...

# copying a list
# if we do slicing of a string such that we don't specify starting index and stopping index and store it in a seperate variable name, the whole list would get copy.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]# we could thought  to use the following syntax "friend_foods = my_foods[]" though it would produce syntax errors as if we put brackets after name of string the interpreter expects an index under it.(more possible explanation to the topic as current details are vague!)
# though if we use syntax like "friend_foods = my_foods" then now both names points to same object in memory.
#and then editing list using one "my_foods.append()" would append the list with given input in apppend function, though now you would be able to access the appended string with "print(friends_food)". we can relate this using ho we used assignments operator(=) to give same value to multiple variables, for ex. "x=y=z=70"

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# TUPLES
# fck the weird name! Tuples are glorified lists. 1) these are immutable,what this means for you is you can not change the original tuple once you declared it. 2) Are ordered just like lists, fck! the abstraction!. This just means you would be ablee tp access elements using their indexes.
example_tuple = (20,30,40,'s','b','d',"surya","sury")# supports multiple data types just like lists...
for _ in example_tuple:
 print(_)# looping through contents of lists

#Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma: "my_t = (3,)" It doesn’t often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.
# To edit a tuple you would need to make a new instannce of a tuple object in memory and then assign sam ename to the new tuple and then pythons garagea collector clears unreferenced objects in memory, the samae is demonstrated in the code below.
dimensions = (200, 50)# it's a Tuple and it is immutable.
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)

dimensions = (400, 100) # yep see the new tuple object in memory.
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)
#<-----end of document----->