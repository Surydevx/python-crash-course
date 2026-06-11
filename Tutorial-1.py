# These notes on python covers chapter 1, 2 & 3.
print("hello world");
x = "hello surya"
print(x)# print function prints values of variables too.but how?
# variables aren't container for data in python they are just a mere label (label=name),actually variables are just name you can assign to container in ram storing certain values.
# there are a lot of built in data types in python...
"""strings as a data type"""
x = "hello the string must be encoded in quotes both single or double quotes works"
print(x[0])# we can just use print function to print values of specific terms of string data type
#string data type works like an array. i.e. stores data as a sequence of characters.

"""for _ in x:
    print(x[_])"""#  this doesn't works as in the first iteration "_" becomes first element of the string i.e. "h" and hey...print(x[h]){_ = h} doesn't makes any sense to python interpreter.

"""lesson learnt that looping variable must be an integer. and the keyword "in" in the declaration of loop literally assigns values of each character in string to looping variables"""

"""range is a function which takes an integer  input an dreturns all the values lesser than itself including 0, though remember it only gives natural no's  as outputs, sample of this is in below line"""

z = range(7)# 7 is a prime no. fun fact :)
print(z)# look how this just prints output as range(0,7) as rang function generates new numbers only upon asking on, otherwise range function just stores info about three parameters.

for _ in z:
    print(_)# see in this "_" takes values in "z" and prints it. though it asks what is the next value in z, and it starts at "0" thenn "1" and then upto "n-1" where n is the input of range function.

# range function formally takes input as range(start,stop,step) the defualt version of range function starts with "0" and use step size of 1.


for _ in range(len(x)):
    print(x[_])# it's a for loop, and for loop is inheretly made to traverse these linear data types.

# while loop on the other hannd works by evaluating condition each time, and doesn't modifies the value of looping variable but for loop does modify the looping variable aautomatically it's method is after each iteration it assigns a new value to the looping variable by simply asking "what is the next value in string?"
#---------------------------------------string methods-----------------------------------
"""generally the methods on strings doesn't chnages the original string. they just give new output, if you want you can save the new output into new string."""
# changing case of strings, using "title()" method.
yapping = "yadayada blabla"
print(yapping.title()) # only capitalizes the first letter of all the string character seperated by space.(why though? would it also do the same if we seperate te words using underscore rather than space?)
"""A general note  that methods are an action that python can perform on data, the syntax is "variable.method()", note that variables here aren't data, actual data are objects in memory. the physical manifestation of class type of variable which is predefined in python(you can use "type(variable_name)" function to determine the data type. and class from it was created.), objects  are formed using some "placeholder_eplanation_here"."""

# methods like "upper()" and "lower()", there functions are self explainable.

#Formatted strings,(basically strings which have blanks or spaces and we can insert anytthing in between...value of any variable whether it is integer, string float...or whatever. by ) why was this needed? traditionall strings were kinda messy when it came to insert value of a variable which has numerical value as concatanation of string doesn't allows concatanion of string with integer.
# demo of Formatted strings.
stupid_string =  "some placeholder string"
print("You can see "+ stupid_string)
# this worked but see this.
stupid_numerical_value = 3 # 3 is a prime number f.f. :)
# print("you will never see this  print cause of concatantion error "+ stupid_numerical_value)
print(f"hello thhis is formatted string and here is your another string {stupid_string} and some stupid numerical value{stupid_numerical_value}")
# general note ---> use escape sequences under a string to include illegal characters, special characters into the string like " \t " and  " \n " , " \\ ", " \' " , " \" " and so on so forth.
x = "hello this is a \"demo\" of escape sequences."
print(x)
print("this is another \"demo\" of escape sequences.")
# interpreting these escape sequences is done by print() function by defualt these escape sequnces are just stored as string into the memory, only when print function interprets  this.
# another  string method is "dumb_variable..strip()" which basically removes whitespaces from starting and ending the string (removes any amount of whitespacing)
dumb_string = " some dumb text placeholder       "
print(dumb_string.strip())
print(dumb_string)# notice that "strip()" method doesn't changes the original string. maybe related to the fact that strings are immutable objects in python. that once you did a typo in a string is created it is fcked up you would need to create a brand new string and assigning it the name same as you did to old string value, as python automatically cleans the unrefrenced objects.
# we have some news! There are varieties of strip method. core strip method removes whitespaces from both sides of the string, lstrip method removes the whitespaces from the left side of the string$ and rstrip method removes whitespcaces from right sides of the strings.
# another string method is "removeprefix()" this method needs input as what prefix to remmove basically...you can input string, numbers, or whatever that makes sense, yk i felt that we can even input a variable's value. or a functions output.
"""out of context but we can chain functions under functions syntax as "function-1(function-2(input-value-for-function-2))" and also apply multiple methods on a data. syntax is "variable_name.method_1.method_2"."""
"""fck strings"""
#general notes#

# python variables are smart af, you cna give them that x = 3*2 or 3/2 and whole lots of operations you can do and it first perform mathematical operation and then assign mathematical value to the variable. alternatively you can do whole lots of calculations under print function, '+' behaves as concatanation and addition operator, and yeah python supports order of operations, basically glorified bodmas and supports more operators rather than just mathematical operator.
# underscores in numbers are a way for programmer to make large nummbers(for ex. amount of money i want) it doesn't affects how pythpn interprets or compiles your code. for ex-- 10_000_000_000_000_00.(yes :) )
# multiple  assignmennts to multiple variables, syntax is "x,y,z = value-1,value02,value-3"
# single asssginment to multiple variables. syntax is "x=y=z = value"
#while python doesn't have built in data type to declare a constant, it inherently just uses variables and for programmers peace of mind they declare name of variable in all capital letters to denote that the variable is indeed a constant variable and never be changed.
#################lists###################
#it's a linear data type which can hold multiple data types, but list is ordered means you should be able to access elements  of list usinng index.
stupid_list = ["hello", 2, 3.5, 2+3j ]# yes python have inbuilt data type for complex numbers.
print(stupid_list[0])
# we can write a for loop for it.
for _ in stupid_list:# earllier i did "stupid_list[]" but this triggered an error cuz these square brackets are used strictly for indexing purposes.
    print(_)

## see this how we can just use the string methods with a string value under list named "bicycle"
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())#btw the general syntax was "variable_name.string_method()" where, variable_name = "some stupid string"
#index in list elements starts at 0, as like string.
#sometimes we would want to access the last element fo string or list.+---+---+---+---+---+---+
""" | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6  -5  -4  -3  -2  -1      """ # see this string.
# we can understand that we can acces the last element of the list or string using the index "-1" and second last as "-2"...though this might be sufficient for now but for slicing the string you need to undrstand the above diagram, where index doesn't represents elements of string but their connections.
print(bicycles[-2].title())
print(bicycles[-1].title())
print(bicycles[-3].title())
message = f"My first bicycle was a {bicycles[0].title()}."# we can also use f strings under variable, and we can not just print values of variable, we can print values of particular index of list or string, along with chaining methods. 
print(message)
# editing a particular element of an list (note that this behaviour wasn't possible in string as strings are immutable but we can pick an index and re-assign it a new value and it would accept.)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# adding elements in the last of list using append method.
motorcycles.append("ducati")# you don't have to assign it a variable name, it changes the original list, this behaviour suggests that lists are of mutable nature.
print(motorcycles)
# we can insert elements into any position nut just at end of the list, here's the syntax goes..."insert(index, value)" where  index is of your choice in list where you want to put value in list.
"""motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)""" # this is an example, i think now our model that index are basically glue which joins two elements of the string or list.

# deleting an element from list..
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]# okay syntax is quite new...i exppected it as another method which supposed to be invoked using "variable_name.method_nmae()" but ig this is invoked just usning del keyword in a statement.
print(motorcycles) 
"""
# assume list as a stack of elements where last element is on top.
# use pop() method, to remove last element of the list or basically remove the top element of the stack, i understood, basically the same work woudl be done by delete statement but then you wonn't be abble to do anything from that deleted value and hence we use pop too, we can even pop element from a specific  index of the list...syntax is "list_variable.pop(index_of_the_element_you_want_to_pop)"
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() # yes, this method  would return a value and you gotta print it or save it in a variable.

print(motorcycles)
print(popped_motorcycle)
# remember either you use delete statement or pop method both removes the element from original list.
"""
# demonstrating how to pop element from a specific index.
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)#  we wanted to pop first element of the list that's why put '0' as an input for pop() method.

print(f"The first motorcycle I owned was a {first_owned.title()}.") # f-strings we could achieve the same results if we directly used the pop function. #  print(f"The first motorcycle i owned was a {motorcycles.pop(0).title()}")

"""
# removing an element from a list usinhg it's values, happens via "remove(value of elements you want to remove)" method.
"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati') # see how this just removes value "ducati" wherever this is present in the list, and also notice that this method doesn't outputs any value that we can use, it just remove elements from list by taking input as a value.
print(motorcycles)
# there's an important note about remove method,  The remove() method deletes only the first occurrence of the value we specify. If there's a possibility the value appears more than once in the list, you'll need to use a loop to make sure all occurrences of the value are removed
"""
############ Organizing a list ###############

#sort() method- it sorts your list permanently, that is channging the original list to a sorted list alphabetically.
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()# again we aren'tr expecting any kind of output here, it jusrt does it's assigned work.
print(cars)
"""
# another way to use sort method.
"""
 cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)# Notice now it would sort list in an  reverse alphabetical order, btw this just changes the index...it dosn't modifies the content so if we used the same  method on an unordered data-type...that wouldn't make any sense.so that's why using sort method only makes sense in case of the data-type is ordered and mutale ofc, this method won't work on strings.
print(cars)

"""
# Sorting the list using sorted function.
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))# notice that this is a function not a method though both works same, i assume it is a stanndard predefine function and thus must apply to list or any data type doesn't matter is mutable or immutable or is ordered or unordered, it can also sort if your list has numbers.
print("\nHere is the original list again:")
print(cars)
"""
# using sorted() function to sort a list which has numbers instead of charaters.
mynumbers= [1,2,3,9,5,7,6,8,0,3,4,5,2,86,4,788,57,3,545]
print(sorted(mynumbers))
# output is "[0, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 57, 86, 545, 788]"
# Notice that if two elements are repeated it just repeats them in it's  output.
# what if the list has charcaters and numbers?
"""
mylist = ["hello", 'c', 'a' ,'a', 'b', 'b', 'd',9,1,4,2,4,5,5,6,3,5,5,6,6,7,3,25,6,7,7]
print(sorted(mylist))
Traceback (most recent call last):
  File "<python-input-17>", line 1, in <module>
    print(sorted(mylist))
          ~~~~~~^^^^^^^^
TypeError: '<' not supported between instances of 'int' and 'str'

# haha, we got the limit, it can sort characters,strings,integers...but can't sort different data types(isn't it obvious,even i won't eb able to do that how can a dumb computer can?)

"""
# sorted(variable_name) also supports a "reverse = True" value as an input.
# Notice about behaviour of sorted function-Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several ways to interpret capital letters when determining a sort order, and specifying the exact order can be more complex than we want to deal with at this time.

# printing a list in reverse order

# we gonnna use the reverse() method (notice the difference between method and function each time we use them.) as the name suggest it reverse the order  of the list (this doens't implies that it sorts backward-alhabetically but it just simply reverse the order of the list)
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
#reverse method reverses the order of list permanently and changes the original list. though we can just reverse the list again to get to original list.
"""
# this will end soon lmao.
# how to find length of list? Simply use "len()" function
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
# output- "4"
notice that now we didn;t use a method but a function.(maybe functions are predefined globally, though methods are specifically are for objects of a class? i am just predicting.
"""
#<--------------The End------------------>#