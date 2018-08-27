from nodeConfig.base import Base

class Node(Base): 
    def __init__(self, node):
        Base.__init__(self, node)

    # aliases for Base class methods
    addStrip = Base.addChild
    getStrips = Base.getChild
    getStripNames = Base.getChildNames