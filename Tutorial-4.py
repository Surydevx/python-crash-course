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
# the del statement deletes the key we specify and the value associated with in the dictionary.
