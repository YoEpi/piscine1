import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Animated Stickman Figure")

# Create a Canvas to draw on
canvas = tk.Canvas(root, width=200, height=300)
canvas.pack()

# Initial coordinates for the stickman's limbs
limb_coordinates = [100, 60, 70, 100, 100, 60, 130, 100]

# Draw the stickman's head (a circle)
head = canvas.create_oval(80, 20, 120, 60, fill="gray")

# Draw the stickman's body (a line)
body = canvas.create_line(100, 60, 100, 150, fill="black", width=3)

# Draw the stickman's limbs (lines)
left_arm = canvas.create_line(*limb_coordinates[:4], fill="black", width=3)
right_arm = canvas.create_line(*limb_coordinates[4:], fill="black", width=3)
left_leg = canvas.create_line(100, 150, 70, 200, fill="black", width=3)
right_leg = canvas.create_line(100, 150, 130, 200, fill="black", width=3)
plus_leg = canvas.create_line(100, 150, 90, 200, fill="red", width=3)

# Add text near the stickman's head
text = canvas.create_text(100, 10, text="Hello, Stickman!", fill="black")

# Function to animate the stickman
def animate_stickman():
    # Update the coordinates to move the arms up and down
    limb_coordinates[1], limb_coordinates[3], limb_coordinates[5], limb_coordinates[7] = (
        limb_coordinates[3], limb_coordinates[1], limb_coordinates[7], limb_coordinates[5]
    )

    # Update the position of the limbs
    canvas.coords(left_arm, *limb_coordinates[:4])
    canvas.coords(right_arm, *limb_coordinates[4:])

    # Schedule the next animation frame after 500 milliseconds (0.5 seconds)
    canvas.after(50, animate_stickman)

# Start the animation loop
animate_stickman()

# Start the Tkinter main loop
root.mainloop()
