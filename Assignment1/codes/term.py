import numpy as np
import matplotlib.pyplot as plt

# Define the signal function x(n)
def x_n(n):
    return (40 + 20 * n) * (n >= 0)

# Generate values for n from -2 to 6
n_values = np.arange(-2, 7)

# Calculate corresponding x(n) values
x_values = x_n(n_values)

# Plot the signal
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Plot of x(n) = (40 + 20n)u(n)')
plt.grid(True)
plt.savefig('term.png')

