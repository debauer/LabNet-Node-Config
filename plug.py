from nodeConfig.base import Base

class Plug(Base): 
    def __init__(self, plug):
        Base.__init__(self, plug)
        if self.data["default"]:
            self.data["status"] = "on"
        else:
            self.data["status"] = "off"

    def __str__(self):
        return "plug: " + self.plug["name"] + " adress: " + str(self.plug["id"]) + " " + str(self.strip["id"]) + " " + str(self.node["id"]) + " "

    def setOn(self):
        self.data["status"] = "on"

    def setOff(self):
        self.data["status"] = "off"

    def set(self,status):
        if status:
            self.data["status"] = "on"
        else:
            self.data["status"] = "off"

    def getStrip(self):
        return self.data["strip"]

    def getStatus(self):
        return self.data["status"]