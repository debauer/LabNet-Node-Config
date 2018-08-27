from nodeConfig.base import Base

class Strip(Base): 
    def __init__(self, strip):
        Base.__init__(self, strip)

    # aliases for Base class methods
    addPlug = Base.addChild
    getPlugs = Base.getChild
    getPlugNames = Base.getChildNames

    def getNode(self):
        return self.data["node"]