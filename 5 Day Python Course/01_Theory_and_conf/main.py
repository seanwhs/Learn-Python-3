# Imports
import math
import sys

# Checking Python Current version
print(f"Python Current version: {sys.version}")

# User Inputs
string_to_print = "Hello world"
list_of_text = ["This is a\n", "test\n", "for storing text in a file\n"]
text_file_name = "testfile.txt"

# Some first basic commands in Python
print(string_to_print)

with open(text_file_name, "w") as file:
    file.writelines(list_of_text)

with open(text_file_name, "r") as file:
    read_from_file = file.read()

print(read_from_file)

for i in range(len(list_of_text)):
    print(list_of_text[i])

# Easy application of math package
print(f"Number pi in Python: {math.pi}")

# Run this script from the console to test how easy it is