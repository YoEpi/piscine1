import tkinter as tk

# Function to handle button click
def button_click():
    entered_text = entry.get()
    result_label.config(text=f"You entered: {entered_text}")

# Create the main window
root = tk.Tk()
root.title("Tkinter LabelFrame with Entry and Button")

# Create a LabelFrame
label_frame = tk.LabelFrame(root, text="LabelFrame")
label_frame.pack(padx=100, pady=100, fill="both", expand="yes")

# Create a Frame inside the LabelFrame
inner_frame = tk.Frame(label_frame)
inner_frame.pack(padx=100, pady=100)

# Add an Entry (input field) to the inner Frame
entry = tk.Entry(inner_frame)
entry.pack()

# Add a Button to the inner Frame
button = tk.Button(inner_frame, text="Submit", command=button_click)
button.pack()

# Create a Label to display the result
result_label = tk.Label(inner_frame, text="")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()

