import tkinter as tk
from math import sqrt

# Create the main window
root = tk.Tk()
root.title("Realistic Sphere")

# Create a Canvas to draw on
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Sphere parameters (configurable)
center_x, center_y = 200, 200  # Sphere center position
radius = 100  # Sphere radius
color = "#3498db"  # Sphere color (e.g., blue)
shadow_color = "#7f8c8d"  # Shadow color
light_direction = (1, -1, 1)  # Direction of light source (x, y, z)

# Calculate lighting intensity based on light direction and surface normal
def calculate_light_intensity(x, y):
    # Calculate the normal vector of the sphere's surface
    normal_vector = (x - center_x, y - center_y, sqrt(radius**2 - (x - center_x)**2 - (y - center_y)**2))

    # Normalize the normal vector
    length = sqrt(sum(comp**2 for comp in normal_vector))
    normal_vector = tuple(comp / length for comp in normal_vector)

    # Calculate dot product of normal and light direction vectors
    dot_product = sum(a * b for a, b in zip(normal_vector, light_direction))
    
    # Normalize the dot product to the range [0, 1]
    normalized_intensity = (dot_product + 1) / 2

    return normalized_intensity

# Draw the sphere
for x in range(center_x - radius, center_x + radius):
    for y in range(center_y - radius, center_y + radius):
        distance = sqrt((x - center_x)**2 + (y - center_y)**2)
        if distance <= radius:
            intensity = calculate_light_intensity(x, y)
            fill_color = color if intensity >= 0.3 else shadow_color
            canvas.create_rectangle(x, y, x+1, y+1, fill=fill_color, outline="")

# Start the Tkinter main loop
root.mainloop()
