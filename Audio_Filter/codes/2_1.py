import matplotlib.pyplot as plt

# Define the sequence x(n)
x = [1, 2, 3, 4, 2, 1]
n = range(len(x))  # n = [0, 1, 2, 3, 4, 5]

# Create the plot
plt.stem(n, x)

# Add labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Plot of x(n)')

# Display the plot
plt.grid(True)
plt.savefig('2_1.png')

