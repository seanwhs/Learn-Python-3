# Python from scratch course
# First hand-on class: Python Basics
# Nicolas Gutierrez 2023

# The code in this script in separated in cells by concepts.

# %% Standard libraries import
# Bare Python has some interesting libraries on its own:
# math -> mathematical operations
# os -> operations on files, filepaths and operative system related.
# glob -> a bit more powerful than os for searching folders.
# json -> native library to handle and open json files.

## Complete here importing the previous described libraries

# %% Math
# https://docs.python.org/3/library/math.html
# Pi number
pi_number = ## Complete here
print(f"Pi number in bare Python: {pi_number:.4f}")

# Operations
value_to_ceil = 3.4
ceil_rounding = ## Complete here
print(f"Ceil of number {value_to_ceil} is {ceil_rounding}")

value_to_floor = 4.5
floor_rounding = ## Complete here
print(f"Floor of number {value_to_floor} is {floor_rounding}")

value_for_factorial = 10
factorial_calculation = ## Complete here
print(f"Factorial of {value_for_factorial} is {factorial_calculation}")

value_to_sqrt = 4
sqrt_calculation = ## Complete here
print(f"Square root of {value_to_sqrt} is {sqrt_calculation}")

# Trigonometric functions
point_1 = (1, 1)
point_2 = (0, 0)
distance_between_points = ## Complete here
print(f"Distance between {point_1} and {point_2} is {distance_between_points}")

radians = 2*math.pi
cosine_value = ## Complete here
print(f"Cosine of {radians} is {cosine_values}")

radians = 2*math.pi
sine_value = ## Complete here
print(f"Sine of {radians} is {sine_values}")

radians_to_degrees = math.pi
value_in_degrees = ## Complete here
print(f"{radians_to_degrees} radians is {value_in_degrees} degrees")


# %% OS
# https://docs.python.org/3/library/os.html
# Operating System dependent functionality
current_working_directory = ## Complete here
print(f"Current working directory is: {current_working_directory}")

# Creation of folders
folder_name_to_create = ## Complete here
## Complete here, there are two options, one is handier as it ignores if it already exists

# Remove, removedirs
## Complete here

# Change the name of a file
## Complete here

# Stats of a file
## Complete here

# Handy separator of folders in the system:
separator = ## Complete here
print(f"The folder separator here is: {separator}")

# Join folder name and file name
folder_name = "Here"
file_name = "we_go.txt"
join_of_both = ## Complete here
print(f"Joining {folder_name} with {file_name} we get {join_of_both}")

# %% Glob
# https://docs.python.org/3/library/glob.html
# Find pathnames with specified pattern
path_pattern = "*.py"
files_with_pattern = ## Complete here
print(f"Files found with pattern {path_pattern} are {files_with_pattern}")

# %% Json
# https://docs.python.org/3/library/json.html
# Json is a very famous file type used in many codes. Python support it natively.

# Create a dictionary with several layers of data
dict_for_json = {"first_layer": {"second_layer": [5,6,7]}}

# Use an order to store the dict_for_json_to the drive (a context manager is recommended)
## Complete here

# Use an option to load again the json from disc (a context manager is recommended)
## Complete here

