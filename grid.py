class Block:
    def __init__(self,r,c,color):
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



class Grid:
    def __init__(self,filepath="level1"):
        with open(f"levels/{filepath}.txt","r") as f:
            rows = f.readlines()
            l = []
            for i in rows:
                r = []
                for x in i.strip("\n"):
                    r.append({})
                l.append(r)
        

        print(l)
