import matplotlib.pyplot as plt

# Read data from the text file
with open('2_2.txt', 'r') as file:
    data = file.readlines()
    y = [float(val.strip()) for val in data]

# Create the plot
plt.stem(range(len(y)), y)

# Add labels and title
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Plot of y(n)')

# Display the plot
plt.grid(True)
plt.savefig('2_2.png')
