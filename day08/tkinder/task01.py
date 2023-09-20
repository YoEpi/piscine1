import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk

# Function to handle the button click
def button_click():
    entered_text = entry.get().upper()
    print(entered_text)

# Create the main window
root = tk.Tk()
root.title("Tkinter LabelFrame with Entry, Canvas, and Buttons")

# Create a LabelFrame
label_frame = tk.LabelFrame(root, text="LabelFrame")
label_frame.pack(padx=10, pady=10, fill="both", expand="yes")

# Create a Frame inside the LabelFrame
inner_frame = tk.Frame(label_frame)
inner_frame.pack(padx=10, pady=10)

# Create a Canvas inside the inner Frame
canvas = Canvas(root, width=400, height=600)
canvas.pack()

# Load and display the background image on the Canvas
background_image = Image.open("img.png")  # Replace with your image file
background_image = ImageTk.PhotoImage(background_image)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Add an Entry (input field) to the inner Frame
entry = tk.Entry(inner_frame)
entry.pack()

# Add a Button to the inner Frame (prints content in UPPERCASE)
button_upper = tk.Button(inner_frame, text="Print UPPERCASE", command=button_click)
button_upper.pack()

# Add a Button below the input field (closes the window)
button_exit = tk.Button(label_frame, text="Exit", command=root.destroy)
button_exit.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
