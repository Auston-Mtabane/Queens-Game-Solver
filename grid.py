class Block:
    def __init__(self,r:int,c:int,color:str):
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
        return f"{self.getColor}, {self.getIndex}, Queen:{self.isQueened}\n"



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
        self.grid[r][c].placeQueen()

    def printGrid(self):
        for r in self.grid:
            for c in r:
                if c.isQueened: print("*",end=" ")
                else: print(c.getColor,end=" ")
            print()
