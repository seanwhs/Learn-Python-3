# Python from scratch course
# Auxiliary functions for Python course
# Nicolas Gutierrez 2023

# Standard libraries
# Third party libraries
import matplotlib.pyplot as plt
# Custom libraries

MARKER_LIST = ["o", "s", "^", "v", "p"]

def scatter_plot(x_variables: list, y_variables: list, file_name="x_vs_y"):
    # Input variable checking
    if len(x_variables) != len(y_variables):
        raise Exception("Size of inputs is different.")
    
    # Initial definitions
    file_extension = ".png"
    
    # Plotting
    plt.figure()
    for i in range(len(x_variables)):
        plt.scatter(x_variables[i], y_variables[i], 
                    label=f"Variable {i+1}",
                    marker=MARKER_LIST[i%len(MARKER_LIST)])
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.legend()
    plt.title(file_name)
    
    if not file_name.endswith(file_extension):
        file_name = file_name + file_extension
    
    plt.savefig(file_name, dpi=250)
    
def line_plot(x_variables: list, y_variables: list, file_name="x_vs_y"):
    # Input variable checking
    if len(x_variables) != len(y_variables):
        raise Exception("Size of inputs is different.")
    
    # Initial definitions
    file_extension = ".png"
    
    # Plotting
    plt.figure()
    for i in range(len(x_variables)):
        plt.plot(x_variables[i], y_variables[i], label= f"Variable {i+1}")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.legend()
    plt.title(file_name)
    
    if not file_name.endswith(file_extension):
        file_name = file_name + file_extension
    
    plt.savefig(file_name, dpi=250)
    
def line_plot_for_electro_fft(x_variables: list, y_variables: list, file_name="x_vs_y"):
    # Input variable checking
    if len(x_variables) != len(y_variables):
        raise Exception("Size of inputs is different.")
    
    # Initial definitions
    file_extension = ".png"
    
    # Plotting
    plt.figure()
    for i in range(len(x_variables)):
        plt.plot(x_variables[i], y_variables[i], label= f"Variable {i+1}")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Y values")
    plt.legend()
    plt.title(file_name)
    plt.ylim([0, 0.05])
    plt.xlim([0, 20])
    
    if not file_name.endswith(file_extension):
        file_name = file_name + file_extension
    
    plt.savefig(file_name, dpi=250)