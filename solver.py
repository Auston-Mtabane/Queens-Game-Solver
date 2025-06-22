from grid import Grid

game = Grid("level2")

for r in range(game.getSize):
    for c in range(game.getSize):
        game.setQueenAt(r,c)


game.printGrid()
