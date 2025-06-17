class Block:
    def __init__(self,r:int,c:int,color:str):
        self.info = {
            "isQueened":False,
            "index":(r,c),
            "color":color
            }
    def placeQueen(self):
        self.info["index"] = True
    def removeQueen(self):
        self.info["index"] = False

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
        with open(f"levels/{filepath}.txt","r") as f:
            rows = f.readlines()
            l = []
            for i,row_s in enumerate(rows):
                r = []
                for j,color in enumerate(row_s.strip("\n")):
                    r.append(Block(i,j,color))
                l.append(r)
        

        print(l)
