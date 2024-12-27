# 1. My First Python Program
# ---------------------------
# print ('I love Hokkien Mee')
# print ("It's really good")

# 2. Variable  = container for value (string, integer, float, boolean)
#           A variable behaves as if it was the value it contains
# ----------------------------------------------------------------------

# Strings
# first_name = 'Sean'
# last_name = 'Wong'
# food = 'Hokkien Mee'
# email = 'email@email.com'

# print (first_name)
# print(f'Hello {first_name} {last_name}')
# print(f'You like {food}')
# print(f'Youe email is {email}')

# Integers
# age = 55
# quantity = 3
# num_of_students = 30

# print(f'You are {age} years old')
# print(f'You are buying {quantity} items')
# print(f'Your clas has {num_of_students} students')

# Floats
# price = 10.99
# gpa = 3.2
# distance = 5.5

# print(f'The price is ${price}.')
# print(f'Your GPA is {gpa}.')
# print(f'You ran {distance} km.')

# Booleans
# is_student = True
# is_student = False

# print (f'Are you a student?: {is_student}')

# if is_student:
#     print('You are a student')
# else:
#     print('You are NOT a student')

# 3. Typecasting is the process of converting a variable from one tyope to another
#       str(), int(), float(), bool()
# ---------------------------------------------------------------------------------
# name = 'Sean Wong'
# age = 55
# gpa = 3.2
# is_student = True

# print('B4 Typecasting')
# print('---------------------')
# print(f' name is of type {type (name)}')
# print(f' age is of type {type (age)}')
# print(f' gpa is of type {type (gpa)}')
# print(f' is_student is of type {type (is_student)}')

# print()
# print('After Typecasting')
# print('---------------------')
# age = float(age)
# age += 1
# print(f' age is {age} and is of type {type (age)}')
# age = str(int(age))
# age += '1'
# print(f' age is {age} and is of type {type (age)}')

# name = bool(name)
# print(name)

# name = ''
# name = bool(name)
# print(name)

# input() -  function that prompts user to enter data
#           Returns enetered data as a string

# name = input('What is your name?: ')
# age = int(input('How old are you?: '))
# age += 1

# print(f'Hello {name}') 
# print('HAPPY BIRTHDAY!!!')
# print(f'You are {age} years old')

# Exercise 1: Rectangle Area Calc
# length = float(input('Enter length of rectangle: '))
# width = float(input('Enter wisth of rectangle: '))
# print(f'Area of rectangle is {length*width} cm^2')

# Exercise 2: Shopping Cart Program
# item = input('What item would you like to buy?: ')
# price = float(input('What is the price?: ')) 
# qty = int(input('How may do you like'))
# total = price * qty
# print(f'You have bought {qty} x {item}/s')
# print(f'Total damage is ${total}')

# 3A. Python Enums
# --------------------------------------------------------------------
# Use enums when you have a fixed set of constants or values 
#       that are logically related.
#  In Python, there are generally two types of enumerations:
#
# Functional Enums (IntEnum): Inherit from enum.IntEnum.
#       Behave like integers and allow comparisons and arithmetic operations.
# Class-based Enums (Enum): Inherit from enum.Enum.  
#       More flexible and can hold any type of value, not just integers. 
#       Support custom methods and properties.

# 3A -1: Enum class in Python
# from enum import Enum  # Importing the Enum base class from the enum module

# # Defining the 'Season' enum class with four members
# class Season(Enum):
#     SPRING = 1    # Enum member SPRING with value 1
#     SUMMER = 2    # Enum member SUMMER with value 2
#     AUTUMN = 3    # Enum member AUTUMN with value 3
#     WINTER = 4    # Enum member WINTER with value 4

# # Printing the enum member 'Season.SPRING'
# print(Season.SPRING)  # Output: Season.SPRING

# # Printing the name of the enum member 'SPRING'
# print(Season.SPRING.name)  # Output: 'SPRING'

# # Printing the value of the enum member 'SPRING'
# print(Season.SPRING.value)  # Output: 1

# # Printing the type of the enum member 'Season.SPRING'
# print(type(Season.SPRING))  # Output: <enum 'Season'>

# # Printing the string representation of the enum member 'Season.SPRING'
# print(repr(Season.SPRING))  # Output: 'Season.SPRING'

# # Printing a list of all the enum members in 'Season'
# print(list(Season))  
# # Output: [<Season.SPRING: 1>, <Season.SUMMER: 2>, <Season.AUTUMN: 3>, <Season.WINTER: 4>]

# 3A -1: Enums Accessing Modes 
# Enum members can be accessed in two ways:
#       By value:- In this method, the value of enum member is passed.
#       By name:- In this method, the name of the enum member is passed.

# from enum import Enum

# # Defining the 'Season' enum class
# class Season(Enum):
#     SPRING = 1    # Enum member SPRING with value 1
#     SUMMER = 2    # Enum member SUMMER with value 2
#     AUTUMN = 3    # Enum member AUTUMN with value 3
#     WINTER = 4    # Enum member WINTER with value 4

# 3A -2: Looping Through Enums
#       Enumerations are iterable
#  
# from enum import Enum

# # Defining the 'Season' enum class
# class Season(Enum):
#     SPRING = 1    # Enum member SPRING with value 1
#     SUMMER = 2    # Enum member SUMMER with value 2
#     AUTUMN = 3    # Enum member AUTUMN with value 3
#     WINTER = 4    # Enum member WINTER with value 4

# # Looping through all enum members in the 'Season' enum
# for season in Season:
#     print(f"{season.value} - {season.name}")  # Printing the value and name of each enum member

# # Accessing an enum member using its value (2)
# print("The enum member associated with value 2 is : ", Season(2).name)  # Output: 'SUMMER'

# # Accessing an enum member using its name ('AUTUMN')
# print("The value associated with enum member 'AUTUMN' is : ", Season['AUTUMN'].value)  # Output: 3

# 3A -3: Enumerations Support Hashing
#       we can hash the Enum class in dictionaries or sets.
  
# import enum

# # Defining the 'Animal' enum class with three members
# class Animal(enum.Enum):
#     dog = 1    # Enum member 'dog' with value 1
#     cat = 2    # Enum member 'cat' with value 2
#     lion = 3   # Enum member 'lion' with value 3

# # Creating an empty dictionary 'di'
# di = {}

# # Adding key-value pairs to the dictionary using enum members
# di[Animal.dog] = 'bark'  # The key is Animal.dog, and the value is 'bark'
# di[Animal.lion] = 'roar'  # The key is Animal.lion, and the value is 'roar'

# # Comparing the dictionary 'di' with another dictionary that has the same keys and values
# if di == {Animal.dog: 'bark', Animal.lion: 'roar'}:
#     print("Enum is hashed")  # If they are equal, print this message
# else:
#     print("Enum is not hashed")  # Otherwise, print this message


# 3A -4: Compare Enums in Python
# Enumerations support two types of comparisons, that are:
#       Identity:- These are checked using keywords “is” and “is not“.
#       Equality :- Equality comparisons of “==” and “!=” types are also supported.

# import enum

# # Defining the 'Animal' enum class with three members
# class Animal(enum.Enum):
#     dog = 1    # Enum member 'dog' with value 1
#     cat = 2    # Enum member 'cat' with value 2
#     lion = 3   # Enum member 'lion' with value 3

# # Checking if Animal.dog is the same as Animal.cat using identity comparison (is)
# if Animal.dog is Animal.cat:
#     print("Dog and cat are same animals")
# else:
#     print("Dog and cat are different animals")

# # Checking if Animal.lion is different from Animal.cat using inequality comparison (!=)
# if Animal.lion != Animal.cat:
#     print("Lions and cat are different")
# else:
#     print("Lions and cat are same")


# import enum  # Importing the enum module to define enumerations

# # Defining the 'Weekday' enum class with three members
# class Weekday(enum.Enum):
#     MONDAY = 1      # Enum member MONDAY with value 1
#     TUESDAY = 2     # Enum member TUESDAY with value 2
#     WEDNESDAY = 3   # Enum member WEDNESDAY with value 3

# # Using enum members as keys in a dictionary
# schedule = {
#     Weekday.MONDAY: "Meeting",      # Key: Weekday.MONDAY, Value: "Meeting"
#     Weekday.TUESDAY: "Presentation", # Key: Weekday.TUESDAY, Value: "Presentation"
#     Weekday.WEDNESDAY: "Training"   # Key: Weekday.WEDNESDAY, Value: "Training"
# }

# # Accessing the value in the dictionary using the enum member 'Weekday.MONDAY'
# print(schedule[Weekday.MONDAY])  # Output: 'Meeting'
# print(schedule[Weekday.TUESDAY])  # Output: 'Presentation'



# 4. Madlibs Game - Create a story by filling blanks with random words
# --------------------------------------------------------------------
# adjective1 = input('Enter an adjective (description): ')
# noun1 = input('Enter a noun (person, place or thing): ')
# adjective2 = input('Enter an adjective (description): ')
# verb1 = input('Enter a verb (action) ending with "ing": ')
# adjective3 = input('Enter an adjective (description): ')

# print('*************************************')
# print(f'Today I went to a {adjective1} zoo.')
# print(f'In an exhibit, I saw a {noun1}.')
# print(f'{noun1} was {adjective2} and {verb1}')
# print(f'I was {adjective3}!')

# 5. Arithmetic and Maths
# -----------------------

# Add, Subtract, Multiply, Divide, Modulus
# friends = 10
# friends += 1
# print(friends)
# friends -= 2
# print(friends)
# friends *= 3
# print(friends)
# friends /= 2
# print(friends)
# friends **= 2
# print(friends)
# remainder = friends % 2 #popular to find even numbers
# print(remainder)

# Math Functions
# x = 3.14
# y = -4
# z = 5
# a = 2

# rounded = round(x)
# print(rounded)
# absolute = abs(y)
# print(absolute)
# power = pow(a, 3)
# print(power)
# maximum = max(a,x,y,z)
# print (maximum)
# minimum = min(a,x,y,z)
# print (minimum)

# Math Module

# import math

# x = 25
# y = 2.1
# z = 2.9

# print(math.pi)
# print(math.e)
# square_root = math.sqrt(x)
# print(square_root)
# round_up = math.ceil(y)
# print(round_up)
# round_down = math.floor(z)
# print(round_down)
# round_to_2_dec = round(math.pi, 2)
# print(round_to_2_dec)

# Exercise: Cal circumference of a circle
# import math
# radius = float(input('Enter radius: '))
# circumference = 2 * math.pi * radius
# print(f'Circumference is: {round(circumference, 2)} cm')

# Exercise: Cal Area of Circle
# import math
# radius = float(input('Enter radius: '))
# area = math.pi * pow(radius, 2)
# print(f'Area is {round(area, 2)} cm**2')

# Exercise: Cal hypotenuse of a right angle triangle
# import math
# a = float(input('Enter side a: ')) 
# b = float(input('Enter side b: '))
# hypotenuse = math.sqrt(pow(a,2) + pow(b,2))
# print(f'Hypotenuse is: {round(hypotenuse,2)} cm') 

# 6. if - execute some code ONLY if some condition is True
# --------------------------------------------------------

# Example 1:
# age = int(input('Enter your age: '))
# if age >= 120:
#     print('You are NOT human. Only humans can sign up!')
# if age >= 100:
#     print('You are You are too old to sign up!')
# elif age >= 18:
#     print('You are signed up!')
# elif age < 0:
#     print("You haven't been borned yet")
# else:
#     print('You must be 18+ to sign up')


# Example 2:
# response = input('Would you like some food? (Y/N) ')
# if response.upper() == 'Y':
#     print('Have some food.')
# elif response.upper() == 'N':
#     print('No food for you.')
# else:
#     print('Invalid Entry')

# Example 3:
# name = input('Enter your name: ')
# if name == '':
#     print('You did NOT type in your name')
# else:
#     print(f'Hello {name}!')

# Example 4:
# for_sale = False
# if for_sale:
#     print('This item is for sale.')
# else:
#     print('This item is NOT for sale')

# Example 5 - Python Calculator
# operator = input('Enter an arithmetic operator (+ - * /): ')
# num1 = float(input('Enter the first number: '))
# num2 = float(input('Enter the second number: '))

# if operator == '+':
#     result = num1 + num2
#     print(round(result, 3))
# elif operator == '-':
#     result = num1 - num2
#     print(round(result, 3))
# elif operator == '*':
#     result = num1 * num2
#     print(round(result, 3))
# elif operator == '/':
#     result = num1 / num2
#     print(round(result, 3))
# else:
#     print(f'{operator} is not a valid operator!')

# Example 6: Python Weight Converter
# weight = float(input('Enter your weight: '))
# unit = input('Kilograms or Pounds: (K/L) ')

# if unit.upper() == 'K':
#     weight *= 2.205
#     unit = 'lb'
#     print(f'Your weight is {round(weight, 2)} {unit}')
# elif unit.upper() == 'L':
#     weight /= 2.205
#     unit = 'kg'
#     print(f'Your weight is {round(weight, 2)} {unit}')
# else:
#     print(f'{unit} is not a valid unit of measurement.')

# Example 6: Python Temperature Converter
# unit = input('Enter Celsius or Farenheit (C/F): ')
# temp = float(input('Enter temperature: '))

# if unit.upper() == 'C':
#     temp = round((9 * temp)/5 + 32, 1)
#     unit = 'F'
#     print(f'Temperature is {temp} degree {unit}')
# elif unit.upper() == 'F':
#     temp = round((temp -32) * 5/9 , 1)
#     unit = 'C'
#     print(f'Temperature is {temp} degree {unit}')
    
# else:
#     print (f'{unit} is not a valid unit of measurement')

# 7. Logical Operators: Evaluate multiple conditions
#   OR - at least ONE condition must be true
#   AND - ALL conditions must be true
#   NOT - inverts the condition
# --------------------------------------------------------

# temp = 18
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print('Outdoor event is cancelled.')
# else:
#     print('Outdoor event is still scheduled.')

# temp = 25
# is_sunny = False

# # To access these emojis, press the Windows Logo + ;
# In Python, logical operators `and` and `or` have lower precedence than comparison operators (like >=, <=, >, <).
# `not` has the highest precedence among logical operators.
# Expressions are evaluated from left to right in terms of operators with the same precedence.

# if temp >=28 and is_sunny:
#     print('It is HOT outside 🥵')
#     print('It is SUNNY ☀️')
# elif temp <= 0 and is_sunny:
#     print('It is COLD outside 🥶')
#     print('It is SUNNY ☀️')
# elif 28 > temp > 0 and is_sunny:
#     print('It is WARM outside 💛')
#     print('It is CLOUDY ☁️')
# if temp >=28 and not is_sunny:
#     print('It is HOT outside 🥵')
#     print('It is SUNNY ☀️')
# elif temp <= 0 and not is_sunny:
#     print('It is COLD outside 🥶')
#     print('It is CLOUDY ☁️')
# elif 28 > temp > 0 and not is_sunny:
#     print('It is WARM outside 💛')
#     print('It is CLOUDY ☁️')

# 8. Conditional Expression or ternary operator - one line shortcut for if 
#       Print or assign one of teo values based on a condition
#       X if condition else Y
# --------------------------------------------------------

# num = -6
# a = 6
# b = 7
# age = 12
# user_role = 'Admin'

# print('Positive' if num > 0 else 'Negative')
# result = 'Even' if num % 2 == 0 else 'Odd'
# print(result)
# max_num = a if a > b else b
# min_num = a if a < b else b
# print(max_num)
# print(min_num)
# status = 'Adult' if age >= 18 else 'Child'
# print(status)
# access_level = 'Full Access' if user_role.lower() == 'admin' else 'Limited Access' 
# print(access_level)

# 9. String Methods
# -----------------------------------

# name = input('Enter your full name: ') # Enter Sean Wong
# phone_number = input('Enter your phone number: ') # Enter 1-234-567-8971
# print(len(name))
# print(name.find(' '))
# print(name.find('S'))
# print(name.find('n'))
# print(name.rfind('n'))
# print(name.find('z')) 
# print(name.capitalize()) # Enter sean wong when prompted
# print(name.upper()) # Enter sean wong when prompted
# print(name.lower()) # Enter sean wong when prompted
# print(name.isdigit()) # Alternate between  sean wong and 1234 when prompted
# print(name.isalpha()) # Enter sean wong when prompted
# print(phone_number.count('-'))
# print(phone_number.replace('-', ' '))
# print(help(str))

# Exercise: validate user input
# - username is no more than 12 caharacters
# - username must not contain spaces
# - username must not contain digits

# username = input('Enter username: ')

# if len(username) > 12:
#     print('username must not be more than 12 characters in length')
# elif not username.find(' ') == -1:
#     print('usernames cannot contain spaces')
# elif not username.isalpha():
#     print('username cannot contain digits')
# else:
#     print(f'Welcome {username}') 

# 10. String indexing - access elements of a sequence using [] (aka indexing operator)
#           [start: end: step]
# ------------------------------------------------------------------------------------

# credit_card_number = '8234-5678-8934-6452'
# nric_number = 'S6755654F'

# print(credit_card_number[0])
# print(credit_card_number[:5])
# print(credit_card_number[0:5])
# print(credit_card_number[5:])
# print(credit_card_number[-1])
# print(credit_card_number[-4:-1])
# print(credit_card_number[-4:])
# print(credit_card_number[::3])

# print(f'xxxx-xxxx-xxxx-{credit_card_number[-4:]}') # print last 4 digits of credit card number
# print(f'{credit_card_number[::-1]}') # reverse credit card number
# print(f'xxxxx{nric_number[-4:]}') # print last 4 chars of nric

# 10. Format Specifiers - {value: flags} formats a string based on flags inserted
#   +: Forces sign (positive or negative).
#   -: Left-aligns the output.
#   0: Pads with zeros.
#   (space): Puts space before positive numbers.
#   ,: Adds comma as a thousands separator.
#   _: Uses underscore as a thousands separator.
#   #: Alternative form (e.g., for octal 0o, hexadecimal 0x).
#   <, >, ^: Alignment (left, right, center).
#   .: Precision (for floating-point or string truncation).
#   %: Percentage formatting.
# ----------------------------------------------------------------------------------

# print(f"{10:#x}")  # Output: '0xa' (for hexadecimal)
# print(f"{8:#o}")   # Output: '0o10' (for octal)
# print(f"{1000:#b}")  # Output: '0b1111101000' (for binary)
# print(f"{3.0:#f}")  # Output: '3.0' (floating point with decimal)

# print(f"{42:<10}")  # Output: '42        ' (left-aligned)
# print(f"{42:>10}")  # Output: '        42' (right-aligned)
# print(f"{42:^10}")  # Output: '    42    ' (center-aligned)

# print(f"{3.14159:.2f}")  # Output: '3.14' (rounds to two decimal places)
# print(f"{0.25:.2%}")  # Output: '25.00%' (formatting as a percentage)

## Example: left-aligned, with padding and a sign
# print(f"{42:+<10}")  # Output: '+42       '

# ## Right-aligned, width of 10, padding with zeros
# print(f"{42:010}")  # Output: '0000000042'

# ## Thousand separator with 2 decimal places
# print(f"{1234567.89:,.2f}")  # Output: '1,234,567.89'

# ## Hexadecimal with alternative form flag
# print(f"{255:#x}")  # Output: '0xff'

# price1 = 30912.1151672
# price2 = -8762.1123
# price3 = 2591.09

# print(f'Price1 is: ${price1:.3f}')
# print(f'Price2 is: ${price2:.2f}')
# print(f'Price3 is: ${price3:.1f}')

# print()
# print(f'Price1 is: ${price1:10}')
# print(f'Price2 is: ${price2:10}')
# print(f'Price3 is: ${price3:10}')

# print()
# print(f'Price1 is: ${price1:010}')
# print(f'Price2 is: ${price2:010}')
# print(f'Price3 is: ${price3:010}')

# print()
# print(f'Price1 is: ${price1:<10}')
# print(f'Price2 is: ${price2:<10}')
# print(f'Price3 is: ${price3:<10}')

# print()
# print(f'Price1 is: ${price1:>10}')
# print(f'Price2 is: ${price2:>10}')
# print(f'Price3 is: ${price3:>10}')

# print()
# print(f'Price1 is: ${price1:^10}')
# print(f'Price2 is: ${price2:^10}')
# print(f'Price3 is: ${price3:^10}')

# print()
# print(f'Price1 is: ${price1:+}')
# print(f'Price2 is: ${price2:+}')
# print(f'Price3 is: ${price3:+}')

# print()
# print(f'Price1 is: ${price1:,}')
# print(f'Price2 is: ${price2:,}')
# print(f'Price3 is: ${price3:,}')

# print()
# print(f'Price1 is: ${price1:+,.2f}')
# print(f'Price2 is: ${price2:+,.2f}')
# print(f'Price3 is: ${price3:+,.2f}')

# 11. While Loops - Execute some code while condition remains true
# ----------------------------------------------------------------
# if else example
# name = input('Enter your name: ')
# if name == '':
#     print('You did not enter your name!!!')
# else:
#     print(f'Hello {name}')

# while loop examples

# name = input('Enter your name: ')
# while name == '':
#     print('You did not enter your name!!!')
#     name = input('Enter your name: ')
# print(f'Hello {name}')

# age = int(input('Enter your age: '))
# while age < 0:
#     print("Age can't be negative!!!")
#     age = int(input('Enter your age: '))
# print(f'You are {age} years old')

# food = input('Enter a food you like (q to quit): ')
# while food != 'q':
#     print(f'You like {food}')
#     food = input('Enter another food you like (q to quit): ')
# print('bye!')

# num = int(input('Enter a number between (1 - 10): '))
# while num < 1 or num > 10:
#     print('You did not enter a number between (1 - 10)!!!')
#     num = int(input('Please enter a number between (1 - 10): '))
# print(f'You entered {num}')

# Example Python Coompound Interest Calculator

# principal = 0
# rate = 0
# time = 0
# while principal <= 0:
#     principal = float(input('Enter principle amount: '))
#     if principal <=0:
#         print('Principal cannot be less than or equal to 0')

# while True:
#     rate = float(input('Enter interest rate: '))
#     if rate < 0:
#         print('Interest rate cannot be less than  0')
#     else:
#         break


# while time <= 0:
#     time = int(input('Enter time in years: '))
#     if time <= 0:
#         print('Time cannot be less than or equal to 0')

# total = principal * pow((1 + rate/100), time)
# print(f'Balance after {time} years is: ${total:,.2f}')

# 12. For Loops - Execute code a fixed number of times
#       You can iterate over a string, range, sequence, etc
# ----------------------------------------------------------------

# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in reversed(range(1,11)):
#     print(i)
# print('Happy New Year!!!')

# credit_card_number = '1234-5678-8901-6564'
# for i in credit_card_number:
#     print(i)

# for i in range(1,21):
#     if i == 13:
#         continue # skip 13
#     else:
#         print(i)

# for i in range(1,21):
#     if i == 13:
#         break # stop execution
#     else:
#         print(i)

# Example: Countdown timer

# import time
# wait_for = int(input('Enter time in seconds: '))
# for i in range(wait_for, 0, -1):
#     seconds = i % 60              # can't exceed 60
#     minutes = int(i/60) % 60      # can't exceed 60
#     hours = int(i/3600) % 24      # can't exceed 24
#     print(f'{hours:02}:{minutes:02}:{seconds:02}')
#     time.sleep(1)
# print("Time's Up")

# 13. Nested Loops - Loop with a loop (Outer, Inner)
#       Outer-Loop:
#           Inner-Loop:

# x = 5  # Initialize x with some value
# y = 3  # Initialize y with some value
# while x > 0:
#     while y > 0:
#         print(f"Now y = {y}, x = {x}")
#         y -= 1  # Decrease y to eventually break the inner loop
#     x -= 1  # Decrease x to eventually break the outer loop
#     y = 3  # Reset y if you want the inner loop to run again for each x


# x = 5  # Initialize x with some value
# while x > 0:
#     for y in range(3):
#         print(f"x = {x}, y = {y}")
#     x -= 1

# for x in range(4):
#     for y in range(3):
#         print(f'x = {x}, y = {y}')


# for x in range(3):
#     y = 3  # Reset y for each iteration of x
#     while y > 0:
#         print(f'x={x}, y={y}')
#         y -= 1

# for x in range(3):
#     for y in range(1,10):
#         print(y, end="")
#     print()

# rows = int(input('Enter Number Of Rows: '))
# cols = int(input('Enter Number Of Columns: '))
# symbol = input('Enter a Symbol to Use: ')
# for x in range(rows):
#     for y in range(cols):
#         print(symbol, end="")
#     print()

# 14. Collection - Single variable used to store multiple values
#       list = [] ordered and mutable. Duplicates OK.
#       set = {} unordered and immutable, but add/remove OK. No Duplicates.
#       tuple = () ordered and immutable. Duplicates OK. Faster.

# fruits = ['apple', 'orange', 'pear', 'apple', 'banana', 'grapes', 'kiwi'] 
# print(fruits)
# print(fruits[1])
# print(fruits[0:3])
# print(fruits[:3])
# print(fruits[::2])
# print(fruits[::-2])
# print(fruits[::-1])
# for fruit in fruits:
#     print(fruit, end=',')
# # print(dir(fruits))
# # print(help(fruits))
# print()
# print(len(fruits))
# print('apple' in fruits)
# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)
# fruits[0] = 'alien-fruit'
# print(fruits)
# fruits.append('pineapple')
# print(fruits)
# fruits.remove('pineapple')
# print(fruits)
# fruits.insert(1, 'durian')
# print(fruits)
# fruits.remove('durian')
# print(fruits)
# print(fruits.index('grapes'))
# print(fruits.count('apple'))
# fruits.clear()
# print(fruits)

# students = {'simon', 'sam', 'peter', 'simon', 'paul', 'mary'}
# # print(dir(students))
# print(students)
# print(len(students))
# print('simon' in students)

# def print_students(iterables):
#     for iterable in iterables:
#         print(iterable, end=', ')
#     print()

# students.add('Jane')
# print_students(students)
# students.remove('Jane')
# print_students(students)

# print(students.pop())
# print_students(students)
# students.clear()
# print(students)


# animals = ('cat', 'dog', 'cat', 'elephant', 'monkey')
# # print(dir(animals))
# print(animals)
# print(animals[3])
# print(animals[:3])
# print(animals[::2])
# print(animals[::-1])
# print(animals.count('cat'))
# print(animals.index('elephant'))
# print(sorted(animals))
# print(len(animals))
# print('leopard' in animals)
# print('cat' in animals)
# print(animals.count('cat'))
# for animal in animals:
#     print(animal, end=', ')

# Exercise: Shopping Cart Program
# foods = []
# prices = []
# total = 0

# while True:
#     food = input('Enter a food to buy (q to quit): ')
#     if food.lower() == 'q':
#         break
#     else:
#         price = float(input(f'Enter price of a {food}: $'))
#         foods.append(food)
#         prices.append(price)

# print('----- YOUR CART -----')

# for food in foods:
#     print(food, end = ' ')

# for price in prices:
#     total += price

# print()
# print(f'Your total is: ${total}')

# Exercise: 2d lists
# fruits = ('apple', 'orange', 'mango', 'pear')
# vegetables = {'celery', 'lettuce', 'chilli'}
# meats = ['beef', 'pork', 'mutton']

# groceries = [fruits, vegetables, meats]
# print(groceries)
# print(groceries[0])
# print(groceries[0][1])

# for collection in groceries:
#     print(collection)

# for collection in groceries:
#     for food in collection:
#         print(food, end = ' ')
#     print()

# Exercise: print telephone keypad
# num_pad =   ((1,2,3),
#             (4,5,6),
#             (7,8,9),
#             ('*', 0, '#'))

# for row in num_pad:
#     for key in row:
#         print(key, end=' ')
#     print()

# # Exercise: Python Quiz Game
# questions = ('How many elements are in the periodic table?: ', 
#             'Which animal lays the largest eggs?: ', 
#             "What is the most abundant gas in Earth's atmoshere?: ", 
#             'How many bones are in the human body?: ', 
#             'Which planet in the solar system is the hottest?: ')

# options = ( ('A. 116', 'B. 117', 'C. 118', 'D. 119'), 
#             ('A. Whale', 'B. Crocodile', 'C. Elephant', 'D. Ostrich'), 
#             ('A. Nitrogen', 'B. Oxygen', 'C. Carbon-Dioxide', 'D. Hydrogen'), 
#             ('A. 206', 'B. 207', 'C. 208', 'D. 209'), 
#             ('A. Mercury', 'B. Venus', 'C. Earth', 'D. Mars'))

# answers = ('C', 'D', 'A', 'A', 'B')

# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print('-------------------------')
#     print(question)
#     for option in options[question_num]:
#         print(option)
    
#     guess = input('Enter (A, B, C, D): ').upper()
#     guesses.append(guess)

#     if guess.upper() not in ('A', 'B', 'C', 'D'):
#         print('Invalid Input')
#     else:
#         if guess == answers[question_num]:
#             score += 1
#             print('CORRECT')
#         else:
#             print('INCORRECT')
#             print(f'{answers[question_num]} is the correct answer')

#     question_num += 1
#     print()

# print('--------------------------------')
# print('           RESULTS')
# print('--------------------------------')

# print('answers: ', end='')
# for answer in answers:
#     print(answer, end =' ')
# print()

# print('guesses: ', end='')
# for guess in guesses:
#     print(guess, end =' ')
# print()

# score = int(score/len(questions) * 100)
# print(f'Your score is {score}%')

# 15. Dictionaries - collection of {key:value} pairs
#                   ordered and mutable. No Duplicates

# capitals = {'Usa':'Washington D.C.',
#             'India': 'New Delhi',
#             'China':'Beijing',
#             'Taiwan':'Taipei',
#             'Malaysia':'Kuala Lumpur',
#             'Indonesia':'Jakarta'}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get('Malaysia'))

# country = input('Enter Country: ').capitalize()
# if capitals.get(country):
#     print(f'Capital of {country} is {capitals.get(country)}')
# else:
#     print(f'{country} is invalid!')

# capitals.update({'Germany':'Berlin', 'Japan':'Tokyo'})
# print(capitals)
# capitals.update({'Indonesia':'Nusantara'})
# print(capitals)

# capitals.pop('Indonesia')
# print(capitals)
# capitals.popitem()
# print(capitals)
# capitals.clea

# items = capitals.items()
# keys = capitals.keys()
# values = capitals.values()
# print(items)
# print(keys)
# print(values)

# choice = input("Enter ('K' for keys or 'V' for values: )")
# if choice.upper() == 'K':
#     for key in capitals.keys():
#         print(key, end = ' ')
#     print
# elif choice.upper() == 'V':
#     for value in capitals.values():
#         print (value, end = ' ')
#     print()
# else:
#     print('Invalid Entry')

# for key, value in capitals.items():
#     print(f'{key}:{value}')


# Exercise: Concession Stand (Store) Program

# menu = {'pizza': 21.0, 
#         'chips': 3.6, 
#         'nachos': 4.25,
#         'mentos': 1.45,
#         'chocolate': 2.55,
#         'pretzel': 3.65,
#         'coke': 1.25,
#         'tea': 2.65,
#         'coffee': 3.55,
#         'lemonade': 5.35,
#         'popcorn': 6.25}

# cart = []
# total = 0

# print('----------- MENU -------------')
# for key, value in menu.items():
#     print(f'{key:10}: ${value:.2f}')
# print('------------------------------')

# while True:
#     food = input('Select an item (q to quit): ')
#     if food.lower() == 'q':
#         break
#     elif menu.get(food):
#         cart.append(food)
    
# print('----------- YOUR ORDER -------------')
# for item in cart:
#     print(item, end=' ')
#     total += menu.get(item)
# print(f'\nTotal is: ${total:.2f}')

# 16. Random Numbers

# import random

# print(dir(random))
# print(help(random))

# print(random.randint(1, 6))

# low = 1
# high = 100
# print(random.randint(low, high))

# fp = random.random()
# print(fp)

# options = ('scissors', 'paper', 'stone')
# play = random.choice(options)
# print(play)

# cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
# print(cards)
# random.shuffle(cards)
# print(cards)

# Exercise: Number guessing game

# import random
# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print('---------------- Python Number Guesing Game ------------------')
# print(f'Select a number between {lowest_num} and {highest_num}.')

# while is_running:
#     guess = input('Enter your guess: ')
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print('NUmber is out of range!!!')
#             print(f'Please select a number between {lowest_num} and {highest_num}.')
#         elif guess < answer:
#             print('Too Low, Try Again')
#         elif guess > answer:
#             print('Too High, Try Again!')
#         else:
#             print(f'CORRECT. The answer was {answer}')
#             print(f'Number of gueses: {guesses}')
#             is_running = False
#     else:
#         print('Invalid guess')
#         print(f'Please select a number between {lowest_num} and {highest_num}.')

# Exercise Scissors, Paper Stone Game
# import random
# options = ('stone', 'paper', 'scissors')
# is_playing = True

# while is_playing:
    
#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input('Enter a choise (stone, paper or scissors): ').lower()

#     print(f'Player: {player}')
#     print(f'Computer: {computer}')

#     if player == computer:
#         print("It's a tie!")
#     elif player == 'scissors' and computer == 'paper':
#         print('You win!')
#     elif player == 'paper' and computer == 'stone':
#         print('You win!')
#     elif player == 'stone' and computer == 'scissors':
#         print('You win!')
#     else:
#         print('You lose!')

#     if not input('Do yopu want to play again (y/n)?: ').lower() =='y':
#         is_playing = False

# print('Thanks for Playing. Bye!')

# Exercise: Dice Roller Game 

# import random

# # print('\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518')
# # ● ┌ ─ ┐ │ └ ┘

# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘")
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # # PRINT VERTICALLY
# # for die in range(num_of_dice):
# #     for line in dice_art.get(dice[die]):
# #         print(line)

# # PRINT HORIZONTALLY
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()


# for die in dice:
#     total += die
# print(f'Total = {total}')

# 17. Function - Block of Reusable Code
#           Place () after function name to invoke it

# def birthday_song(name='You', age=18):
#     print(f'Happy Birthday to {name}!')
#     print(f'You {age} years old!')
#     print('Happy Birthday to You!')
#     print()

# birthday_song()
# birthday_song("Sean")
# birthday_song("Sean", 56)

# def display_invoice(username, amount, due_date):
#     print(f'Hello {username}')
#     print(f'Your bill of ${amount:.2f} is due on {due_date}')

# display_invoice('Sean', 25, '25th December 2024')

# return = statement used to end the function
#   and send a result back to the caller

# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# def multiply(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     return num1 / num2

# first_num = int(input('Enter the first number: '))
# second_num = int(input('Enter the second number: '))
# operations = ('+', '-', '*', '/')
# choice = None

# while choice not in operations:
#     choice = input('Enter the operation(+,-,*,/): ')

# if choice == '+':
#     result = add(first_num, second_num)
#     print(f'{first_num} {choice} {second_num} = {result}')
# elif choice == '-':
#     result = subtract(first_num, second_num)
#     print(f'{first_num} {choice} {second_num} = {result}')
# elif choice == '*':
#     result = multiply(first_num, second_num)
#     print(f'{first_num} {choice} {second_num} = {result}')
# else: 
#     result = divide(first_num, second_num)
#     print(f'{first_num} {choice} {second_num} = {result}')

# def create_name(fname='John', lname='Doe'):
#     fname = fname.capitalize()
#     lname = lname.capitalize()
#     return fname + ' ' + lname

# dummy_name = create_name()
# print(dummy_name)
# full_name = create_name('sean', 'wong')
# print(full_name)

# 18. Default Arguments - Default value for certain parameters
#       default is used when argument is omitted when function is invoked
#       make your functions more flexible, reduces # of arguments
#       1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# def net_price(list_price, discount=0, sales_tax=0.05):
#     return list_price * (1 - discount) * (1 - sales_tax)

# print(net_price(5000))
# print(net_price(5000, 0, 0.05))
# print(net_price(5000, 0.1, 0))

# import time

# def count(end, start=0 ):
#     for x in range(start, end+1):
#         print(x, end=' ', flush=True)  # Force immediate output
#         time.sleep(1)
#     print('DONE!')

# count(10, 0)
# count(10)
# count(30, 20)

# 19. Keyword Arguments - An argument preceeded by an identifier
#       helps with readability
#       order of argumernts doesn't matter
#       1. positional, 2. default, 3. KEYWORD, 4. arbitraty

# def hello(greeting, title, fname, lname):
#     print(f'{greeting}, {title} {fname} {lname}')

# hello('Good Morning', 'Mr.', 'Spongebob', 'Squarepants')
# hello(lname='Squarepants', title='Mr.', fname='Spongebob', greeting='Good Morning')
# hello('Good Morning', lname='Squarepants', title='Mr.', fname='Spongebob') #positional arguments must be first

# for x in range(1, 10):
#     print(x, end=' ') # end is a kw argument
# print()

# print('1', '2', '3', '4', '5', sep='-') # sep is a kw argument


# def get_phone(country, area, first, last):
#     return f'{country}-{area}-{first}-{last}'

# phone = get_phone(country=1, area=123, first=456, last=7890)
# print(phone)

# 20. Arbitraty Arguments - 
# *args     - allow you to pass multiple non-key arguments (tuple)
# **kwargs  - allow you to pass multiple keyword arguments (dictionary)
#           * unpacking operator
#       1. positional, 2. default, 3. keyword, 4. ARBITRARY

# def display_arge_type(*args):
#     print(type(args))
# display_arge_type()

# def add(*args):
#     total=0
#     for arg in args:
#         total += arg
#     return total

# def add(*nums):
#     total=0
#     for num in nums:
#         total += num
#     return total

# print(add(1,2))
# print(add(1,2,3))
# print(add(1,2,3,4))
# print(add(1,2,3,4,5))

# def display_name(*args):
#     for arg in args:
#         print(arg, end = ' ')
#     print()

# display_name('Sean', 'Wong', 'Hong', "Sian")
# display_name('Sean', 'Wong')

# def display_argument_type(**kwargs):
#     print(type(kwargs))
# display_argument_type()

# def print_address(**kwargs):
#     print('---------- ADDRESS ----------')
#     for k, v in kwargs.items():
#         print(f'{k:15}:{v}')
#     print('-----------------------------')

# def print_address(**kwargs):
#     for key in kwargs.keys():
#         print(key)

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)

# print_address(unit='123B', 
#             block='117', 
#             road='Bedok View Street 1', 
#             postal_code='244125')


# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=' ')
#     print()

#     # for value in kwargs.values():
#     #     print(value, end= ' ')
    
#     if 'block' in kwargs:
#         print(f"Apt Blk {kwargs.get('block')}, {kwargs.get('unit')},")
#     else:
#         print(f"{kwargs.get('unit')},")

#     print(f"{kwargs.get('road')}, Singapore({kwargs.get('postal_code')}),")
#     print('Republic of Singapore')

# shipping_label('Dr', 'William', 'Henry', 'Gates',
#                 unit='#10-123B', 
#                 block='117', 
#                 road='Bedok View Street 1', 
#                 postal_code='244125')   # positional arguments must come first


# 21. Itearables - An object/collection that cam return its elements one at a time
#       allowing it to be iterated in a loop

# numbers = [1,2,3,4,5]
# for number in numbers:
#     print(number, end = ' ')

# numbers = [1,2,3,4,5]
# for number in reversed(numbers):
#     print(number, end = ' ')

# sentence = 'Python is freally versatile!'
# for character in sentence:
#     print(character, end =' - ')

# my_dictionary = {'a':1, 'b':2, 'c':3, 'd':4}

# for key in my_dictionary:
#     print(key, end = ' ')

# for value in my_dictionary.values():
#     print(value, end = ' ')

# for key, value in my_dictionary.items():
#     print(f"{key}={value}", end=' ')

# 22. Membership Operators - Used to test whether a value or variable 
#       is found in a sequence (string, list, tuple, set, dictionary)
#       1. in, 2. not in

# word = 'APPLE'
# continue_playing = True

# while continue_playing:
#     letter = input('Guess a letter in the secret word: ').upper()
    
#     if letter in word:
#         print(f'There is a {letter}')
#         continue_playing = False  # Ends the loop if the letter is found
#     else:
#         print(f"'{letter}' was not found!")
#         play_on = input('Continue playing? (y/n): ').lower()
#         if play_on != 'y':
#             continue_playing = False  # Ends the loop if user does not want to continue

# print('Thanks for playing')

# students = {'sam', 'harry', 'daniel', 'bob', 'donald'}
# another = True

# while another:
#     student = input('Enter name of student: ').lower()
#     if student not in students:
#         print(f'{student.capitalize()} was not found!')
#         ask_another = input('Pick another student? (y/n)?: ').lower()
#         if ask_another  != 'y':
#             another = False
#     else:
#         print(f'{student.capitalize()} is a student')
#         another = False
        
#     print('Thanks for using our service. Good Bye')

# grades = {"Sam": 'A', 
#         'Peter':'B', 
#         'Susan':'HD', 
#         'Samson': 'D'}
# keep_asking = True

# while keep_asking:
#     student = input('Enter name of student: ').capitalize()

#     if student in grades:
#         print(f"{student.capitalize()}'s grade is {grades[student]}")
#         keep_asking = False
#     else:
#         print(f'{student.capitalize()} was not found!')
#         ask_another = input('Ask for another student? (y/n): ').lower()
#         if ask_another != 'y':
#             keep_asking = False


# email = 'mail@email.com'

# if '@' in email and '.' in email:
#     print('email is valid')
# else:
#     print('email is invalid')

# 23. List Comprehension - A concise way to create lists in python
#       Compact and easier to read than traditional loops
#       [expression for value in iterable if condition]

# doubles_trad = []
# for x in range(1,11):
#     doubles.append(x * 2)
# print(doubles_trad)

# doubles_lc = [x * 2 for x in range(1,11)]
# squares = [x * x for x in range(1,11)]
# print(doubles_lc)
# print(squares)

# fruits = ['apple', 'orange', 'banana', 'mango', 'durian']
# fruits = [fruit.capitalize() for fruit in fruits]
# fruit_char = [fruit[0] for fruit in fruits]
# print(fruits)
# print(fruit_char)

# numbers = [1,-2, 2, 3, -3, 4,-5,6,-7, 8, -9, 10]
# positive_nums = [number for number in numbers if number>0]
# negative_nums = [number for number in numbers if number<0]
# even_nums = [number for number in numbers if number%2==0]
# odd_nums = [number for number in numbers if number%2!=0]
# positive_even_nums = [number for number in numbers if number%2==0 and number > 0]
# print(f"Numbers:                {numbers}")
# print(f'Positive Numbers:       {positive_nums}')
# print(f'Negative Numbers:       {negative_nums}')
# print(f'Even Numbers:           {even_nums}')
# print(f'Odd Numbers:            {odd_nums}')
# print(f'Positive Even Numbers:  {positive_even_nums}')

# grades = [34, 50, 68, 88, 90, 72, 12, 61]
# student_grades = [('sam', 61), ('daniel', 88), ('mark', 76), ('simon', 34), ('joshua', 12), ('caleb', 28)]
# pasing_grades = [grade for grade in grades if grade > 60]
# pasing_students = [student for student in student_grades if student[1] > 60]
# failing_students = [student for student in student_grades if student[1] < 60]
# print(f'Grades:             {grades}')
# print(f'Passing Grades:     {pasing_grades}')
# print(f"Students' Grades:   {student_grades}")
# print(f'Passing Students:   {pasing_students}')
# print(f'Failing Students:   {failing_students}')

# 24. Match Case Statement (switch) - An alternative to using many elif statements
#       Executes some code if a value mateches a 'case'
#       benefits: Cleaner and easier to read

# def day_of_week(day):
#     if day == 1:
#         return 'Sunday'
#     elif day == 2:
#         return 'Monday'
#     elif day == 3:
#         return 'Tuesday'
#     elif day == 4:
#         return 'Wednesday'
#     elif day == 5:
#         return 'Thursday'
#     elif day == 6:
#         return 'Friday'
#     elif day == 7:
#         return 'Saturday'
#     else:
#         return 'Not a day'
# print(day_of_week(3))       

# def day_of_week(day):
#     match day:
#         case 1:
#             return 'Sunday'
#         case 2:
#             return 'Monday'
#         case 3:
#             return 'Tuesday'
#         case 4:
#             return 'Wednesday'
#         case 5:
#             return 'Thursday'
#         case 6:
#             return 'Friday'
#         case 7:
#             return 'Saturday'
#         case _:
#             return 'Mot a Day'
# print(day_of_week(7))

# def is_weekend(day):
#     match day:
#         case 'Saturday' | 'Sunday':
#             return True
#         case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
#             return False
#         case _:
#             return False
# print(is_weekend('Monday'))

# 25. module - a file containing code you want to include in your program
#       use 'import' to include a module (built-in or your own)
#       useful to break up a large program into reusable files

# print(help('modules')) 
# print(help('math'))

# import math as m 
# from math import e
# print(f'PI:{m.pi}') 
# print(f'Exp: {e}')
# a,b,c,d = 1,2,3,4
# print(f'e raised to {a}:: {e**a}')
# print(f'e raised to {b}:: {e**b}')
# print(f'e raised to {c}:: {e**c}')
# print(f'e raised to {d}:: {e**d}')

# import example as ex #example is a module we created
# print(f'PI:: {ex.pi}')

# radius = 2.44
# circle_circumference = ex.circumference(radius)
# print(f'Circumference for radius: {radius} = {circle_circumference}')
# circle_area = ex.area(radius)
# print(f'Area for radius: {radius} = {circle_area}')

# base = 2
# rasied_to = 5
# result = ex.exponent(base, rasied_to)
# print(f'{base} rasied to {rasied_to} = {result}')

# 26. Scope Resolution
#       Variable Scope - where a variable is visible and accessible
#       Scope resolution (LEGB) - local->enhanced->global->builtin

# def func1():
#     print('------func1-----')
#     x = 1
#     print(f'x = {x}')

# def func2():
#     print('------func2-----')
#     x = 'Hello There'
#     print(f'x = {x}')

# def func3():
#     print('------func_c-----')
#     message = "We can only see variables in our own function!!! "
#     print(f'variable scope = {message}')
#     print(x)

# func1()
# func2()
# func3()

# def func1():
#     x = 1
#     y = 2
#     def func2():
#         y = 'Hello'
#         print(f'Enclosed function. x from calling functions is: {x}')
#         print(f'y from local functions is: {y}')
#     func2()
# func1()

# name = 'spongebob'

# def func1():
#     print(f'func1. variable outside func is global in scope. global name is {name}')

# def func2():
#     print(f'func2. variable outside func is global in scope. global name is {name}')

# func1()
# func2()

# from math import e

# def print_e():
#     print(e) 
# print_e()

# e = 'Hello There'
# print_e() # Remeber LEGB, global comes before builtin

# 27. if __name__ == __main__ : this script can be imported or run standalone
#       functions and classes in this module can be reused
#       without the main block of code executing
# ex.library = import library for functionality
#       when running library directly, display a help page      
#
# def main():
#     # your program goes here
# if name == '__main__':
#     main()
# https://www.youtube.com/watch?v=o4XveLyI6YU

# 28. Exercise: Python Banking Program

# def show_balance(balance):
#     print(f'Your balanace is ${balance:.2f}')

# def deposit():
#     amount = float(input('Enter amount to deposit: '))
#     if amount < 0:
#         print("That's not a valid amount")
#         return 0
#     else:
#         return amount

# def withdrawal(balance):
#     amount = float(input('Enter amount to withdraw: '))
#     if amount < 0:
#         print("That's not a valid amount")
#         return 0
#     elif amount > balance:
#         print('Insufficient funds')
#         return 0
#     else:
#         return amount

# def main():
#     balance = 0
#     is_running = True

#     while is_running:
#         print('------------ BANKING PROGRAM -----------')
#         print('1. Show Balance')
#         print('2. Deposit')
#         print('3. Withdrawal')
#         print('4. Exit')
#         print('----------------------------------------')

#         choice = input('Enter your choice (1-4): ')
#         match choice:
#             case '1': 
#                 show_balance(balance)
#             case '2':
#                 balance += deposit()
#             case '3':
#                 balance -= withdrawal(balance)
#             case '4' :
#                 is_running = False
#             case _ :
#                 print('That is NOT a valid choice!')

#     print('Thank you. Have a nice day!')

# if __name__ == '__main__':
#     main()

# 29. Python Slot Machine
# import random

# def spin_row():
#     symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
#     return [random.choice(symbols) for _ in range(3)]    

# def print_row(row):
#     print(' | '.join(row))

# def get_payout(row, bet):
#     if row[0] == row[1] == row[2]:
#         match row[0]:
#             case '🍒':
#                 return bet * 2
#             case '🍉':
#                 return bet * 4
#             case '🍋':
#                 return bet * 6
#             case '🔔':
#                 return bet * 8
#             case '⭐':
#                 return bet * 10
#     return 0 

# def main():
#     balance = 100

#     print('--------------------------')
#     print(' Welcome to Python Slots ')
#     print(' symbols: 🍒 🍉 🍋 🔔 ⭐')
#     print('--------------------------')

#     while balance > 0:
#         print(f'Current balance: ${balance}')
        
#         bet = input('Place your bet amount: ')

#         if not bet.isdigit():
#             print('Please enter a valid number!')
#             continue

#         bet = int(bet) 

#         if bet > balance:
#             print('Insufficient Funds')
#             continue

#         if bet <= 0:
#             print('Bet must be greater than 0')
#             continue

#         balance -= bet

#         row = spin_row()
#         print('Spinning.../n')
#         print_row(row)

#         payout  = get_payout(row, bet)

#         if payout > 0:
#             print(f'You won ${payout:.2f}')
#         else:
#             print('Sorry you lost this round')

#         balance += payout

#         play_again = input('Would you like to spin again? (y/n): ').lower()
#         if play_again != 'y':
#             break
    
#     print('--------------------------------------------')
#     print(f'Good Game. Your final balance is ${balance}')
#     print('--------------------------------------------')

# if __name__ == '__main__':
#     main()

# 30. Exercise: Encryption Program - Substituion Cipher
# import random
# import string

# chars = ' ' + string.punctuation + string.digits + string.ascii_letters 
# # print(chars)
# chars = list(chars)
# key = chars.copy()

# # print(f'chars:  {chars}')
# # print(f'key:    {key}')

# random.shuffle(key)
# # print(f'chars:  {chars}')
# # print(f'key:    {key}')

# # ENCRYPT
# plain_text = input('Enter a message to encrypt: ')
# cipher_text = ' '

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f'Plain Text:     {plain_text}')
# print(f'Encrypted Text: {cipher_text}')

# # DECRYPT
# cipher_text = input('Enter a message to decrypt: ')
# plain_text = ' '

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]

# print(f'Encrypted Text: {cipher_text}')
# print(f'Plain Text:     {plain_text}')

# 31. Exercise: Hangman in Python
# from wordslist import words
# import random 

# # words = ('apple', 'orange', 'banana', 'kiwi', 'durian', 'mango') # used only for testing
# hangman_art = hangman_art = {0: ("   ",         # key:(). Each key represents an incorrect guess
#                                    "   ",
#                                    "   "),
#                              1: (" o ",
#                                    "   ",
#                                    "   "),
#                              2: (" o ",
#                                    " | ",
#                                    "   "),
#                              3: (" o ",
#                                    "/| ",
#                                    "   "),
#                              4: (" o ",
#                                   "/|\\",
#                                    "   "),
#                               5: (" o ",
#                                    "/|\\",
#                                    "/  "),
#                               6: (" o ",
#                                    "/|\\",
#                                    "/ \\")}

# def display_man(wrong_guesses):
#     for line in hangman_art[wrong_guesses]:
#         print (line)

# def display_hint(hint):
#     print(' '.join(hint))

# def display_answer(answer):
#     print(' '.join(answer))

# def main():
#     answer = random.choice(words)
#     hint = ['_'] * len(answer)
#     wrong_guesses = 0
#     guessed_letters = set()
#     is_running = True

#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         # display_answer(answer) # cheat when testing. remove in production
#         guess = input('Enter a letter: ').lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print('Invalid Input')
#             continue

#         if guess in guessed_letters:
#             print(f'{guess} is already guessed!')
#             continue

#         guessed_letters.add(guess)

#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
#         else:
#             wrong_guesses += 1

#         if '_' not in hint:
#             print('---------------')
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print('YOU WIN!')
#             print('---------------')
#             is_running = False
#         elif wrong_guesses >= len(hangman_art) - 1:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print('YOU LOSE!')
#             is_running = False


# if __name__ == '__main__':
#     main()

# 32. Python Object Oriented Programming
# object - A bundle of related attributes (variables) and methods (functions)
#       Eg phone, cup, book
#       You need a class to create many objects
# class - blueprint use to design and structure and layout of an object

# from car import Car
# car1 = Car('Mustang', 2024, 'Red', False)
# print(car1)
# print(car1.model)
# print(car1.for_sale)
# car1.describe()
# car1.drive()
# car1.stop()

# car2 = Car('Corvette', 2021, 'Blue', True)
# print(car2)
# print(car2.model)
# print(car2.for_sale)
# car2.describe()
# car2.drive()
# car2.stop()

# 33. class variables - shared among all instances of a clsss
#       instance variables are defined inside the constructor
#       class variables are defined outside the constructor
#       All you to share data among all objects created from the class

# class Student:
#     class_year = 2024
#     num_students = 0 

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1

# student1 = Student('Sam', 24)
# student2 = Student('Peter', 35)
# student3 = Student('Benny', 28)
# student4 = Student('Danny', 38)

# print(student1.name, student1.age, student1.class_year, Student.num_students)
# print(student2.name, student2.age, student2.class_year, Student.num_students)
# print(student3.name, student3.age, student3.class_year, Student.num_students)
# print(student4.name, student4.age, student4.class_year, Student.num_students)
# print(Student.class_year)
# print(f'My graduating class 0f {Student.class_year} has {Student.num_students} students')
# print(student1.name)
# print(student2.name)
# print(student3.name)
# print(student4.name)

# 34. Inheritance - Allow a class to inherit methods and attributes from another class
#       Helps wuth reusability and extensibility
#       class Child(Parent)
#       class Sub(Super)

# class Animal():
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f'{self.name} is eating')

#     def sleep(self):
#         print(f'{self.name} is sleeping')

# class Dog(Animal):
#     def speak(self):
#         return 'Woof!'

# class Cat(Animal):
#     def speak(self):
#         return 'Meow!'

# class Mouse(Animal):
#     def speak(self):
#         return 'Squek!'

# dog = Dog('Lassie')
# cat = Cat('Garfield')
# mouse = Mouse('Mickey')

# print(dog.name, cat.name, mouse.name)
# print(dog.is_alive, cat.is_alive, mouse.is_alive)
# dog.eat()
# dog.is_alive = False
# print(dog.is_alive)
# print(dog.speak(), cat.speak(), mouse.speak())

# 35. Multiple, MultiLevel Inheritance
# Multiple Inheritance - Inherit from more than one parent class
#       C(A,B)
# MuliLevel Inheritance - Inherit from a parent which inherits from anotherf parent
#       C(B) <- B(A) <- A 

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} is eating')
    
#     def sleep(self):
#         print(f'{self.name} is sleeping')

# class Prey(Animal):
#     def flee(self):
#         print(f'{self.name} is fleeing!')

# class Predictor(Animal):
#     def hunt(self):
#         print(f'{self.name} is HUnting!')
    
# class Rabbit(Prey):
#     pass

# class Hawk(Predictor):
#     pass

# class Fish(Prey, Predictor):
#     pass

# rabiit = Rabbit('Bugs Bunny')
# hawk = Hawk('Tony')
# fish = Fish('Nemo') 

# rabiit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()

# rabiit.eat()
# hawk.sleep()

# 36. super() - a function used in a child class to call methods from a parent class(superclass)
#       Allows you to extend functionality of the inherited methods

# class Shape:
#     def __init__(self, colour, is_filled):
#         self.colour = colour
#         self.is_filled = is_filled

#     def describe(self):
#         print(f'It is {self.colour} and is {'filled' if self.is_filled else 'not filled'}.')

# class Circle(Shape):
#     def __init__(self, colour, is_filled, radius):
#         super().__init__(colour, is_filled)
#         self.radius = radius

#     def describe(self):
#         print(f'It is a cirle with an area of {3.14 * self.radius * self.radius}cm **')

# class Square(Shape):
#     def __init__(self, colour, is_filled, width):
#         super().__init__(colour, is_filled)
#         self.width = width

#     def describe(self):
#         super().describe()
#         print(f'It is a square with an area of {self.width * self.width}cm **')


# class Triangle(Shape):
#     def __init__(self, colour, is_filled, width, height):
#         super().__init__(colour, is_filled)
#         self.width = width
#         self.height = height

# triangle = Triangle('Red', True, 10, 12)
# circle = Circle(colour='Blue', is_filled=False, radius=10)
# square = Square(colour='Green', is_filled=False, width=10)

# print(triangle.colour, triangle.is_filled, triangle.width, triangle.height)
# print(circle.colour, circle.is_filled, circle.radius)
# triangle.describe()
# circle.describe()
# square.describe()

# 37. Polymorphism - Greek wors that means having many forms or faces
#       Two ways to achieve polymorphism
#       1. Inheritance - An object could be treated as the same type a the parent class
#       2. 'Duck Typing' - Objcet must have neccessary attributes/methods

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2    

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side **2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return (self.base * self.height)/2

# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         self.topping = topping
#         super().__init__(radius)

# circle = Circle(radius = 4) # circle object has 2 forms, Circle and Shape 

# shapes = [Circle(radius = 4), Square(side=5), Triangle(base=6, height=7), Pizza(topping='pepperoni', radius=9)]

# for shape in shapes:
#     print(f"Area is {shape.area()}cm square")

# 38. Duck Typing - Another way to achieve polymorphism besides Inheritance
#       Objects must have the minimum neccesary attributes/methods
#       'If it looks like a duck, and quakes like a duck, it must be a duck'

# class Animal:
#     alive=True

# class Dog(Animal):
#     def speak(self):
#         print('Woof!')

# class Cat(Animal):
#     def speak(self):
#         print('Meow!')

# class Car:
#     alive=False
#     def speak(self):
#         print('Honk!')

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print (animal.alive)

# 39. static methods - method that belongs to a class, NOT any object from that class
#       usually used for general utility functions
# instance methods - for operations on instances of the class (aka objects)
#static methods - for utitlity functions that do not need access to class data

# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def get_info(self):
#         return f'{self.name} - {self.position}'

#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']
#         return position in valid_positions

# employee1 = Employee('Mickey', 'Manager')
# employee2 = Employee('Minnie', 'Cashier')
# employee3 = Employee('Donald', 'Cook')
# employee4 = Employee('Garfield', 'Janitor')

# print(Employee.is_valid_position('cook'.capitalize()))
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())
# print(employee4.get_info())

# 40. class methods - allow operations related to the class itself
#       Take (cls) as the first parameter, which represents the class itself
# Instance methods - for operations on instances of the class (aka objects)
# Static methods - for utility functions that do not need access to class data
# Class methods - for class level data or require access to class itself

# class Student:
#     count = 0
#     tottal_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.tottal_gpa += gpa
    
#     # instance method
#     def get_student(self):
#         print(f"{self.name} - {self.gpa}")

#     @classmethod
#     def get_count(cls):
#         return f'Total number of students: {cls.count}'

#     @classmethod
#     def get_avg_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f'Average gpa: {cls.tottal_gpa / cls.count:.2f}'

# student1 = Student('Trump', 2.7)
# student2 = Student('Harris', 2.8)
# student3 = Student('Biden', 2.3)
# student4 = Student('Pelosi', 3.4)

# print(Student.get_count())
# student1.get_student()
# student2.get_student()
# student3.get_student()
# student4.get_student()
# print(Student.get_avg_gpa())

# 41. magic methods - dunder methods __init__, __str__, __eq__
#       They are automatically called by python's built-in methods
#       They allow developers to define or customize behavior of objects

# class Book:

#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         return f"'{self.title}' - {self.author}"

#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author

#     def __lt__(self, other):
#         return self.num_pages < other.num_pages
    
#     def __Gt__(self, other):
#         return self.num_pages < other.num_pages
    
#     def __add__ (self, other):
#         return f'{self.num_pages + other.num_pages} pages'
    
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
    
#     def __getitem__(self, key):
#       match key:
#           case 'title':
#               return f"Title:'{self.title}'"
#           case 'author':
#               return f"Author:'{self.author}'"
#           case 'pages':
#               return f"Pages:'{self.num_pages}'"
#           case _:
#               return f"'{key}' was not found"

# book1 = Book('The Hobbit', 'JRR Tolkien', 310)
# book2 = Book('Harry Potter', 'JK Rolling', 223)
# book3 = Book('Narnia', 'CS Lewis', 172)
# book4 = Book('Narnia', 'CS Lewis', 599)

# print(book1)
# print(book2)
# print(book3)

# print(book1==book3)
# print(book3==book4)
# print(book3 < book4)
# print(book1 > book2)
# print(book3 + book4)
# print('Hobbit' in book1)
# print('CS' in book4)
# print(book1['title'], book1['author'], book1['pages'], book1['bibliography'])

# 42.@property - decorator used to define a method as a property (it can be accessed like a property)
#       Benefit: Add additional logic when read, write, delete attributes
#       Gives you getter, setter and deliver method

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width     # private attribute
#         self._height = height   # private attribute

#     @property
#     def width(self):
#         return f'{self._width:.1f} cm'

#     @property   
#     def height(self):
#         return f'{self._height:.1f} cm'

#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print('Width must be greater than 0')

#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print('Height must be greater than 0')

#     @width.deleter
#     def width(self):
#         del self._width
#         print('Width has been deleted.')

#     @height.deleter
#     def height(self):
#         del self._height
#         print('Height has been deleted.')

# rectangle = Rectangle(5,6)
# print(rectangle._width, rectangle._height)
# print(rectangle.width, rectangle.height)

# rectangle.width = 0
# rectangle.height = -3
# print(rectangle.width, rectangle.height)

# rectangle.width = 7
# rectangle.height = 8
# print(rectangle.width, rectangle.height)

# del rectangle.width
# del rectangle.height
# # print(rectangle.width, rectangle.height)

# 43. Decorator - A function that extends the behavior of another function
#       w/o modifying the base function
#       Pass the base function as an argument to the decorator
#       @add_sprinkles
#       get_ice_cream{'vanilla}

# def add_sprinkles(function):
#     def wrapper(*args, **kwargs):
#         print('** YOU ADD SPRINKLES 🎊 **')
#         function(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print('**YOU ADD FUDGE 🍫 **')
#         func(*args, **kwargs)
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavour):
#     print(f'Here is your {flavour} ice-cream 🍦')

# get_ice_cream('Vanilla')

# 44. exception handling
# exception - Event that interrupts the flow of a program 
#       (ZerDivisionError, TypeError, ValueError)
#       1. try, 2. except, 3. finally
#   try:
#       try some code
#   except Exception:
#       handle and exception
#   finally:
#       do some cleanup

# try:
#     number = int(input('Enter a number: '))
#     print(1/number)
# except ZeroDivisionError:
#     print('You cannot divide by zero')
# except ValueError:
#     print('Enter only numbers pleaase!')
# except Exception:
#     print('Something went wrong!')
# finally:
#     print('Dp some cleanup.')

# 45. Python file detection

# from genericpath import isdir, isfile
# import os
# filepath = 'test.txt'   # relative path
# filepath2 = 'stuff/test2.txt'
# absolute_path = 'D:\\Documents\\BRO CODE - PYTHON\\stuff\\test2.txt' #\ is an escape char
# absolute_path2 = 'D:/Documents/BRO CODE - PYTHON/stuff' 

# if os.path.exists(filepath):
#     print(f"The location '{filepath}' exists")
#     if os.path.isfile(filepath):
#         print('That is a file')
# else:
#     print('That location does not exist.')

# if os.path.exists(filepath2):
#     print(f"The location '{filepath2}' exists")
# else:
#     print('That location does not exist.')

# if os.path.exists(absolute_path):
#     print(f"The location '{absolute_path}' exists")
#     if os.path.isfile(absolute_path):
#         print('That is a file')
# else:
#     print('That location does not exist.')

# if os.path.exists(absolute_path2):
#     print(f"The location '{absolute_path2}' exists")
#     if os.path.isfile(absolute_path2):
#         print('That is a file')
#     elif os.path.isdir(absolute_path2):
#         print('That is a directory')
# else:
#     print('That location does not exist.')

# 46. Python writing files (*.txt, *.json. *.csv)
# import json
# import csv

# txt_data = 'I Love Python.'
# append_data = 'This is a new line.'
# filepath = 'output.txt' # relative file path
# filepath2 = 'output2.txt' 
# employees = ['Sam', 'Simon', 'Patrick', "Mary", 'Jane']
# emp_path = 'employees.txt' 
# person = {
#     'name':'Patricia',
#     'age':'16',
#     'occupation': 'student'
# }
# person_path = 'person.json' 
# indented_person_path = 'person-indent.json' 
# people = [['Name', 'Age', 'Occupation'],
#           ['James', 25, 'Chef'],
#           ['Simon', 43, 'Manager'],
#           ['Samantha', 34, 'Accountant'],
#           ['Jane', 38, 'Data Scientist']]
# people_path = 'stuff/people.csv'

# with open(file=filepath, mode='w') as file: # overwrite file if exists
#     file.write(txt_data)
#     print(f"Text file '{filepath}' was created")

# try:
#     with open(file=filepath2, mode='x') as file: # write only if file does NOT exists
#         file.write(txt_data)
#         print(f"Text file '{filepath2}' was created")
# except FileExistsError:
#     print(f'{filepath2} already exists!')

# with open(file=filepath2, mode='a') as file: # append to exisiting file
#     file.write('\n' + append_data)
#     print(f"Text appended to file '{filepath2}'")

# try: 
#     with open(emp_path, 'w') as file:
#         for employee in employees:
#             file.write(employee + ', ')
#         print(f"'{emp_path}' was created!")
# except TypeError:
#     print('write() argument must be str, not list')


# with open(person_path, 'w') as file:
#     json.dump(person, file)
#     print(f'{person_path} was created')

# with open(indented_person_path, 'w') as file:
#     json.dump(person, file, indent=4) # indent each element by 4 spaces
#     print(f'{indented_person_path} was created')

# with open(people_path, 'w', newline='') as file:
#     writer = csv.writer(file) # create write object
#     for individual in people:
#         writer.writerow(individual)
#     print(f'{people_path} was created')

# 47. Python reading file (txt, json, csv)
# import json
# import csv 

# txt_file = 'output2.txt'
# json_file = 'person.json'
# csv_file = 'stuff/people.csv'

# # Text File
# try:
#     with open(txt_file, 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print('File not found')
# except PermissionError:
#     print('You do not have permission to read that file.')

# # json file
# try:
#     with open(json_file, 'r') as file:
#         content = json.load(file)
#         print(content)
#         print(f"Name: {content['name']}")
#         print(f"Age: {content['age']}")
# except FileNotFoundError:
#     print('File not found')
# except PermissionError:
#     print('You do not have permission to read that file.')

# # csv file
# try:
#     with open(csv_file, 'r') as file:
#         content = csv.reader(file)
#         for line in content: # print rows
#             print(line)
# except FileNotFoundError:
#     print('File not found')
# except PermissionError:
#     print('You do not have permission to read that file.')

# try:
#     with open(csv_file, 'r') as file:
#         content = csv.reader(file)
#         for line in content: # print columns
#             print(line[0])
# except FileNotFoundError:
#     print('File not found')
# except PermissionError:
#     print('You do not have permission to read that file.')

# 48. Python date and time
# import datetime # use system clock

# # Create specific date and time objects
# date = datetime.date(2024, 2, 22)  # Specific date: 22nd February 2024
# today = datetime.date.today()  # Current date (today)
# time = datetime.time(12, 30, 0)  # Time object for 12:30:00
# now = datetime.datetime.now()  # Current date and time (datetime object)

# # Format the current datetime in a custom way
# now_formatted = now.strftime('%H:%M:%S %d-%m-%Y')  # Time in HH:MM:SS day-month-year format

# # Print all objects
# print(f"Specific date: {date}")
# print(f"Today's date: {today}")
# print(f"Specific time: {time}")
# print(f"Current date and time: {now}")
# print(f"Formatted current date and time: {now_formatted}")

# target_datetime = datetime.datetime(2020, 1, 12, 12, 1)
# current_datetime = datetime.datetime.now()

# print('---------------------------------')
# if target_datetime < current_datetime:
#     print('Target date is in the past')
# elif target_datetime > current_datetime:
#     print('Target date is in the future')
# else:
#     print('Target date is the same as current_date')

# 49. Exercise: Python Alarm Clock
# import time
# import datetime #allow us to work with string representations of time

# # to suppress pygame notice
# from os import environ
# environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
# # execute above b4 importing pygamne

# import pygame #for sound effects

# def set_alarm(alarm_time):
#     print(f"Alarm set for:: {alarm_time}")
#     sound_file = 'Alarm.mp3'
#     is_running = True
    
#     while is_running:
#         current_time = datetime.datetime.now().strftime('%H:%M:%S')
#         print(current_time)

#         if current_time == alarm_time:
#             print('WAKE UP!! 🌅')
            
#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()

#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)

#             is_running = False
#         time.sleep(1)

# if __name__ == '__main__':
#     alarm_time = input('Enter alarm time (HH:MM:SS)')
#     set_alarm(alarm_time)

# 50. Multithreading - Performing multiple tasks concurrently
#       Good for I?O bound tasks like reading files or fetching data from APIs
#       threading.Thread(target=my_function)

# import threading
# import time

# dog_name='Scooby'

# def walk_the_dog(name):
#     time.sleep(8)
#     print(f'Walk {name}.')

# def throw_trash():
#     time.sleep(2)
#     print('Throw trash.')

# def read_email():
#     time.sleep(10)
#     print('Read email.')

# def wash_dishes():
#     time.sleep(3)
#     print('Wash dishes.')

# def do_laundry():
#     time.sleep(5)
#     print('Do laundry.')

# def write_report():
#     time.sleep(10)
#     print('Write Report.')

# def buy_lunch():
#     time.sleep(4)
#     print('Buy Lunch.')

# def call_customer(fname, lname):
#     time.sleep(3)
#     print(f'Call {fname} {lname}')

# # walk_the_dog()
# # throw_trash()
# # read_email()
# # wash_dishes()

# chore1 = threading.Thread(target = walk_the_dog, args =(dog_name, )) # single args must end with ','
# chore1.start()

# chore2 = threading.Thread(target = throw_trash)
# chore2.start()

# chore3 = threading.Thread(target = read_email)
# chore3.start()

# chore4 = threading.Thread(target = wash_dishes)
# chore4.start()

# chore5 = threading.Thread(target = write_report)
# chore5.start()

# chore6 = threading.Thread(target = do_laundry)
# chore6.start()

# chore7 = threading.Thread(target = buy_lunch)
# chore7.start()

# chore8 = threading.Thread(target = call_customer, args=('Donald', 'Trump')) #args are passed in as a tuple
# chore8.start()

# chore1.join()
# chore2.join()
# chore3.join()
# chore4.join()
# chore5.join()
# chore6.join()
# chore7.join()
# chore8.join()
# print('All chores are complete')

# 51. How to connect to an API using Python
# We will use the pokemon API server
# https://pokeapi.co/api/v2/

# import requests
# base_usl = 'https://pokeapi.co/api/v2/'

# def get_pokemon_info(name):
#     url = f'{base_usl}/pokemon/{pokemon_name}'
#     response = requests.get(url)
#     print(f'Response code is: {response}')

#     if response.status_code == 200:
#         pokemon_data = response.json()    # converts json object into a python dictionary
#         return pokemon_data
#     else:
#         print(f'Failed to retrieve data {response.status_code}')    

# if __name__ == '__main__':
#     pokemon_name = 'pikachu'
#     # pokemon_name = 'typhlosion'
#     pokemon_info = get_pokemon_info(pokemon_name)

#     if pokemon_info:
#         print('-------Pokemon Info--------------')
#         print(f"Name:   {pokemon_info['name'].capitalize()}")
#         print(f"ID:     {pokemon_info['id']}")
#         print(f"Height: {pokemon_info['height']} m")
#         print(f"Weight: {pokemon_info['weight']} kg")

# 52. PyQt5 Intro
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('PyQt5 Template')
#         self.setGeometry(700,300, 800, 500)
#         self.setWindowIcon(QIcon('logo.png'))

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# 53. PyQt5 Labels
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QIcon, QFont
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('PyQt5 Labels')
#         self.setGeometry(200,200, 1500, 700)
#         self.setWindowIcon(QIcon('logo.png'))

#         label = QLabel('Hello World', self)
#         label.setFont(QFont('Roboto', 40))
#         label.setStyleSheet('color:#154c79;' #access hex value fro online color picker
#                             'background-color:lightpink;'
#                             'font-weight: bold;'
#                             'font-style:italic;'
#                             'text-decoration:underline;') 
#         label.setGeometry(70,70,600,400)
#         # label.setAlignment(Qt.AlignTop) # vertically top
#         # label.setAlignment(Qt.AlignBottom) # vertically bottom
#         # label.setAlignment(Qt.AlignVCenter) # vertically center

#         # label.setAlignment(Qt.AlignRight) # horizontally right
#         # label.setAlignment(Qt.AlignLeft) # horizontally left
#         # label.setAlignment(Qt.AlignHCenter) # horizontally center

#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # horizontally center, vert Top
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # horizontally center, vert Bottom
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # horizontally center, vert Center
#         # label.setAlignment(Qt.AlignCenter) # horizontally center, vert Center

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# 54. PyQt5 Images
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QIcon, QPixmap

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('PyQt5 Images')
#         self.setGeometry(200,200, 1500, 700)
#         self.setWindowIcon(QIcon('logo.png'))

#         label = QLabel(self) #self refers to the window object
#         label.setGeometry(0, 0, 500, 500) # x,y,width, height

#         pixmap = QPixmap('Batman.webp')
#         label.setPixmap(pixmap)
#         label.setScaledContents(True)

#         # label.setGeometry(  self.width() - label.width(),      #right. use 0 for left
#         label.setGeometry(  (self.width() - label.width())//2,   # H center, // for integer division
#                             # self.height() - label.height(),    # bottim
#                             (self.height() - label.height())//2, # V center
#                             label.width(), 
#                             label.height()
#                             )

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# 55. PyQt5 Layouts

# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
#                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('PyQt5 Layouts')
#         self.setGeometry(700,300, 800, 500)
#         self.initUI()

#     def initUI(self):
#         central_widget = QWidget() # generic widget
#         self.setCentralWidget(central_widget)

#         label1 = QLabel('Label #1', self)
#         label2 = QLabel('Label #2', self)
#         label3 = QLabel('Label #3', self)
#         label4 = QLabel('Label #4', self)
#         label5 = QLabel('Label #5', self)

#         label1.setStyleSheet('background-color:red;')
#         label2.setStyleSheet('background-color:yellow;')
#         label3.setStyleSheet('background-color:green;')
#         label4.setStyleSheet('background-color:blue;')
#         label5.setStyleSheet('background-color:purple;')

#         # # VERTICAL LAYOUT
#         # vbox = QVBoxLayout()
#         # vbox.addWidget(label1)
#         # vbox.addWidget(label2)
#         # vbox.addWidget(label3)
#         # vbox.addWidget(label4)
#         # vbox.addWidget(label5)
#         # central_widget.setLayout(vbox)

#         # # HORIZONTAL LAYOUT
#         # hbox = QHBoxLayout()
#         # hbox.addWidget(label1)
#         # hbox.addWidget(label2)
#         # hbox.addWidget(label3)
#         # hbox.addWidget(label4)
#         # hbox.addWidget(label5)
#         # central_widget.setLayout(hbox)
        
#         # GRID LAYOUT
#         grid = QGridLayout()
#         grid.addWidget(label1, 0, 0) #widget, row, column
#         grid.addWidget(label2, 0, 1)
#         grid.addWidget(label3, 1, 0)
#         grid.addWidget(label4, 1, 1)
#         grid.addWidget(label5, 2, 2)
#         central_widget.setLayout(grid)

        
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# 56. PyQt5 Buttons
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('PyQt5 Buttons')
#         self.setGeometry(700,300, 800, 500)
#         self.setWindowIcon(QIcon('logo.png'))
#         self.label = QLabel('Hello', self)
#         self.initUI()

#     def initUI(self):
#         self.button = QPushButton('Click me!', self)
#         self.button.setGeometry(150, 200, 200, 100)
#         self.button.setStyleSheet('font-size: 30px;')
#         self.button.clicked.connect(self.on_click)
#         self.button.setText('Clicked') # signal.connect(slot)

#         self.label.setGeometry(150, 300, 300, 100)
#         self.label.setStyleSheet('font-size: 50px;')

#     def on_click(self):
#         self.label.setText('Goodbye!')

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# # 57. PyQt5 Checkboxes
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('PyQt5 CheckBox')
#         self.setGeometry(700,300, 800, 500)
#         self.checkbox = QCheckBox('Do you like some food?', self)
#         self.setWindowIcon(QIcon('logo.png'))
#         self.label = QLabel('Hello', self)
#         self.initUI()

#     def initUI(self):
#         self.checkbox.setGeometry(10, 0, 500, 100)
#         self.checkbox.setStyleSheet('font-size: 30px;'
#                                     'font-family: Roboto;')
#         self.checkbox.setChecked(False)
#         self.checkbox.stateChanged.connect(self.checkbox_changed)

#         self.label.setGeometry(10, 100, 500, 50)
#         self.label.setStyleSheet('font-size: 26px;')

#     def checkbox_changed(self, state): # signal method
#         # print(state)
#         if state == Qt.Checked:
#             self.label.setText('You want some Food')
#         else:
#             self.label.setText('You do NOT want Food')


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# # 57. PyQt5 Radio Buttons
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QRadioButton, QButtonGroup
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('PyQt5 Radio Butons')
#         self.setGeometry(700,200, 800, 700)
#         self.setWindowIcon(QIcon('logo.png'))
#         self.radio1 = QRadioButton('Visa', self)
#         self.radio2 = QRadioButton('Mastercard', self)
#         self.radio3 = QRadioButton('Gift Card', self)
#         self.radio4 = QRadioButton('In Store', self)
#         self.radio5 = QRadioButton('Online', self)
#         self.button_group1 = QButtonGroup(self)
#         self.button_group2 = QButtonGroup(self)
#         self.initUI()

#     def initUI(self):
#         self.radio1.setGeometry(10,0, 300, 50)
#         self.radio2.setGeometry(10,50, 300, 50)
#         self.radio3.setGeometry(10,100, 300, 50)
#         self.radio4.setGeometry(10,150, 300, 50)
#         self.radio5.setGeometry(10,200, 300, 50)

#         self.setStyleSheet("QRadioButton{"
#                             "font-size:38px;"
#                             "font-family:Robot;"
#                             "padding:10px;"
#                             "}")

#         self.button_group1.addButton(self.radio1)
#         self.button_group1.addButton(self.radio2)
#         self.button_group1.addButton(self.radio3)

#         self.button_group2.addButton(self.radio4)
#         self.button_group2.addButton(self.radio5)

#         self.radio1.toggled.connect(self.radio_button_changed)
#         self.radio2.toggled.connect(self.radio_button_changed)
#         self.radio3.toggled.connect(self.radio_button_changed)
#         self.radio4.toggled.connect(self.radio_button_changed)
#         self.radio5.toggled.connect(self.radio_button_changed)

#     def radio_button_changed(self):
#         radio_button = self.sender()
#         if radio_button.isChecked():
#             print(f"{radio_button.text()} is selected")

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# 58. PyQt5 Line Edits(Text Boxes)

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('PyQt5 Radio Butons')
#         self.setGeometry(700,200, 800, 700)
#         self.setWindowIcon(QIcon('logo.png'))
#         self.line_edit= QLineEdit(self)
#         self.button = QPushButton('Submit', self)
#         self.initUI()

#     def initUI(self):
#         self.line_edit.setGeometry(10,10,200,40)
#         self.button.setGeometry(220,10,100,40)
#         self.line_edit.setStyleSheet('font-size:25px;'
#                                     'font-family:Roboto;')
#         self.button.setStyleSheet('font-size:25px;'
#                                     'font-family:Roboto;')
#         self.line_edit.setPlaceholderText('Enter Your Name')                                    
#         self.button.clicked.connect(self.submit)


#     def submit(self):
#         text = self.line_edit.text()
#         print(f"Your name is: {text}")

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


# # 59. PyQt5 CSS

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('PyQt5 Radio Butons')
#         self.setWindowIcon(QIcon('logo.png'))
#         self.button1 = QPushButton('#1')
#         self.button2 = QPushButton('#2')
#         self.button3 = QPushButton('#3')
#         self.initUI()

#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         hbox = QHBoxLayout()
#         hbox.addWidget(self.button1)
#         hbox.addWidget(self.button2)
#         hbox.addWidget(self.button3)

#         central_widget.setLayout(hbox)

#         self.button1.setObjectName('b1')
#         self.button2.setObjectName('b2')
#         self.button3.setObjectName('b3')



#         self.setStyleSheet("""
#             QPushButton {
#                 font-size: 40;
#                 font-family: Roboto;
#                 padding: 15px 75px;
#                 margin: 25px;
#                 border: 3px solid;
#                 border-radius: 35px;
#             }

#             QPushButton#b1 {
#                 background-color: hsl(0, 100, 94);
#             }

#             QPushButton#b2 {
#                 background-color: rgb(0, 240, 0);
#             }

#             QPushButton#b3 {
#                 background-color: blue;
#             }

#             QPushButton#b1:hover {
#                 background-color: hsl(0, 100, 164);
#             }

#             QPushButton#b2:hover {
#                 background-color: pink;
#             }

#             QPushButton#b3:hover {
#                 background-color: yellow;
#             }

#         """)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# 60. Digital Clock Program

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# from PyQt5.QtCore import QTimer, QTime, Qt
# from PyQt5.QtGui import QFont, QFontDatabase

# class DigitalClock(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.time_label = QLabel(self)
#         self.timer = QTimer(self)
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Digital Clock')
#         self.setGeometry(600, 400, 300, 100)

#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)
#         self.setLayout(vbox)

#         self.time_label.setAlignment(Qt.AlignCenter)
#         self.time_label.setStyleSheet("font-size:150px;"
#                                         "color:hsl(111, 250, 100);")
#         self.setStyleSheet('background-color:black;')

#         font_id = QFontDatabase.addApplicationFont('DS-DIGI.TTF')
#         font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#         my_font = QFont(font_family, 150)
#         self.time_label.setFont(my_font)

#         self.timer.timeout.connect(self.update_time) # Connect the timer's timeout signal to the update_time function

#         self.timer.start(1000) # Update every 1 second

#         self.update_time()

#     def update_time(self):
#         current_time = QTime.currentTime().toString('hh:mm:ss AP')
#         self.time_label.setText(current_time)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     clock = DigitalClock()
#     clock.show()
#     sys.exit(app.exec_())

# 61. Stop Watch Program

# from email.charset import QP
# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
#                      QPushButton, QVBoxLayout, QHBoxLayout)
# from PyQt5.QtCore import QTimer, QTime, Qt



# class Stopwatch(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.time = QTime(0,0,0,0) # HOURS, MINS, SECS, MINISECS
#         self.time_label = QLabel('00:00:00:00', self)
#         self.start_button = QPushButton('Start', self)
#         self.stop_button = QPushButton('Stop', self)
#         self.reset_button = QPushButton('Reset', self)
#         self.timer = QTimer(self)
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Stop Watch')

#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)
#         vbox.addWidget(self.start_button)
#         vbox.addWidget(self.stop_button)
#         vbox.addWidget(self.reset_button)

#         self.setLayout(vbox)
#         self.time_label.setAlignment(Qt.AlignCenter)

#         hbox = QHBoxLayout()
#         hbox.addWidget(self.start_button)
#         hbox.addWidget(self.stop_button)
#         hbox.addWidget(self.reset_button)

#         vbox.addLayout(hbox)

#         self.setStyleSheet("""
#             QPushButton, QLabel {
#                 padding:20 px;
#                 font-weight: bold;
#                 font-family: calibri;
#             }
#             QPushButton {
#                 font-size: 50px;
#             }
#             QLabel {
#                 font-size:120px;
#                 background-color:hsl(200,100,85);
#                 border-radius: 20px;
#                 padding:20 px;
#             }
#         """)

#         self.start_button.clicked.connect(self.start)
#         self.stop_button.clicked.connect(self.stop)
#         self.reset_button.clicked.connect(self.reset)
#         self.timer.timeout.connect(self.update_display)

#     def start(self):
#         self.timer.start(10) # 10 milliseconds

#     def stop(self):
#         self.timer.stop() 

#     def reset(self):
#         self.timer.stop() 
#         self.time = QTime(0,0,0,0)
#         self.time_label.setText(self.format_time(self.time))

#     def format_time(self, time):
#         hours = time.hour()
#         minutes = time.minute()
#         seconds = time.second()
#         milliseconds = time.msec() // 10 # integer divide by 10 to remove one dec place

#         return f'{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}'

#     def update_display(self):
#         self.time = self.time.addMSecs(10) 
#         self.time_label.setText(self.format_time(self.time))

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     stopwatch = Stopwatch()
#     stopwatch.show()
#     sys.exit(app.exec_())

# 62. Weather API App
#   https://openweathermap.org/api
#   seanwhs (uname) , pw(hotmail)

# import sys
# from flask import Request
# import requests
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
#                             QLineEdit, QPushButton, QVBoxLayout)
# from PyQt5.QtCore import Qt

# class WeatherApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.city_label = QLabel('Enter City Name: ', self)
#         self.city_input = QLineEdit(self)
#         self.get_weather_button = QPushButton('Get Weather', self) 
#         self.temperature_label = QLabel(self)
#         self.emoji_label = QLabel(self)
#         self.description_label = QLabel(self)
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Weather App')

#         vbox = QVBoxLayout()
#         vbox.addWidget(self.city_label)
#         vbox.addWidget(self.city_input)
#         vbox.addWidget(self.get_weather_button)
#         vbox.addWidget(self.temperature_label)
#         vbox.addWidget(self.emoji_label)
#         vbox.addWidget(self.description_label)

#         self.setLayout(vbox)

#         # Align labels and inputs
#         self.city_label.setAlignment(Qt.AlignCenter)
#         self.city_input.setAlignment(Qt.AlignCenter)
#         self.temperature_label.setAlignment(Qt.AlignCenter)
#         self.emoji_label.setAlignment(Qt.AlignCenter)
#         self.description_label.setAlignment(Qt.AlignCenter)

#         # Set object names to match stylesheet selectors
#         self.city_label.setObjectName('city_label')
#         self.city_input.setObjectName('city_input')
#         self.get_weather_button.setObjectName('get_weather_button')
#         self.temperature_label.setObjectName('temperature_label')
#         self.emoji_label.setObjectName('emoji_label')
#         self.description_label.setObjectName('description_label')

#         # Apply stylesheet 
#         self.setStyleSheet("""
#             QLabel, QPushButton{
#                 font-family: Roboto;
#             }
#             QLabel#city_label{
#                 font-size: 40px;
#                 font-style: italic;
#             }
#             QLineEdit#city_input{
#                 font-size: 40px;
#             }
#             QPushButton#get_weather_button{
#                 font-size: 30px;
#                 font-weight: bold;
#             }
#             QLabel#temperature_label{
#                 font-size: 75px;
#             }
#             QLabel#emoji_label{
#                 font-size: 100px;
#                 font-family: Segoe UI emoji;
#             }
#             QLabel#description_label{
#                 font-size: 50px;
#             }
#         """)

#         # Force update of the UI to reflect the stylesheet
#         self.update()

#         self.get_weather_button.clicked.connect(self.get_weather)

#     def get_weather(self):
#         api_key = '109851312d1edc371da45e773a85752c'
#         city = self.city_input.text()
#         url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

#         try:
#             response = requests.get(url)
#             response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an error status
#             data = response.json()
#             # print(data)

#             if data['cod'] == 200:
#                 self.display_weather(data)

#         except requests.exceptions.HTTPError as http_error:
#             # print(response.status_code) # testing only
#             status_code = response.status_code  # Get the status code from the response
#             match status_code:
#                 case 400:
#                     self.display_error('Bad Request:\nPlease check your input')
#                 case 401:
#                     self.display_error('Unauthorised:\nInvalid API Key')
#                 case 403:
#                     self.display_error('Forbidden:\nAccess is Denied')
#                 case 404:
#                     self.display_error('Not Found:\nCity Not Found')
#                 case 500:
#                     self.display_error('Internal Server Error:\nPlease try again later')
#                 case 502:
#                     self.display_error('Bad Gateway:\nInvalid Response Ftom the Server')
#                 case 503:
#                     self.display_error('Service Unavailable:\nServer is Down')
#                 case 504:
#                     self.display_error('Gateway TimeOut:\nNo Response from the Server')
#                 case _:
#                     self.display_error(f'HTTP Error Occured:\n{http_error}')

                
#         except requests.exceptions.ConnectionError:
#             self.display_error('ConnectionError:\nCheck your internet connection.')    
#         except requests.exceptions.Timeout:
#             self.display_error('Time Out Error:\nRequests Timed Out.')    
#         except requests.exceptions.TooManyRedirects:
#             self.display_error('Too many redirects:\nCheck the url.')    
#         except requests.exceptions.RequestException as req_error:
#             self.display_error(f'Request Error:\n{req_error}')    
        

#     def display_error(self, message):
#         self.temperature_label.setText(message)
#         self.temperature_label.setStyleSheet('font-size:30px')
#         self.emoji_label.clear()
#         self.description_label.clear()


#     def display_weather(self, data):
#         self.temperature_label.setStyleSheet('font-size:75px')
#         # print(data) #testing only
#         temperature_k = data['main']['temp']    #kelvin
#         temperature_c = temperature_k -273.15   #clesius
#         weather_id = data['weather'][0]['id']
#         weather_description = data['weather'][0]['description']
#         self.temperature_label.setText(f'{temperature_c:.0f} degree celsius')
#         self.emoji_label.setText(self.get_weather_emoji(weather_id))
#         self.description_label.setText(weather_description)

#     @staticmethod
#     def get_weather_emoji(weather_id):
#         if 200 <= weather_id <= 232:
#             return ' 🌩️'
#         elif 300 <= weather_id <= 321:
#             return ' 🌧️'
#         elif 500 <= weather_id <= 531:
#             return ' 🌧️'
#         elif 600 <= weather_id <= 622:
#             return ' ❄️'
#         elif weather_id == 762:
#             return ' 🌋'
#         elif weather_id == 771:
#             return ' 🐡'
#         elif weather_id == 781:
#             return ' 🌪️'
#         elif weather_id == 800:
#             return ' 🌞'
#         elif 801 <= weather_id <= 804:
#             return ' 🌥️'
#         else:
#             return ''


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     weather_app = WeatherApp()
#     weather_app.show()
#     sys.exit(app.exec_())


