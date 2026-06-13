###This is the 4th tutorial, we will be explicitly larning dictionaries.
#===========================
# A simple dictionary
#===========================
# syntax for a simple dictionary is described as follows...
temp_dict = {"key-1" : "value-1","key-2" : "value-2","key-3" : "value-3"}# we could have infinite number of key-value pairs in it.

# A dictionary is a simple collection of key value pairs, each key is associated with some value..and value of a key can be anything be it string,  integer,float, or another dictionary, or you can use custom object made by custom class as a value to the key.
# accessing the values in a  dictionary.
# the syntax here is like this "name_of_dict[key]", mention key whose values you want to access.
colors = {'color': 'green'}
print(colors['color'])
#output's- "green"
# similarly you could add new key-value pairs into the dictionary using the following syntax "dict[some_key]=some value", where dict is the name of dictionary and some_key is our declaration of key and some_value is our declaration of value f the keyw e declared our earlier.
colors["fav"]="blue"
for _ in colors:
 print(colors[_])# this should print all the values of a dictionary, as the looping variable loops through dictionary and which means looping variable would loop through all the key's of dictionary.
#output -
"""
green
blue
"""
# notice that we are accessing or creating new values into dictionary element via "key", that's our identifier.
# what if we had two key's with the same name? i predict that there would some error from python interpreter.

temp_dict={'blue':10,'red':9,'brown':5,"maroon":11,"burgundy":8.5}#all the color's name i could remember at the moment and the respective numbers are  my subjective ratings.does anyone agree?
print(temp_dict)
#output
"""
{'blue': 10, 'red': 9, 'brown': 5, 'maroon': 11, 'burgundy': 8.5}
"""
# let's add one more key-value pair. brown-9 (i am purposefully taking different value for brown)
temp_dict["brown"] = 9
print(temp_dict)
#output
"""{'blue': 10, 'red': 9, 'brown': 9, 'maroon': 11, 'burgundy': 8.5}"""
# okay, i was wrong. so it overwrote previous value of brown, which actually suggest that any new key-value pairs are added at last when though it first checks if key- value pairs are new? 
#though i come to a concusion that key's are more important than values, since changing values of a key, it overwrote the value of same key already present in the dictionary,  which suggest that key with same name can't be present in same dictionary though different key with same value can be present in dictionary.
# with this i also think that the key-value pairs must be unique, that's no redundancy that is the dictionary enforces that there must be only one key of a kind, no two keys can be same.. of a kind, no two keys can be same..
# i happened to have some stroke of intutition that these key's are bheaving much like a variable would upon re-updating a variable value. (i am wrong maybe)
# ohh, one thing goes without saying is dictionaries are mutable unlike strings, but dictionaries do respect order, all the key-value pairs are in an order as they were assigned during creation of dicionary or addition of new elements of the dictionary.
#At times we define empty dcitionary cuz we expect that with time the programme will add and remove the contents of dictionary, wait man?there must be a way to remove a key-value pair from dictionary..empty dictioanary generated below.
empty_dictionary = {}# see, it is empty...

#Modifying Values in a Dictionary
# ahh, a bit before we accidentally explored  this concept before.
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'# re-assigning values to the key= "color"
print(f"The alien is now {alien_0['color']}.")

#Removing Key-Value Pairs
# yay just as i was expecting we got the way to remove an key-value pairs from a dictionary.
# example.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0["points"]# why this doesn't get's printed? like i was expecting '5' as a value...
print(alien_0["points"])# prints value which key "points" holds in the dictionary.
del alien_0['points']# okay, so this is the syntax. you just need key you want to delete and the name of dictionary.
print(alien_0)
# the del statement deletes the key we specify and the value associated with in the dictionary, though it is deleted permanently so be sure.
"""
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])# will print error as no key exists with the name "points"
"""
# output
"""
Traceback (most recent call last):
File "alien_no_points.py", line 2, in <module>
print(alien_0['points'])
~~~~~~~^^^^^^^^^^
KeyError: 'points'
"""
# accessing dictionary values via specifying key's has helped us accessing the dictionary, ut what if you asked the dcitionary for a key-value pair that doesn't exists? that would cause interpreter errors.

# so to save our asses from above problem we will use dictiioary method, called "get()"
"""
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
""" 
# the syntax for "get()" method is "dict_name.get("searched_key","message to be displayed if the key isn't found.")" the get method gives a graceful message instead a interpreter crash.
#If you leave out the second argument in the call to get() and the key doesn’t exist, Python will return the value None. The special value None means “no value exists.”This is not an error: it’s a special value meant to indicate the absence of a value.

#looping through a dictionary
# we have looped through a dictionary earlier, though theres a small catch, we have a diff approach this time.
# using two variable for loop along with "item()" method..called sequential unpacking.
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():# we have two looping variables though they kind of proceed in like a pair(what i mean here is they both gets corresponding value at the same time.). Good technique..
# we are using items() method, which is a method of dictionary, and what it does is it returns a tuple of key-value pairs on each iteration on demand by for loop, which they gets assigned to to the two looping variables.
 print(f"\nKey: {key}")
 print(f"Value: {value}")
# why this method is different? yk by default when we use for loop for dictionaries, see example in line 15, the loop variable only loops with the keys, not the values....though we could engineer same output from that method. It comes down to personal preference, though i personally feel that using "items()" is cleaner approach that forces us to think in a new direction that using two variables  is possible.
# I am kind of unsatisfied with the explanation...so i would be diving more deep.
# so, i came to few revelations that dictionary actually remembers the order in which you put key-value pairs, why this important? cause the book i am following just tripped me cause it was kind of old and before version of python like 3.7 or something the dictionary didn't remembered the ordered in which u placed them, what that meant for u was..when using for loop to print every key-value pairs of the dictionary you could get totally scrambled order in output while knowing that this isn't the order you placed pairs into dictionaries.

# So what we are loooking at here is a mix of two concepts, used iplicityly w/o mentioning by the author at this level.

#1. sequence unpacking
#2. Dictionary view objects, 

# sequencce unpacking 
#
# it is a method by which we can assign two or more variable values from an iterable data type like sttring,list,tuple,set,frozenset in a single line.

# Basic Unpacking

student_info = ("Alice", 24, "Computer Science")# we used tuple bbut any iterable data type could be used.

name, age, major = student_info# we assigned  values to 3 variables considering the number of elements of tuple..yep both numbers  should be same or otherwise python interpreter will throw and error.

print(name)  # Output: Alice
print(age)   # Output: 24
print(major) # Output: Computer science.

# there would be a seperate tutorial on this  sequence unpacking for now this much knowledge on topic should be enough.

# dictionary view objects- there are three methods for dictionary data type and upon calling these method these  method invokes dictionary view class which in turn creates the dictionary view object actuall memory of the host systemn which is named  differently to whichever dictionary method called it..
#keys()-dictionary view objects callled as "dict_keys"
#values()-dictionary view objects callled as "dict_values"
#items() - dictionary view objects callled as "dict_items"
# further exploration of the topic....
# None of the dictionary view objects holds  data, they only hold addresses of the  actual dictionary objects, and only returns data from dictionary upon request.
# dict_items= it handles data in a tuple data type whenever for loop asks for it using iterator protocol and since dict_items itself doesn't hold a static copy of the dictioary but instead use pointers  it can dynamically access the dictionaory using pointers thus after updation of a dictionaries content immediately we can access the new key-value pair.
# keys() method
# this method initiates the dict_keys object which upon request by for loop gives keys one by one of dictionary.
# values() method
# this method intiates the dict_values object which upon request by for loop gives values one by one from dictionary.

# Notes- since by default for loop loops over keys of a dictionary..you actuallly don't need to use keys method.

# i gave a thought why dict_items gives us key-value pair in a tuple form? findings are shocking! listen - out of all the data type tuple is the only data type which is immuatble, is ordered and keeps the original data type. for example...immutable data types are string, forzenset, tuple. but forzenset is not ordered and it enforces uniquenness (that's if you had your key-value pairs as same, frozenset would literally just one entry and would keep only unique entry) and understand that string and tuples are ordered and immutable....but string enforces all data types into strings...which causes hard to find bugs....so tuple is the natural and only choice of data type.
# why immutabble is so necessary.? i gave it a thought...my obv and first reaction was duh cause of security? you don't want your data to get change in middle of dict_items object fetching data from actual dictionary..but it kinda serves this purpose instead it goes this even further, it is because saving us from  side-effects of abstraction(thanks to python devs.) that's how they saved us with this immutability concept. what if you had somethhing in your programe going on which was modifying that data you just called using "items()" method.
#  see this....
user_env = {'os': 'Arch Linux'}

# Imagine this gives you a list instead of a tuple!
for pair in user_env.items(): 
 # pair is now ['os', 'Arch Linux']

 # What happens if you as a developer writes this line by accident?
 """
 pair[0] = 'hacked_key'
 """

# why do we need ordered data type? you might asks? reason is if you used for loop on "dictionary.items()" then dict_items object would be initialied in memory and would return key-value pairs. and if it gave it in a data type which doesn't respect orders then ? you could get value-key pair and looping variables will get opposite values(not exactly opposite cause you would never know when an unordered data type would give data in same order and when not in an same order causing unpredictable behaviour...) and thus we use tuples where strict indexing is necessary...0 represents key and 1 index represents value..
#why do we not data type like frozenset? frozenset has immutability...the reason is that this data type is unordered. and more problematic than that it strictly enforces that data must be unique, and this is a problematic behaviour in a case that if your key and value are same? the forzenset would lterally delete an extra copy...causing your programme to fail critically
# Fundamentally dictionaries in python are hash table, more details would be in a seperate tutorials.(this point is for my own referennce to dig more into these topics.)


#=====================================================
# now's time for code we been doing a lot of theory stuff "# Ref: Charlie Day conspiracy board meme from It's Always Sunny in Philadelphia."
#=====================================================
# how do i know that why and how this much. about items method?, behold and see this...

# 1. Define the original dictionary
user_env = {
    'os': 'Arch Linux', # Yes, i use arch btw.
    'shell': 'Zsh',
    'editor': 'Nvim'
}

# items() method does not copy the dictionaries data into varialble; it's a reference to actual data in the dictionary.
view = user_env.items()


print("==== \"View\" variable points to a dynamic dictionary view object===") # dynamic refers to the below behaviour

# "Modifying the dictionary after we have declared the variable "view" and saved the value in variable." ~ it is called dynammic cause if it was static copy then you won't  get the output you are getting at line 169.
user_env['terminal'] = 'Alacritty'

# The "view" reflects the change instantly because it points directly to user_env
print(view)

# Output: dict_items([('os', 'Arch Linux'), ('shell', 'Zsh'), ('editor', 'Nvim'), ('terminal', 'Alacritty')]),this shows that output of dict_item looks like a list of tuples..and every tuple denotes key-value pair in the order they will written in dictionary and this output proves that printing "view" variable doesn't hold full data they are just refferences to original dictionary as just after editing the data in main dictionary it autmatically reflects the value of variable "view". 

"""
print(view[0]) #problematic code! Running thhis would cause errors.
"""

"""
  File "/home/surya/python-project/python-crash-course/Tutorial-4.py", line 176, in <module>
    print(view[0])
          ~~~~^^^
TypeError: 'dict_items' object is not subscriptable
""" # this is the error you get....mainly because dict_items gives output using iterator protocol :) and indexing fails as it doesn't gives any output when gave any index or rather doesn't know how to process that info, so we use next()or loops to get tuples from dict_items..haha(i am happy for some reason.)
## this also proves that "view" isn't an list, as if it would have,  we would have gotten some output.

# i have a code which is kinda creepy, looks simple but reveals so much about he code.

"""
my_dict = {"A": 1, "B": 2}

for key, value in my_dict.items():
    my_dict["C"] = 3  # Triggers dynamic hash table resizing in RAM!
    print(key, value)
"""
#this is a problematic 
"""
Traceback (most recent call last):
  File "/home/surya/python-project/python-crash-course/Tutorial-4.py", line 182, in <module>
    for key, value in my_dict.items():
                      ~~~~~~~~~~~~~^^
RuntimeError: dictionary changed size during iteration
"""# i must look into hash table problem and how it affects above behaviour and how dictionary and why this error  popped up.
## some more topic completion aside from conspiracy theories.
# we can use "sorted()"" function to present them in an alphabetical order despite whatever the order dictionary was written, here's how would u do that.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# "sorted()" function sorts the keys in an alphabetical order before giving them to for loop, i don't understand how this works...as dictionaries specifically follows iterator protocol in loops like for loop....but if we applly a fuction we effectively saying that sorted function first stores tha keys  in somewhere and then sorts themm into alphabetical order but sorted function is a function..it's not a variable whom we can store any value? wait..i remembered that functions in pythonn are also objects instantiating from inbuilt class in python called as function, could that object have sa=ome variable? idk.
for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")
#for now this seems to work but i will dig onto this in future.
## Looping through values of a dictionary.
# using "values()" method to grab only values of dictionary key-value pairs.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")

# "set()" function makes sure that there are no duplicates before loop starts, main risk is we are using this data type conversion into set is because we don't want duplicating values to haunt us...though using set gives us a tradeoff that now our output won't be ordered :) (hahha i am even more happy)
for language in set(favorite_languages.values()):
    print(language.title())
# output - 
"""
C
Python
Ruby
"""

print(favorite_languages.values()) # by default these "values()" are presented to us as list of values but that's not the case as how computer see this.
# output -"dict_values(['python', 'c', 'ruby', 'python']) "
# even now to access each one of these values we are seeing, the computer needs to go through specific iterator protocol to get these values...we are able to see these values cause python core devs thought that this would help us.and it does. lmao.

# nesting is remained fro future incorporations, as we have done already massive work. thanks for reading this fck ahh tutorial.