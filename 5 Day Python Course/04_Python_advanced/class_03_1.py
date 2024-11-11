# Python from scratch course
# Third hand-on class: Python advanced features
# Nicolas Gutierrez 2023

# The code in this script in separated in cells by concepts.
# This script is meant to be done in a guided way during the class.

# %% Importing libraries
# Standard libraries
import re
import functools
import time
# Third party libraries
import numpy as np

# %% List Comprehensions
# It allows poweful functionality within a single line of code.
# Main uses are:
    # List Creation
    # Filtering
    # Mapping
# https://realpython.com/list-comprehension-python/
# Sometimes the list comprehension is faster, check the end of the

# 1) Let's load the file "Cheapestelectriccars-EVDatabase.csv" using just Python functions
file = ## Complete here
file_per_lines = file.readlines()
file.close()

# 2) Use list comprehensions for splitting every line into its concepts
file_separated = ## Complete here

# 3) Filter the file so we get just the Audis
# TIP: How long is this list? There should be 17 Audi lines
audi_data = ## Complete here

# 4) Filter columns with no price (neither Germany or UK)
# 4.1) TIP: Check the number of commas per file.
number_of_commas_per_line = ## Complete here
no_price_removed_list = ## Complete here

# 5) Would you be able to find the most expensive car in euros in one line?
# TIPS:
# Start by creating a regular expresion so you can capture the price
# Get a list of prices as ints
# Find the index of the maximum value (you can use np.argmax here)
# Get the line with the above index
# Split the line so you can get the name of the car
most_expensive_car = ## Complete here

# %% Context managers
# It handles automatically set up and teardown functions. It creates an isolated 
# space with certain rules that are freed when the lines inside are finished.
# Normally they are used with files or APIs or external resources.
# https://realpython.com/python-with-statement/

# Use a context manager to open a file with write permissions and write something.
## Complete here

# Use a context manager to open the file in the list comprehensions example in point 1
## Complete here

# %% Type hinting
# Python is a dynamically typed language, which is good and flexible and bad and error
# prone at the same time. This is deep into Python conception and cannot be changed,
# but in order to detect errors and make it more readible, type hinting is recommended.
# Additionally, other more advanced IDEs can highlight if there is a mismatch of data types.
# Check the example below
def multiplication(a: float, b: float) -> float:
    c = b * a
    return c

# Can you do the same with other built in types? 
def multiplication_list(a: list, b: list) -> list:
    c = []
    for i in range(len(a)):
        c.append(b[i] * a[i])
    return c

# Would you specify the type inside a collection type? How would you do that?
from typing import List, Tuple, Dict, Union
def multiplication_list_type_cast(a: Union[List[float], float], b: Union[List[float], float]) -> List[float]:
    c = []
    for i in range(len(a)):
        c.append(b[i] * a[i])
    return c

# %% Logging
# Many times project start with showing something on the screen with a simple print 
# statement. This is handy, but not very elegant and does not allow many options. 
# Python has the logging library for this.
## Complete here with the corresponding import

# Look for the getLogger function
logger = ## Complete here

# Set the minimum level of your logger
logger.setLevel(logging.DEBUG)

# The following code is a tip that you should include to avoid repeating handlers
if logger.hasHandlers():
    logger.handlers.clear()

# Below you can see how to manage a stream handler
screen_handler = ## Complete here
screen_handler.setLevel(logging.INFO)

# Can you look for a FileHandler in the help of logging?
file_handler = ## Complete here
file_handler.setLevel(logging.DEBUG)

# One of the advantages of logging is that allows including certain format by means of
# formatters, can you check the documentation for the formatters.
# TIP: Remember you need to define a formatter and associate it with your handler
formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
screen_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Finally we add the handlers as follows
logger.addHandler(screen_handler)
logger.addHandler(file_handler)

# Now use your logger to log messages as info, debug, warning and error
logger.info("Testing message!")
logger.debug("Testing message!")
logger.warning("Testing message!")
logger.error("Testing message!")

# %% Decorators
# They wrap a function, modifying its behavior.
# https://realpython.com/primer-on-python-decorators/

# Ad hoc decorators
def repeat(_func=None, *, num_times=1):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

# Create a function to multiply two matrices and use the timer and repeat decorators
@timer
@repeat(num_times=100000)
def multiply_two_matrices(A, B):
    C = np.matmul(A, B)
    return C

A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

C = multiply_two_matrices(A, B)

# Standard decorators are as follows
# @properties -> Getters and setters of attributes of the class
# @staticmethod -> They cannot modify object state of class state
# @classmethod -> Can modify the class attributes of all classes instantiated.

# We will see them in action in the next script
