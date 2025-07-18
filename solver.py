from grid import Grid
import tkinter as tk

def gridToTkinter(grid: Grid):
    cell_size = 50
    size = grid.getSize * cell_size

    # Create main window
    root = tk.Tk()
    root.title("Grid Visualization")

    # Create canvas
    canvas = tk.Canvas(root, width=size, height=size)
    canvas.pack()

    # Draw grid
    for i, row in enumerate(grid.grid):
        for j, block in enumerate(row):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            color = block.getColor
            fill = '#%02x%02x%02x' % tuple(color)  # Convert RGB list to hex string

            # Draw the block
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="black", width=3)

            # If queen is placed, draw a "Q"
            if block.isQueened:
                canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2,
                                   text="Q",
                                   font=("Arial", 20, "bold"),
                                   fill="white")

    root.mainloop()

# Example usage
game = Grid("level2")

# Place queens on all cells (for demonstration)
for r in range(game.getSize):
    for c in range(game.getSize):
        game.setQueenAt(r, c)

# Visualize grid using tkinter
gridToTkinter(game)

# Also print grid to console
game.printGrid()