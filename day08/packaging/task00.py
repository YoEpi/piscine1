import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Game GUI")

# Create a Frame for the game canvas
game_frame = tk.Frame(root, width=800, height=600, bg="black")
game_frame.pack()

# Create a Canvas for the game graphics
game_canvas = tk.Canvas(game_frame, width=800, height=600, bg="white")
game_canvas.pack()

# Create a Score Label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 16))
score_label.pack()

# Create a Time Label
time_label = tk.Label(root, text="Time: 0:00", font=("Arial", 16))
time_label.pack()

# Create a Life Bar
life_bar = tk.Canvas(root, width=200, height=30, bg="white")
life_bar.pack()

# Create an Inventory Frame
inventory_frame = tk.Frame(root, width=800, height=100, bg="gray")
inventory_frame.pack()

# Create Inventory Items (e.g., buttons)
item1_button = tk.Button(inventory_frame, text="Item 1")
item1_button.pack(side=tk.LEFT)
item2_button = tk.Button(inventory_frame, text="Item 2")
item2_button.pack(side=tk.LEFT)
item3_button = tk.Button(inventory_frame, text="Item 3")
item3_button.pack(side=tk.LEFT)

# Create a Menu Button
menu_button = tk.Button(root, text="Menu", font=("Arial", 16), command=lambda: print("Menu clicked"))
menu_button.pack()

# Start the Tkinter main loop
root.mainloop()
