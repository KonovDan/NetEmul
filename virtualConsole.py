class console():
    def __init__(self, motherDevice,motherDeviceName): 
        self.motherDevice = motherDevice
        self.motherDeviceName = motherDeviceName

    def start(self):
        print(f"### Welcome to {self.motherDeviceName} console ###")
        while True:
            inputedValue = input(f"{self.motherDeviceName} >>> ").split(" ")
            if inputedValue[0] == "exit": break
            elif inputedValue[0] == "info": print(f"\
Name:{self.motherDeviceName}\n\
Type:{self.motherDevice.type}\n\
Model:{self.motherDevice.model}\n\
Mount of ports:{len(self.motherDevice.ports)}\
                ")