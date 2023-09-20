import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Stickman Figure")

# Create a Canvas to draw on
canvas = tk.Canvas(root, width=200, height=300)
canvas.pack()

# Draw the stickman's head (a circle)
head = canvas.create_oval(80, 20, 120, 60, fill="gray")

# Draw the stickman's body (a line)
body = canvas.create_line(100, 60, 100, 150, fill="black", width=3)

# Draw the stickman's limbs (lines)
left_arm = canvas.create_line(100, 60, 70, 100, fill="black", width=3)
right_arm = canvas.create_line(100, 60, 130, 100, fill="black", width=3)
left_leg = canvas.create_line(100, 150, 70, 200, fill="black", width=3)
right_leg = canvas.create_line(100, 150, 130, 200, fill="black", width=3)
right_leg = canvas.create_line(100, 150, 90, 200, fill="red", width=3)


# Add text near the stickman's head
text = canvas.create_text(100, 10, text="Hello, Stickman!", fill="black")

# Start the Tkinter main loop
root.mainloop()
