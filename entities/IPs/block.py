# Atomic class for memory blocks

class Block:
    def __init__(self, number, data):
        self.number = number
        self.data = data

    # Get and Set functions for block numbers
    def getNumber(self):
        return self.number.value
    def setNumber(self, number):
        self.number.value = number

    # Get and Set functions for block data
    def getData(self):
        return self.data.value
    def setData(self, data):
        self.data.value = data