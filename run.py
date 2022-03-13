models = {"ER4" : 4}

def main():
    A = switch("ER4")
    B = switch("ER4")
    print(A.ports)

class port():
    def __init__(self):
        state = False
        ipAddr = ""
        connectedTo = ""
        maxPriority = 0
        chache = []
    
    def recieve(self,packet):
        chache.append([maxPriority,packet])
        maxPriority += 1


class switch():
    def __init__(self,model):
        self.model = models[model]
        self.state = True
        self.ports = []

        for _ in range(self.model):
            self.ports.append(port)
        

if __name__ == "__main__":
    main()