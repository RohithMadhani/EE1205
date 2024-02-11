import numpy as np
import matplotlib.pyplot as plt

# Define the signal function y(n)
def y_n(n):
    return (50 * n + 10 * n**2) * (n >= 0)

# Generate values for n from -2 to 10
n_values = np.arange(-2, 11)

# Calculate corresponding y(n) values
y_values = y_n(n_values)

# Highlight stem when n = 6
highlight_index = np.where(n_values == 6)[0][0]

# Plot the signal
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.stem(n_values[highlight_index], x_values[highlight_index], linefmt='g-', markerfmt='go', basefmt='r-')  # Highlight stem
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Plot of y(n) = (50n + 10n^2)u(n)')
plt.grid(True)
plt.savefig('Sum.png')
