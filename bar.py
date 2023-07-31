import tkinter as tk

def draw_bar_graph(data):
    # Find the maximum value in the data to scale the bars accordingly
    max_value = max(data)

    # Create the Tkinter window
    root = tk.Tk()
    root.title("Bar Graph")

    # Set the size of the canvas
    canvas_width = 400
    canvas_height = 300
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Define the dimensions for the bars
    bar_width = 30
    gap = 20
    x_start = 50
    y_start = canvas_height - 50

    # Draw each bar on the canvas
    for i, value in enumerate(data):
        x0 = x_start + (bar_width + gap) * i
        y0 = y_start
        x1 = x0 + bar_width
        y1 = y_start - (value / max_value) * (canvas_height - 100)

        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
        canvas.create_text((x0 + x1) / 2, y1 - 10, text=str(value))

    root.mainloop()

# Example data for the bar graph
data = [35, 20, 15, 40, 50, 10]

# Draw the bar graph
draw_bar_graph(data)
