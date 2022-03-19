import objectLibrary
import os



def start():
    while True:
        inputedValue = input(">>> ").split(' ')
        if inputedValue[0] == "exit": os.sys.exit()
        elif inputedValue[0] == "help": print("\n\
devices - shows list of all created devices\n\
create - creates device >>> create [switch, router, ...] {name} {model}\n\
link - links ports >>> link {first device} {port} {second device} {port}\n\
console - opens console of device >>> console {device}\n\
exit - exit the program\n\
                ")
        elif inputedValue[0] == "devices":
            print(objectLibrary.devices)
            for _ in objectLibrary.devices.keys():
                print(f"{_}: {objectLibrary.devices[_]()}")
        elif inputedValue[0] == "create": createDevice(inputedValue)
        elif inputedValue[0] == "link": updateLink(inputedValue)
        elif inputedValue[0] == "console": objectLibrary.devices[inputedValue[1]].startConsole()
        else: print("---Wrong command---")


def createDevice(inputedValue):
    if inputedValue[1] == "switch":
        if inputedValue[2] in objectLibrary.devices: print("---There is already device with this name---")
        else: objectLibrary.devices[inputedValue[2]] = objectLibrary.switch(name=inputedValue[2],model=inputedValue[3])
    else: print("---There is no type of device as {}---".format(inputedValue[1]))


def updateLink(inputedValue):
    objectLibrary.devices[inputedValue[1]].ports[int(inputedValue[2])].connectedTo = objectLibrary.devices[inputedValue[3]].ports[int(inputedValue[4])]
    objectLibrary.devices[inputedValue[3]].ports[int(inputedValue[4])].connectedTo = objectLibrary.devices[inputedValue[1]].ports[int(inputedValue[2])]