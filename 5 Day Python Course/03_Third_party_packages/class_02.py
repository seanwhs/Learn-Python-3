# Python from scratch course
# Second hand-on class: Common 3rd party packages
# Nicolas Gutierrez 2023

# The code in this script in separated in cells by concepts.
# This script is meant to be done in a guided way during the class.

# %% Installation of libraries

# Bare Python is a bit limited on its own. That limitation anyway is easy to mitigate, 
# by installing and importing any third party packages. The most common ones for 
# engineers are the following:

# Numpy (https://numpy.org/) -> Scientific computing and numeric operations
# (Coming from Matlab -> https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
# Scipy (https://scipy.org/) -> Algorithms for scientific computing
# Matplotlib (https://matplotlib.org/) -> Visualizations
# Pandas (https://pandas.pydata.org/) -> Data analysis and manipulation

# The package manager in python is pip, to install something you will need open a 
# python console and use the command pip install PACKAGE (Careful with the name of 
# packages because sometimes they are a bit confusing, the best way of doing is checking 
# in google first how to install a package). 
# In this case we will use pipenv as a package manager. As we discussed previously,
# pipenv allows the installation of a package in a virtual environment.

# 1) So if in windows, click windows key and write cmd and the press enter.
# 2) in the console, navigate to the folder where you have the files and you want to create
# your virtual environment. 
# 3) pipenv shell and enter. This will create a virtual environment linked to that folder.
# 4) now it is the moment to install all packages:
# 4.1) pipenv install numpy
# 4.2) pipenv install scipy
# 4.3) pipenv install matplotlib
# 4.4) pipenv install pandas
#__ Following is an auxiliary for an example
# pipenv install pooch

# If you want to check the current packages that you have install: pipenv graph

# Can you doublecheck all the packages installed are there?

#%% Importing libraries
# Now that we have installed all the required libraries, it is not enough yet, we need
# to import them to be available during the session, you can do that using the command
# import


# Standard libraries
# Third party libraries
## Complete here with imports for all libraries (leave the following untouched, the func_aux)
# Custom libraries
from func_aux import scatter_plot
from func_aux import line_plot
from func_aux import line_plot_for_electro_fft

# Why do we import in the beginning of scripts?
# In case of having libraries from python, third party and custom, what you believe 
# is the recommended order? 

# %% Numpy Interpolation
# Interpolation is a very common application in engineering that allows us "estimate"
# values in between measures.

# Look for a function in numpy to create a vector of certain amount of components and 
# complete the following x_sin variable definition
x_sin = np.linspace(0, 2*np.pi, 10)
y_sin = ## Complete here

# Use the same function you used below in the x_interpolate below
x_interpolate = np.linspace(0, 2*np.pi, 20)
# Look for and use a function to interpolate the values
y_interpolate = ## Complete here 

# The following line is a function created for you just for this example
scatter_plot([x_sin, x_interpolate], [y_sin, y_interpolate], file_name="sin_interpolation_example")

# %% Numpy Derivation
# Derivation is very common as well, when doing it in a computer is numerical
# derivation. The derivative is the slope between of two points: vertical increment 
# divided by horizontal increment
x_sin = np.linspace(0, 2*np.pi, 100)
y_sin = ## Complete here 

vertical_increment = ## Complete here 
horizontal_increment = ## Complete here 
y_derivative = vertical_increment / horizontal_increment

# The following line is a function created for you just for this example
scatter_plot([x_sin, x_sin], [y_sin, y_derivative], file_name="sin_derivation_example")

# %% Numpy Integration
# The integral of a 1D time series is the area below the curve.
x_lin = np.linspace(0, 10, 1000)
y_lin = ## Complete here 

y_integration = np.zeros_like(x_lin)
for i in range(len(x_lin)):
    y_integration[i] = ## Complete here 

area_below = ## Complete here 

scatter_plot([x_lin, x_lin], [y_lin, y_integration], file_name="lin_integration_example")

# %% Numpy Eigenvalues and eigenvectors
# Look for an order in Numpy to form a unity matrix of any shape (>=3)
# TIP: you can use two orders actually, array and matrix

mat_eig = ## Complete here
# mat_eig = np.matrix('1 0 0; 0 1 0; 0 0 1')

# Look for the order to get the eigenvalues and eigenvectors of a matrix
## Complete here
w, v = ## Complete here

# %% Numpy Singular Value Decomposition
# It is a factorization of a matrix in the sense M = UΣV*
# It is similat to finding the eigenvalues and eigenvectors of a matrix, but it works for
# any matrix, even if it is not square.

mat_svd = np.array([[1, 0, 0, 0, 2],
                    [0, 0, 3, 0, 0],
                    [0, 0, 0, 0, 0], 
                    [0, 2, 0, 0, 0]])

# Find the order in numpy to do a Singular Value Decomposition of matrix b
## Complete here
u, s, vh = ## Complete here

# %% Numpy linalg solve
# This order allow solving linear equation systems in the sense Ax = b
# Generate matrix A and vector b so they define the following system:
# 3*x_0 + x_1 + 2*x_2 = 11
# x_0 + x_1 + x_2 = 6
# 2*x_0 - 2*x_1 + 5*x_2 = 13


A = ## Complete here
b = ## Complete here

x = ## Complete here

# %% Store your results to continue later
file_name = "numpy_variables.npz"
# Look for a function to store the vectors:
# x_interpolate,
# x_lin,
# x_sin,
# y_derivative
# y_integration
# y_interpolate
## Complete here

# Look for the function to load the file_name
npzfile = ## Complete here
print(npzfile.files)

# TIP: Shelve or pickle might be useful for storing workspaces

# %% Scipy minimization-optimization
# Scipy has several minimizer routines to use depending on the problem on hand. In this
# case we will try to check if the curve we got in the example of Numpy integration is
# a cuadratic.

# 1) We are going to need a polynomial function:
def polynomial_minimization(params, x_real):
## Complete here

# 2) Then, we will need an error function (MAE?)
def error_function(y_real, y_estimation):
## Complete here

# 3) Next, we will define a wrapper function that will contain both previously defined
def wrapper_function(params, arguments):
## Complete here

# 3) Now we will an initial iterant
initial_iterant = [0, 1, 1, 0]

# 4) Finally we will set up our optimizer
minimization_solution = ## Complete here(wrapper_function, 
                                                initial_iterant,
                                                args=[x_lin, y_integration],
                                                method='nelder-mead',
                                                options={'xatol': 1e-8,
                                                         'disp': True})

print(f"The solution found by the method is {minimization_solution.x}")
y_approximation = polynomial_minimization(minimization_solution.x, x_lin)
scatter_plot([x_lin, x_lin], [y_integration, y_approximation], file_name="minimization_example")

# %% Scipy PA = LU matrix decomposition
# PA = LU matrix decomposition is very handy for several lineal problems.
## Check how to do this on Scipy. 
p, l, u = ## Complete here

# %% Scipy fft
# Let's download first a dataset for an electrocardiogram (sampling frequency = 360Hz)
electrocardiogram_data = scipy.datasets.electrocardiogram()
time = np.arange(electrocardiogram_data.size) / 360

line_plot([time], [electrocardiogram_data], file_name="electrocardiogram_data")

# Let's calculate the fft now
N = len(electrocardiogram_data)
T = 1.0 / 360
yf = ## Complete here
xf = ## Complete here

yf_to_plot = 2.0/N * np.abs(yf[0:N//2])
line_plot_for_electro_fft([xf], [yf_to_plot], file_name="electrocardiogram_data")

# Let's clean this a bit using a hanning window in scipy
hanning_window = ## Complete here
electro_windowed = electrocardiogram_data * hanning_window

yf = ## Complete here
xf = ## Complete here

yf_to_plot = 2.0/N * np.abs(yf[0:N//2])
line_plot_for_electro_fft([xf], [yf_to_plot], file_name="electrocardiogram_data_hanning")

# Let's clean a bit the signal by removing high frequency noise
sos = scipy.signal.butter(6, 10, 'lowpass', fs=360, output='sos')
filtered = scipy.signal.sosfilt(sos, electro_windowed)

yf = scipy.fft.fft(filtered)
yf_to_plot = 2.0/N * np.abs(yf[0:N//2])
line_plot_for_electro_fft([xf], [yf_to_plot], file_name="electrocardiogram_data_hanning_filtered")


# %% Scipy numeric quadrature
# Another example of numeric integration, this time using scipy package
f = lambda x: x
area_below_x = ## Complete here

# Being a so easy function, what geometric figure resembles the are below the curve when
# starting in 0? How far is the numeric integration from analytical one.

# %% Scipy interp1d
x_sin = np.linspace(0, 2*np.pi, 10)
y_sin = np.sin(x_sin)
x_interpolation = np.linspace(0, 2*np.pi, 100)

# Let's use a linear interpolation
interpolation_function = ## Complete here
y_interpolation = interpolation_function(x_interpolation)
scatter_plot([x_sin, x_interpolation], [y_sin, y_interpolation], file_name="scipy_interpolation_linear")

# Let's move to a cuadratic one and see if it improves
interpolation_function = ## Complete here
y_interpolation = interpolation_function(x_interpolation)
scatter_plot([x_sin, x_interpolation], [y_sin, y_interpolation], file_name="scipy_interpolation_quadratic")

# And a cubic
interpolation_function = ## Complete here
y_interpolation = interpolation_function(x_interpolation)
scatter_plot([x_sin, x_interpolation], [y_sin, y_interpolation], file_name="scipy_interpolation_cubic")

# %% ODE45 like functions
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html

# %% Matplotlib plot
# Matplotlib stands for MATlab like PLOTting LIBrary. It is quite powerful and it has 
# many plots that can be used. Let's start with the standard line plot.

# 1) You can plot something quite easily, directly indicating the variable.
# With just one variable, it is assumed it is a dependent variable, and the independent
# is assumed to be the index.
## Look for the code for plotting and plot using just one input.
## Complete here

# 2) Normally you like having more options instead. Now we will create first the figure 
# and plot with two variables and let's include xlabel, ylabel and title.
## Complete here

# 3) In case you want to store the figure, how would do it?
## Complete here

# %% Matplotlib scatter 
# Scatter plots are used when we have noisy variables or point clouds and we don't lines
# joining them.

# 1) Look for an order in matplotlib to create a scatter plot.
## Complete here

# 2) Let's work with the colors and the markers. Let's move the color to green and the 
# marker to a triangle pointing upwards.
## Complete here

# %% Matplotlib bar plot
# Look for an order in matplotlib to use the bar plot. 
## Complete here

# %% Matplotlib composed plot
# Let's complicate now the things a bit more doing a composition plot. Matplotlib can
# compose different plots into one, by means of the order subplots.
plt.rcParams['figure.constrained_layout.use'] = True
fig = plt.figure()
gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, :])

## Complete here for ax1

## Complete here for ax2

## Complete here for ax3

plt.rcParams['figure.constrained_layout.use'] = False

# %% Pandas load csv and describe
# *DataFrame obtained from: https://www.kaggle.com/datasets/kkhandekar/cheapest-electric-cars
# Have a look at the csv in this folder first.

# Pandas uses dataframes as a built-in data type. DataFrames are very handy to be used as 
# a table. Filtering and processing the data is quite easy.

# Load the csv with Pandas
csv_data = pd.read_csv("Cheapestelectriccars-EVDatabase.csv")
# Look for useful functions to describe the data on it
summary = ## Complete here

# What happen? The summary is not great, do you know why?

# %% Pandas create new columns
# To create a new column, you will need a name that is a not a column already. Let's list
# the columns that we have so far.
print(## Complete here)

# Then you will need a list, np array or vector with the same lenght as the current
# dataframe. Check the size of the data frame first, then generate a vector and create
# a new column
length_of_dataframe = 
new_column = 

csv_data["new_column"] = new_column

# %% Pandas cleaning dataframe
# Let's start by removing the NaN.
csv_data_clean = ## Complete here

# Now we can continue cleanning all columns. Now they are all strings except the number
# of seats. Do not work on the "FastChargeSpeed", we will do that one afterwards
csv_data_clean.loc[:, 'Acceleration'] = ## Complete here
csv_data_clean.loc[:, 'TopSpeed'] = ## Complete here
csv_data_clean.loc[:, 'Efficiency'] = ## Complete here
csv_data_clean.loc[:, 'Range'] = ## Complete here
csv_data_clean.loc[:, 'PriceinGermany'] = ## Complete here
csv_data_clean.loc[:, 'PriceinUK'] = ## Complete here

# Let's do the "FastChargeSpeed" now. This column is tricky, Do you know why?
# We will need a separate function to apply here.
def FastChargeCleaning(x):
    if ' ' in x:
        return float(x.split(' ')[0])
    else:
        return 0

csv_data_clean.loc[:, 'FastChargeSpeed'] = csv_data_clean['FastChargeSpeed'].apply(FastChargeCleaning)

# %% Pandas filtering
# Filtering DataFrames by a column is easy, we just need to implement the selection 
# criteria and apply it to the data frame.
# Let's find the most efficient cars with Efficienty higher than 200 and order the 
# dataframe ascending by Efficiency.

most_efficient_cars = ## Complete here

# %% Pandas storing a file
# Once we have the required csv, storing it into a csv again is quite easy. 
# Let's find the method to do so

## Complete here


# %% Scipy stats gaussian
# Check scipy stats, look for a guassian distribution and find the method to return the
# percent point function.
# Create a vector of 100 components between the points 1 and 99%.
## Complete here
x = np.linspace(,
                , 100)

# Now let's find the probability density function, and use it to get the probability
# of every x before.
probability_of_x_gaussian = ## Complete here

# Now, plot x and probality of x gaussian and check that effectively it is a gaussian
fig, ax = plt.subplots(1, 1)
ax.plot(x, probability_of_x_gaussian, 
        'r-', lw=5, alpha=0.6, label='norm pdf')

# Did you see the inputs loc and scale? Do you know what do they mean? 

# %% Scipy stats gamma
# Can you repeat the same steps above for a gamma distribution?