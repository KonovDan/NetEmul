import virtualConsole

models = {"ES4" : 4}
devices = {}

class frame:
    def __init__(self, sndMAC, dstMAC, incapsulatedData):
        self.header = sndMAC + dstMAC
        self.incapsulatedData = incapsulatedData

    def __call__(self): return self.header + self.incapsulatedData


class port:
    def __init__(self, motherDevice):
        self.motherDevice = motherDevice
        self.state = False
        self.IPAddr = ""
        self.MACAddr = ""
        self.connectedTo = ""

    def recieveFrame(self, frame): print(frame())
    def sendFrame(self, frame):  self.connectedTo.recieveFrame(frame)


class switch:
    def __init__(self, name, model):
        self.name = name
        self.type = "switch"
        self.model = model
        self.console = virtualConsole.console(motherDevice=self, motherDeviceName=self.name)
        self.state = True
        self.ports = {}
        self.chache = []
        for _ in range(models[self.model]):
            self.ports[_] = port(self)
    
    def __call__(self): return f"{self.type} | {self.model}"

    def chacheUse(operationType, packet=None):
        if operationType == "READ":
            pass
        elif operationType == "WRITE":
            pass
        elif operationType == "SEARCH":
            pass

    def startConsole(self):
        self.console.start()