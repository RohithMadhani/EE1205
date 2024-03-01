import numpy as np
import matplotlib.pyplot as plt

# Define the function
def y(x):
    return (3 - 2*x)*np.exp(-0.5*x) * (x >= 0)

# Read data from file
with open("linspace.txt", "r") as file:
    x_values = [float(line.strip()) for line in file]

# Calculate y values
y_values = y(np.array(x_values))

# Plot the function
plt.plot(x_values, y_values, label='y(x)')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Plot of y(x)')
plt.grid(True)
plt.savefig('fig1.png')
