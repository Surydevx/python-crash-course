# This is Tutorial 6 part 2.
# The first part got a lot lengthy and i wasn't seeing it ending anytime soon so splitted this tutorial into two parts.
# okay? one more tip is write and design your functions so that they are doing exactly one job, you wouldn't want a spaghetti code, would you?
# preventing a functtion from modifying a list.
# very simple logic, function will change the list and if you don't want that your oriiginal list get changed just pass a copy of the original list as an argument to function.? simple! syntax - "function_name(list_name[:])",the slice notation [:] makes a copy of the list to send to the function
"""
print_models(unprinted_designs[:], completed_models)
"""
#Even though we can preserve the contents of a list by passing a copy of it to functions, we should pass the original list to functions unless we have a specific reason to pass a copy. It’s more efficient for a function to work with an existing list, because this avoids using the time and memory needed to make a separate copy. This is especially true when working with large lists.
# you would notice that as we proceed further just the complexity of code increases and concepts are just those basic ones we already learned.
# Passing an Arbitrary Number of Arguments
# why do we need this? sometimes  we don't know ahead of time how much arguments of a function we would need..? and thus we need this concept. see  example.

#consider a function that builds a pizza. It needs to accept a number of toppings, but we can’t know ahead of time how many toppings a person would choose. The function in the following example has one parameter, "*toppings", but this parameter collects as many arguments as the calling line provides:
def make_pizza(*toppings):
 """Print the list of toppings that have been requested."""
 print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#  what does this * operator does? basically whenever we define a prameter of a function using "*parameter_name" the function would create a tuple and of name "paramater_name",and tuple recieves all the values we gave,
# outputs of code above-
"""
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
"""
# notice how  even if we provide on argument, it would be stored in a tuple now.
# coming to think of it we can use loops to print each member of the tuple precisely.
# only natural condition we can ponder rn is..
# Mixing Positional and Arbitrary Arguments
# If we want that a function accepts several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.
# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.
def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print(f"\nMaking a {size}-inch pizza with the following toppings:")
 for topping in toppings:
  print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#output-
"""
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
"""
#we will often see the generic parameter name *args, which collects arbitrary positional arguments.

