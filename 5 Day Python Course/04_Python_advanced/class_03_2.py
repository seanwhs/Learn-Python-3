# Python from scratch course
# Third hand-on class: Python advanced features, second script
# Nicolas Gutierrez 2023

# The code in this script in separated in cells by concepts.
# This script is meant to be done in a guided way during the class.

# %% Importing libraries
# Standard libraries
# Third party libraries
import pandas as pd
import matplotlib.pyplot as plt
# Custom libraries
from plotter import Plotter

# %% Introduction to OOP
# External pdf for
#   Monolithic vs Modular
#   Programming paradigms context explanation.
#   Brief introduction to OOP

# %% Description of a class example class
# We will check together the class Plotter, included in the folder.
# Keyword class and main components
# Useful decorators
# Type hinting and default values
# Explanation of classmethod + properties decorators

student_plotter = Plotter()

print(f"Instance bar_colour: {student_plotter.bar_colour}")
student_plotter.bar_colour = 'g'
print(f"Instance changed bar_colour: {student_plotter.bar_colour}")
print(f"Class bar_colour: {student_plotter.get_bar_colour()}")

# %% Monolithic code example
# 1) Load the file most_efficient_cars.csv
csv_data = pd.read_csv("Cheapestelectriccars-EVDatabase.csv")
# 2) Operate on the file to extract the data we need
csv_data_clean = csv_data.dropna()
# Now we can continue cleanning all columns. Now they are all strings except the number
# of seats. Do not work on the "FastChargeSpeed", we will do that one afterwards
csv_data_clean.loc[:, 'Acceleration'] = csv_data_clean['Acceleration'].apply(lambda x: float(x.split(' ')[0]))
csv_data_clean.loc[:, 'TopSpeed'] = csv_data_clean['TopSpeed'].apply(lambda x: float(x.split(' ')[0]))
csv_data_clean.loc[:, 'Efficiency'] = csv_data_clean['Efficiency'].apply(lambda x: float(x.split(' ')[0]))
csv_data_clean.loc[:, 'Range'] = csv_data_clean['Range'].apply(lambda x: float(x.split(' ')[0]))
csv_data_clean.loc[:, 'PriceinGermany'] = csv_data_clean['PriceinGermany'].apply(lambda x: float(x.replace('€', '').replace(',', '')[0:]))
csv_data_clean.loc[:, 'PriceinUK'] = csv_data_clean['PriceinUK'].apply(lambda x: float(x.replace('£', '').replace(',', '')[0:]))
# Let's do the "FastChargeSpeed" now. This column is tricky, Do you know why?
# We will need a separate function to apply here.
def FastChargeCleaning(x):
    if ' ' in x:
        return float(x.split(' ')[0])
    else:
        return 0

csv_data_clean.loc[:, 'FastChargeSpeed'] = csv_data_clean['FastChargeSpeed'].apply(FastChargeCleaning)

# 3) Store the file cleaned
csv_data_clean.to_csv("most_efficient_cars_cleaned.csv", index=False)

# 4) Create a graph so the efficiency can easily be seen as a bar plot
plt.rcParams['figure.constrained_layout.use'] = True
ax = csv_data_clean.sort_values('Efficiency', ascending=False).plot.bar(x='Name', y='Efficiency', rot=90, figsize=(3*6.4, 4.8))
ax.set_ylabel("Efficiency")
plt.savefig("Pandas_bar_plot_efficiency.png", dpi=350)

# %% Introduction to PyCharm
#   Opening, loading a project.
#   Project view
#   Menus
#   Selection of interpreter
#   Splitting the window
#   Running code

# %% In PyCharm move the Monolithic example to OOP
# 1) Think about the encapsulated groups of operations you will need
# 1 - for loading the file.
# 2 - Processing
# 3 - Storing
# 4 - Plotter
# 2) Create a main.py -> with the operations
# 3) Create a many classes as you decide in step 1.
# 4) Run your code

