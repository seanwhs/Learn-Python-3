# 1. Positional Parameters 
# The most common form of parameters. 
# When you define a function, you specify the parameters in a fixed order
# When you call the function, you pass arguments that correspond to the parameters' positions.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 30)

# 2. Keyword Parameters
# Call a function by specifying the parameter names in the function call, 
# regardless of the order in which they appear in the function definition. 
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=55, name="Sean")

# 3. Default Parameters
# Provide default values for parameters in the function definition. 
# If caller does not provide a value for those parameters, default values will be used.
def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

greet("James")  # Uses the default age value of 25
greet("Bob", 30)  # Overrides the default age

# 4. Variable-Length Parameters
# Accept a variable number of arguments. There are two types of variable-length parameters:
# *args (Non-keyword arguments): It allows you to pass a variable number of positional arguments.
# **kwargs (Keyword arguments): It allows you to pass a variable number of keyword arguments.


# Using *args:
# When you don't know in advance how many arguments will be passed, you can use *args. 
# It collects all the additional positional arguments into a tuple.

def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3)  # Outputs: 1 2 3

# Using **kwargs:
# **kwargs is used to pass a variable number of keyword arguments, 
# and it collects them into a dictionary.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)  # Outputs: name: Alice, age: 30

# 5. Combination of Positional, Default, *args, and **kwargs Parameters
# Python allows a combination of different types of parameters, 
# but they must appear in a specific order:

# Positional parameters
# - Default parameters
# - *args
# - **kwargs

def function(a, b=2, *args, c=5, **kwargs):
    print(a, b, args, c, kwargs)

function(1, 3, 4, 5, d=6, e=7)

# 6. Lambda Functions and Parameters
# Lambda functions are anonymous functions defined with the lambda keyword. 
# You can define lambda functions with parameters just like regular functions.
add = lambda x, y: x + y
print(add(3, 4))  # Outputs: 7

# Code Samples for Python Function Parameters
# Sample 1: Positional Parameters
def multiply(a, b):
    return a * b

result = multiply(3, 4)  # Passing arguments positionally
print(result)  # Output: 12

# Sample 2: Keyword Parameters
def introduce(name, age):
    print(f"Hi, I'm {name} and I'm {age} years old.")

introduce(name="John", age=25)  # Passing arguments as keywords

# Sample 3: Default Parameters
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # Uses default greeting
greet("Bob", "Hi")  # Overrides default greeting

# Sample 4a: Variable-Length Positional Arguments (*args)
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(10, 20, 30, 40))  # Output: 100

# Sample 4b: Variable-Length Positional Arguments (*args)
def greet(*names):
    for name in names:
        print(f"Hello {name}")

greet("Alice", "Bob", "Charlie")  
# Output:
# Hello Alice
# Hello Bob
# Hello Charlie

# Sample 5a: Variable-Length Keyword Arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

# Sample 5b: Variable-Length Keyword Arguments (**kwargs)
def greet_kwargs(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

greet_kwargs(name="Alice", age=25)  
# Output:
# name: Alice
# age: 25

# Sample 6: Mixing Different Parameters
def profile(name, age=30, *hobbies, **extra_info):
    print(f"Name: {name}, Age: {age}")
    print("Hobbies:", hobbies)
    print("Extra Information:", extra_info)

profile("Alice", 25, "Reading", "Cycling", city="New York", occupation="Engineer")
# Output:
# Name: Alice, Age: 25
# Hobbies: ('Reading', 'Cycling')
# Extra Information: {'city': 'New York', 'occupation': 'Engineer'}

