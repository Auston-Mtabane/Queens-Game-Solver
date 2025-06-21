from typing import List

class Block:
    def __init__(self,r:int,c:int,color:str):
        self.colorCode = {"p":"\033[0;35m","o":"\033[0;33m","g":"\033[1;32m","G":"\033[1;30m","b":"\033[1;34m","r":"\033[1;31m"}
        self.info = {
            "isQueened":False,
            "index":(r,c),
            "color":color
            }
    def placeQueen(self):
        self.info["isQueened"] = True
    def removeQueen(self):
        self.info["isQueened"] = False

    @property
    def getColor(self):
        return self.info["color"]
    
    @property
    def getIndex(self)->tuple:
        return self.info["index"]
    
    @property
    def isQueened(self):
        return self.info["isQueened"]
    
    def __repr__(self):
        return f"{self.colorCode[self.getColor]}{"Q" if self.isQueened else "■"}\033[0m"

class ColorSection:
    def __init__(self,section:List[Block]):
        pass


    


class Grid:
    def __init__(self,filepath="level1"):
        self.grid = []
        with open(f"levels/{filepath}.txt","r") as f:
            rows = f.readlines()
            for i,row_s in enumerate(rows):
                r = []
                for j,color in enumerate(row_s.strip("\n")):
                    r.append(Block(i,j,color))
                self.grid.append(r)
    @property
    def getSize(self):
        return len(self.grid)

    def setQueenAt(self,r:int,c:int):
        if self.isMoveValid(r,c):
            self.grid: List[List[Block]]
            self.grid[r][c].placeQueen()

    def printGrid(self):
        for r in self.grid:
            for c in r:
                print(c,end=" ")
            print()
    
    def isMoveValid(self,r:int,c:int):
        #check row and call 
        for row in self.grid:
            for b in row:
                if r==b.getIndex[0] and c!= b.getIndex[1] and b.isQueened:
                    print("there's a queen in the same row ")
                    return False
                elif r != b.getIndex[0] and c == b.getIndex[1] and b.isQueened:
                    print("there's a queen in the same column ")
                    return False

        #check color
        block = self.grid[r][c]

        for row in self.grid:
            for b in row:
                if b.isQueened and b.getColor == block.getColor:
                    print(f"color already queened at {b} {b.getIndex}")
                    return False


        #check diagonal 
        #TODO place diagonal code here.
        for y,x in [[r,c+1],[r,c-1],[r+1,c],[r-1,c]     ,[r+1,c+1],[r+1,c-1],[r-1,c+1],[r-1,c-1]]:
            try:
                if self.grid[y][x].isQueened :
                    print("there's a queen adjesent or diagonal")
                    return False
            except IndexError:
                continue
        return True
