import tkinter as tk
from math import sqrt

# Create the main window
root = tk.Tk()
root.title("Realistic Sphere with Shadow")

# Create a Canvas to draw on
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Sphere parameters (configurable)
center_x, center_y = 200, 200  # Sphere center position
radius = 100  # Sphere radius
sphere_color = "white"  # Sphere color (white)
shadow_color = "#7f8c8d"  # Shadow color
light_direction = (1, -1)  # Direction of light source (x, y)

# Calculate lighting intensity based on light direction and surface normal
def calculate_light_intensity(x, y):
    # Calculate the normal vector of the sphere's surface
    normal_vector = (x - center_x, y - center_y)

    # Avoid division by zero by handling the case when the normal vector has no length
    length = sqrt(sum(comp**2 for comp in normal_vector))
    if length == 0:
        return -1  # Set intensity to -1 for points at the sphere's center
    normal_vector = tuple(comp / length for comp in normal_vector)

    # Calculate dot product of normal and light direction vectors
    dot_product = sum(a * b for a, b in zip(normal_vector, light_direction))

    return dot_product

# Draw the sphere and its shadow
for x in range(center_x - radius, center_x + radius + 1):
    for y in range(center_y - radius, center_y + radius + 1):
        z_squared = radius**2 - (x - center_x)**2 - (y - center_y)**2
        if z_squared >= 0:
            z = sqrt(z_squared)
            intensity = calculate_light_intensity(x, y)
            fill_color = sphere_color if intensity >= 0 else shadow_color
            canvas.create_rectangle(x, y, x+1, y+1, fill=fill_color, outline="")

# Start the Tkinter main loop
root.mainloop()
