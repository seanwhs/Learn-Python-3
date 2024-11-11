# Python from scratch course
# Second hand-on class: Common 3rd party packages
# Nicolas Gutierrez 2023

# The code in this script in separated in cells by concepts.
# This script is meant to be done in a guided way during the class.

# %% Importing libraries
import datetime
import numpy as np

# %%
# One application of the factorization is solving linear systems of equations
# Let's check the difference between doing it inverting the matrix and with pa = lu

A = np.array([[1, 1, 1, 1], 
              [0, 1, 3, -1], 
              [5, -1, 1, 3],
              [1, -1, 2, 4]])
b = [10.5, 28, -1.5, 1.5]

# Matrix inversion
start_time = datetime.datetime.now()
for i in range(1000000):
    A_inverted = np.linalg.inv(A)
    x_slow = np.matmul(A_inverted, b)
time_elapsed = datetime.datetime.now() - start_time

print('Inverting matrix Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

# Linalg solve
start_time = datetime.datetime.now()
for i in range(1000000):
    x = np.linalg.solve(A, b)
time_elapsed = datetime.datetime.now() - start_time

print('Linalg solve Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))