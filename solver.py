from grid import Grid

game = Grid()

for r in range(6):
    for c in range(6):
        game.setQueenAt(r,c)


game.printGrid()
