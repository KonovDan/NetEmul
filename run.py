import os
switches = []
models = {"ER4": 4}


def main():
    switches.append(switch("ER4"))
    A = switch("ER4")
    B = switch("ER4")
    A.ports[0].connectedTo = B.ports[0]

    f = frame("1", "2", "incapsulatedData")

    A.ports[0].sendFrame(frame=f)
    VSHELL()


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
    def __init__(self, model):
        self.model = models[model]
        self.state = True
        self.ports = []
        self.chache = []
        for _ in range(self.model):
            self.ports.append(port(self))

    def chacheUse(operationType, packet=None):
        if operationType == "READ":
            pass
        elif operationType == "WRITE":
            pass
        elif operationType == "SEARCH":
            pass


def VSHELL():
    while True:
        inputedValue = input(">>>")
        if inputedValue == "exit":
            os.sys.exit()
        elif inputedValue == "switches":
            print(switches)


if __name__ == "__main__":
    main()
