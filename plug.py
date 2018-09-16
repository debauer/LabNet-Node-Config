from nodeConfig.base import Base

class Plug(Base):
    def __init__(self, plug):
        Base.__init__(self, plug)
        if self.data["default"]:
            self.data["status"] = "on"
        else:
            self.data["status"] = "off"

    def __str__(self):
        return "plug: " + self.data["name"] + " address: " + str(self.data["address"]) + " " + str(self.data["id"]) + " " + str(self.data["pludId"]) + " "

    def setOn(self):
        self.data["status"] = "on"

    def setOff(self):
        self.data["status"] = "off"

    def set(self,status):
        if status:
            self.data["status"] = "on"
        else:
            self.data["status"] = "off"

    def getStripId(self):
        return self.data["stripId"]

    def getStatus(self):
        return self.data["status"]
