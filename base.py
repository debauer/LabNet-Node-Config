class Base:
    def __init__(self, data):
        self.data = data
        self.childs = []

    def getData(self):
        return self.data

    def getAddress(self):
        return self.data["address"]

    #def setName(self,name):
    #    self.data["name"] = name

    #def getName(self):
    #    return self.data["name"]

    def setId(self,Id):
        self.data["id"] = Id

    def getId(self):
        return self.data["id"]

    setName = setId
    getName = getId

    def addChild(self,child):
        self.childs.append(child)

    def getChild(self):
        return self.child

    def getChildNames(self):
        d = []
        for s in self.childs:
            d.append(s.getName())
        return d