class L1Block():
    def __init__(self, number, data, coherence, address):

        self.number = number
        self.data = data
        self.coherence = coherence
        self.address = address

    # Get and Set functions for each self attribute.
    def getNumber(self):
        return self.number
    def setNumber(self, number):
        self.number = number
        return

    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data
        return

    def getCoherence(self):
        return self.coherence
    def setCoherence(self, coherence):
        self.coherence = coherence
        return

    def getAddress(self):
        return self.address
    def setAddress(self, address):
        self.address = address
        return