from grid import Grid
import turtle as t
def gridToTurtle(grid:Grid):
    s = grid.getSize*50
    half = s/2
    t.setup(s+20,s+20)
    t.speed(-1)
    t.hideturtle()
    t.colormode(255)


    for i,row in enumerate(grid.grid):
        for j,b in enumerate(row):
            
            r,g,b = b.getColor
            t.fillcolor(r,g,b)
            t.pensize(3)
            t.teleport(-half+50*j,half -50*i)
            t.begin_fill()
            for _ in range(4):
                t.forward(50)
                t.right(90)
            t.end_fill()

    t.done()

    
    

game = Grid("level2")

for r in range(game.getSize):
    for c in range(game.getSize):
        game.setQueenAt(r,c)

gridToTurtle(game)

game.printGrid()
