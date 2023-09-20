import matplotlib.pyplot as plt
# Data
x = [0, 1, 2, 3]
y = [12, 32, 42, 52]

# Create a scatter plot
plt.scatter(x, y, label='Data Points')

# Set axis labels and title
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Scatter Plot of Points')

# Display grid lines
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()