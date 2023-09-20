import tkinter as tk

# create the function to draw teh stick man
def draw_stickman(canvas):
    # body
    canvas.create_line(50, 100, 50, 35, fill="black", width=4)
    canvas.create_line(50, 50, 20, 60, fill="black", width=2)
    canvas.create_line(50, 50, 65, 45, fill="black", width=2)
    # canvas.create_line(65, 45, 75, 22, fill="black", width=2)
    canvas.create_line(50, 100, 20, 140, fill="black", width=3)
    canvas.create_line(50, 100, 70, 140, fill="black", width=3)
    canvas.create_oval(40, 15, 60, 35, fill="black")


def animate_line(canvas, line_id, x1, y1, x2, y2, speed):

    canvas.coords(line_id, x1, y1, x2, y2)

    x2 += speed
    y2 += speed

    canvas.coords(line_id, x1, y1, x2, y2)

    canvas.after(100, animate_line, canvas, line_id, x1, y1, x2, y2, speed)



# Create the main window
root = tk.Tk()
root.title("StickMan")

# create the canvas
canvas= tk.Canvas(root, width=100, height=150)
canvas.pack()

draw_stickman(canvas)

line = canvas.create_line(65, 45, 75, 22, fill="black", width=2)

animate_line(canvas, line, 65, 45, 80, 30, speed=2)

# excute the loop
root.mainloop()
