import numpy as np
import matplotlib.pyplot as plt

# Read data from file
data = np.loadtxt('linspace_y.txt')
t_values = data[:, 0]
y_values = data[:, 1]

# Plot y(t)
plt.plot(t_values, y_values, label='y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Plot of y(t)')
plt.grid(True)
plt.savefig('fig1.png')
