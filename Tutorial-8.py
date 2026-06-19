
# so, this  is the 8th tutorial.
# we will learn "FILES AND EXCEPTIONS".
# Reading from a File
# Reading the Contents of a File
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)
# explanation of the code.
# see line 6, to tell the python paths of a file we use the module "pathlib" and we imported class "Path"
# see line 7, we created an object named "path" from class "Paths" and passed the relative path of the file "pi_digits.txt".
# see line 8, we used the method "read_text()" on the object "paths", which suggest that the class "Path" had a function in it's definitiot strictly to read text. and to return a value whenever callled, and the value got stored in the variable named "contents"
"""
PYTHON-CRASH-COURSE on  main [?] via  v3.14.5
❯ python Tutorial-8.py
3.1415926535
8979323846
2643383279

"""
# this is the output, the output had an empty line at the end of output that is line 20.
# paths? it's a location of a file or a directory in a storage drive.. in linux distribution '/' defines root and any user who can access this level of directory is named as superuser, and apart that we have directories like '/home/user_name', these paths of a file are almost alwasy stored like in a tree like structure so yk, and in linux file system, everything starts witha  root. in this subdriectories all other users live, and applications, all kernels, operating system itself can be accessed by someone who is a superuser.
# how can you give someone address of a very famous cafe? 
#1. either you would argue that this is the google map location..(say that it is precise, anyone from all over  the world could just visit that cafe, it's absolute location, doesn't matter where you are the map is same for you.)
#2. or you say that "hey man, just take this road straight and then take a left and then again left. and thus you get to the cafe" what you told were the instructions to tell him location of the cafe relative to wherever he is present now.
#simple right?  yes! that's you call absolute and relative paths.
# we use similar logic to denote where a folder(call it directory from now on) or a file in the file system.
# The is the reasoon for line 22, the contents of the file are returned as a single string, which we assign to the variable contents. When we print the value of contents, we see the entire contents of the text file.
# okay so whenever we are giving the relative paths, we must keep this on our mind that where is the system currently is in the directory structure, be default whenever just a name is given of the file see line 7, it means that the programme would only check for this file in the same directory as the programme, if it's not in same folder you would need to use relative paths or absolute paths, 
# To tell Python (and the Linux file system) to move up one directory level relative to where you currently are, you use two dots (..).

#Same directory: Path('pi_digits.txt')
#Inside a lower folder: Path('data_folders/pi_digits.txt')
#Up one level (higher directory): Path('../pi_digits.txt')
#Up two levels, then into a folder: Path('../../config/pi_digits.txt')
# using absolute paths is very simply you just start with the '/' directory. for example "path = Path('/home/eric/data_files/text_files/filename.txt')"

#Accessing a File’s Lines
# we can use the splitlines() method to turn a long string into a set of lines, and then use a for loop to examine each line from a file, one at a time. example code.
"""
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
print(line)
"""
# explanation of the code above.
# the splitlines() method belongs specifically to string objects.
# any text file which has lines will be loaded into ram as "some text on line-1\nfrom  here  second line starts\nn from here 3rd line does."
# and splitlines() method just checks this invisible '\n' excape sequences by default (we could just give it some input and it would treat that character as a trigger to cut the string.)

#The Mechanics of splitlines()
#splitlines() is a built-in string method which cuts strings.
#It takes your massive string and reads it from left to right, hunting specifically for newline characters (\n or \r\n).
#The exact millisecond it detects a newline character, it slices the string into two separate pieces.
#It deliberately deletes the \n character entirely. It does not keep it attached to the text
#It takes all those freshly sliced, clean pieces of text and drops them into a standard Python List.
# how it worked real time as our code ran.
"""
# When line 44 executes, Python reads the file from hard drive and allocates a single, contiguous block of ram to hold every single character as one giant string. If the file has a 100000 lines,we now have one massive string in memory with a 100000 hidden \n (newline) characters buried inside it.

# When line 45 executes, Python invokes the splitlines() string method.
#It scans the massive string from left to right(order is imp.), looking for those hidden \n characters.
#Every time it hits a \n, it "cuts" the text and creates a brand new, separate string object in memory.
#It stores the memory addresses of all these new, smaller strings inside a standard Python List.
# and this method is incredibly inefficient as it is requiring you double the size of the file to just load the file into the ram, wdym?
"""
# Working with a File’s Contents
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
 pi_string += line
print(pi_string)
print(len(pi_string))
# i will explain how this code works!
# everything is predictable and new code is line 75 , we have defined an empty string
# See line 76 and 77, we have assigned a for loop on the output of the splitlines() method, and we know that this  method returns a list, and thus it means that for loop on line 76, would be looping on this list returned by method "splitlines()", and line 77 is simple, it just concatanates strings, and stores all lines in the variable name "pi_string", well rest of the code is simple.
# btw in practice this method of string conncatannation is clunky, as strings are immutable to just add a new element to  a string, it recalculates the amount of memory it needs and  asks the os to gie it a new space, and can you imagine running this  loop for an large data?
# Writing to a File 
# Once you have a path defined, you can write to a file using the write_text() method.
#as understood we used the read_text() method and now we are using write_text() method.
# btw these are methods of what class? i believe these are from class named "Path" which is a class written in pathlib module.
"""
from pathlib import Path
path = Path('programming.txt')
path.write_text("I love programming.")
"""
#If programming.txt does not exist at the specified path point in the drive, Python will ask the OS to create it and write string in it.

#If programming.txt already exists, and it has 10,000 lines of highly valuable data inside it, write_text() will completely obliterate the entire file instantly, without asking for permission, and replace all 10,000 lines with "I love programming."

#Also, after writing the string to the file, it makes sure the file is closed properly. Files that aren’t closed properly can lead to missing or corrupted data.

# write_text() method operates in "Write" mode ('w'), which in C/Linux system calls literally means "truncate the file to zero bytes, then write the new data."

#Python can only write strings to a text file. If we want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.

# To write data more than one line, you would need to store your string in a variable and then pass that variable into write_text()" method.

#Exceptions
#yk why we  study exceptions and error handling is bcz you don't want you end users to see complex traceback  error messages, it is better that programmme end gracefully with your pre  decided error message than porgramm crashing with a complex traebackw hhich confuses users and more so if you users are malicious hackers, this  traceback would allow them to get more than they should knoiw about your porgrammes stucture and this info could be used maliciously
# let's start with error and exceptions 
#Python uses special objects called exceptions to manage errors that arise during a program’s execution.Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object. If you write code that handles the exception, the program will continue running.
#Exceptions are handled with try- except blocks. A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised.
#Handling the ZeroDivisionError Exception
# see this code.
"""
print(5/0)
"""
# output of the above code
"""Traceback (most recent call last):
File "division_calculator.py", line 1, in <module>
print(5/0)
~^~
ZeroDivisionError: division by zero
"""
#notie that the error reported in the traceback, ZeroDivisionError, is an exception object in memory.
# now see the modified code.
"""
try:
print(5/0)
except ZeroDivisionError:
print("You can't divide by zero!")
"""
# see this, we places our risky code in try, 
#we place our risky code in try block and we put alternative instructions to run in except block if the code in tyr lock results in a particular kind of exception.
# though notice that we need to know what kind of exception our porgramme would have and then use try except block to handle that exception, so it's kinda trial and error.
#notice that if our try blck didn't have raised any exception, then except block of code would have never ran anyways.
#In this example, the code in the try block produces a ZeroDivisionError, so Python looks for an except block telling it how to respond. Python then runs the code in that block, and the user sees a friendly error message instead of a traceback
#Using Exceptions to Prevent Crashes
# Handling errors correctly is especially important when the program has more work to do after the error occurs.
# see this code.
"""
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
first_number = input("\nFirst number: ")
second_number = input("Second number: ")

answer = int(first_number) / int(second_number)
print(answer)
"""
# if we input second number as 0, the porgramme would crash literally
# see code whhich handles this exception,
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
 first_number = input("\nFirst number: ")
 if first_number == 'q':
  break
 second_number = input("Second number: ")
 if second_number == 'q':
  break

 try:
  answer = int(first_number) / int(second_number)

 except ValueError:
  print("please input only numerical values")

 except ZeroDivisionError:
  print("you are trying to divide by zero, which is actually undefined, and please don't think that it is infinty. ")
 else:
  print(answer)
#This example also includes an else block. Any code that depends on the try block executing successfully goes in the else block. and risky code  itself goes into tty block and if we think a certain type of error can occur we declare an except block telling interpreter what to do in case that crertain error occurs.
# did u notice that i used two except blocks relative  to two possible exceptions
# one more  thing is you need to know that yopou won't alwasy know what kind of error and exception you programme into, so during testing phase  you write code like this
"""
try:
    # Some crazy unpredictable code
    risky_operation()
    
except Exception as e:
    # This catches EVERYTHING, and 'e' is the actual exception object.
    # It allows you to inspect the exact error without crashing.
    print(f"I caught an unknown error: {type(e).__name__}")
"""
# and then run the code each time you find a new bug or error. consider that this is a sbad practice in actual production env. as ig hides the acctual bugs the code might have.
