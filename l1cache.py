import l1block as l1bl

# L1 cache memory, 4 blocks each memory.
class L1Cache:
    def __init__(self):
        # Block definition: Number, Data, Coherence, Address.
        self.l1block0 = l1bl.L1Block(0, 00, "0", 0)
        self.l1block1 = l1bl.L1Block(1, 11, "1", 1)
        self.l1block2 = l1bl.L1Block(2, 22, "2", 2)
        self.l1block3 = l1bl.L1Block(3, 33, "3", 3)

        self.l1BlocksDictionary = {
                                    0: self.l1block0,
                                    1: self.l1block1,
                                    2: self.l1block2,
                                    3: self.l1block3
                                  }

    def getAllBlocks(self):
        return [self.l1block0, self.l1block1, self.l1block2, self.l1block3]

    def getL1BlockByNumber(self, number):
        return self.l1BlocksDictionary.get(number)

# Testing class
#l1cache = L1Cache()
#print(l1cache.getAllBlocks())
#print(l1cache.getL1BlockByNumber(2).data)