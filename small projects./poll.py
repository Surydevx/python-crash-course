# okay so my aim is to make a programme which takes polls.
polls = {}  # intitating empty directory.
x = 1  # some intital value to kickstart while loop.
while x:
    candidate_name = input("please enter your name")
    fav_language = input("please enter your fav programming language")
    polls[candidate_name.strip().title()] = fav_language.strip().title()
    x = input("are there any more peoples joining us?(Y/N)")
    if x == "Y":
        x = 1
    elif x == "N":
        x = 0

for _ in polls:
    print(f"{_} : {polls[_]}")
