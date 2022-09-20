import l1cache as l1c

class Control:
    def __init__(self, l1cacheDataHolder, memory, instructionsHolder):
        self.l1cache = l1c.L1Cache()
        self.l1cacheDataHolder = l1cacheDataHolder
        self.memory = memory
        self.instructionsHolder = instructionsHolder

        # Coherence for P0 cache L1 
        self.l1getCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.getCoherence00,
            1: self.l1cacheDataHolder.getCoherence01,
            2: self.l1cacheDataHolder.getCoherence02,
            3: self.l1cacheDataHolder.getCoherence03}                             
        self.l1setCoherenceDictionaryP0 = {
            0: self.l1cacheDataHolder.setCoherence00,
            1: self.l1cacheDataHolder.setCoherence01,
            2: self.l1cacheDataHolder.setCoherence02,
            3: self.l1cacheDataHolder.setCoherence03}
        # Coherence for P1 cache L1 
        self.l1getCoherenceDictionaryP1 = {
            0: self.l1cacheDataHolder.getCoherence10,
            1: self.l1cacheDataHolder.getCoherence11,
            2: self.l1cacheDataHolder.getCoherence12,
            3: self.l1cacheDataHolder.getCoherence13}                             
        self.l1setCoherenceDictionaryP1 = {
            0: self.l1cacheDataHolder.setCoherence10,
            1: self.l1cacheDataHolder.setCoherence11,
            2: self.l1cacheDataHolder.setCoherence12,
            3: self.l1cacheDataHolder.setCoherence13}
        # Coherence for P2 cache L1 
        self.l1getCoherenceDictionaryP2 = {
            0: self.l1cacheDataHolder.getCoherence20,
            1: self.l1cacheDataHolder.getCoherence21,
            2: self.l1cacheDataHolder.getCoherence22,
            3: self.l1cacheDataHolder.getCoherence23}                             
        self.l1setCoherenceDictionaryP2 = {
            0: self.l1cacheDataHolder.setCoherence20,
            1: self.l1cacheDataHolder.setCoherence21,
            2: self.l1cacheDataHolder.setCoherence22,
            3: self.l1cacheDataHolder.setCoherence23}
        # Coherence for P3 cache L1 
        self.l1getCoherenceDictionaryP3 = {
            0: self.l1cacheDataHolder.getCoherence30,
            1: self.l1cacheDataHolder.getCoherence31,
            2: self.l1cacheDataHolder.getCoherence32,
            3: self.l1cacheDataHolder.getCoherence33}                             
        self.l1setCoherenceDictionaryP3 = {
            0: self.l1cacheDataHolder.setCoherence30,
            1: self.l1cacheDataHolder.setCoherence31,
            2: self.l1cacheDataHolder.setCoherence32,
            3: self.l1cacheDataHolder.setCoherence33}

        # Adress for P0 cache L1                  
        self.l1getAddressDictionaryP0 = {
            0: self.l1cacheDataHolder.getAddress00,
            1: self.l1cacheDataHolder.getAddress01,
            2: self.l1cacheDataHolder.getAddress02,
            3: self.l1cacheDataHolder.getAddress03}                          
        self.l1setAddressDictionaryP0 = {
            0: self.l1cacheDataHolder.setAddress00,
            1: self.l1cacheDataHolder.setAddress01,
            2: self.l1cacheDataHolder.setAddress02,
            3: self.l1cacheDataHolder.setAddress03}
        # Adress for P1 cache L1                  
        self.l1getAddressDictionaryP1 = {
            0: self.l1cacheDataHolder.getAddress10,
            1: self.l1cacheDataHolder.getAddress11,
            2: self.l1cacheDataHolder.getAddress12,
            3: self.l1cacheDataHolder.getAddress13}                          
        self.l1setAddressDictionaryP1 = {
            0: self.l1cacheDataHolder.setAddress10,
            1: self.l1cacheDataHolder.setAddress11,
            2: self.l1cacheDataHolder.setAddress12,
            3: self.l1cacheDataHolder.setAddress13}
        # Adress for P2 cache L1                  
        self.l1getAddressDictionaryP2 = {
            0: self.l1cacheDataHolder.getAddress20,
            1: self.l1cacheDataHolder.getAddress21,
            2: self.l1cacheDataHolder.getAddress22,
            3: self.l1cacheDataHolder.getAddress23}                          
        self.l1setAddressDictionaryP2 = {
            0: self.l1cacheDataHolder.setAddress20,
            1: self.l1cacheDataHolder.setAddress21,
            2: self.l1cacheDataHolder.setAddress22,
            3: self.l1cacheDataHolder.setAddress23}
        # Adress for P3 cache L1                  
        self.l1getAddressDictionaryP3 = {
            0: self.l1cacheDataHolder.getAddress30,
            1: self.l1cacheDataHolder.getAddress31,
            2: self.l1cacheDataHolder.getAddress32,
            3: self.l1cacheDataHolder.getAddress33}                          
        self.l1setAddressDictionaryP3 = {
            0: self.l1cacheDataHolder.setAddress30,
            1: self.l1cacheDataHolder.setAddress31,
            2: self.l1cacheDataHolder.setAddress32,
            3: self.l1cacheDataHolder.setAddress33}

        # Data for P0 cache L1
        self.l1getDataDictionaryP0 = {
            0: self.l1cacheDataHolder.getData00,
            1: self.l1cacheDataHolder.getData01,
            2: self.l1cacheDataHolder.getData02,
            3: self.l1cacheDataHolder.getData03}                        
        self.l1setDataDictionaryP0 = {
            0: self.l1cacheDataHolder.setData00,
            1: self.l1cacheDataHolder.setData01,
            2: self.l1cacheDataHolder.setData02,
            3: self.l1cacheDataHolder.setData03}
        # Data for P1 cache L1
        self.l1getDataDictionaryP1 = {
            0: self.l1cacheDataHolder.getData10,
            1: self.l1cacheDataHolder.getData11,
            2: self.l1cacheDataHolder.getData12,
            3: self.l1cacheDataHolder.getData13}                        
        self.l1setDataDictionaryP1 = {
            0: self.l1cacheDataHolder.setData10,
            1: self.l1cacheDataHolder.setData11,
            2: self.l1cacheDataHolder.setData12,
            3: self.l1cacheDataHolder.setData13}
        # Data for P2 cache L1
        self.l1getDataDictionaryP2 = {
            0: self.l1cacheDataHolder.getData20,
            1: self.l1cacheDataHolder.getData21,
            2: self.l1cacheDataHolder.getData22,
            3: self.l1cacheDataHolder.getData23}                        
        self.l1setDataDictionaryP2 = {
            0: self.l1cacheDataHolder.setData20,
            1: self.l1cacheDataHolder.setData21,
            2: self.l1cacheDataHolder.setData22,
            3: self.l1cacheDataHolder.setData23}
        # Data for P3 cache L1
        self.l1getDataDictionaryP3 = {
            0: self.l1cacheDataHolder.getData30,
            1: self.l1cacheDataHolder.getData31,
            2: self.l1cacheDataHolder.getData32,
            3: self.l1cacheDataHolder.getData33}                        
        self.l1setDataDictionaryP3 = {
            0: self.l1cacheDataHolder.setData30,
            1: self.l1cacheDataHolder.setData31,
            2: self.l1cacheDataHolder.setData32,
            3: self.l1cacheDataHolder.setData33}
                                    
    def handleOperation(self, operation, processorNumber, address, data):
        self.updateLocalCache(processorNumber)
        return self.handleOperationAux(operation, processorNumber, address, data)

    def handleOperationAux(self, operation, processorNumber, address, data):
        if (operation == "R"):
            return self.handleRead(processorNumber, address)
        else:
            return self.handleWrite(processorNumber, address, data)

    def updateLocalCache(self, processorNumber): 
        l1blocks = self.l1cache.getAllBlocks()
        if (processorNumber == 0):
            for l1block in l1blocks:
                l1block.setCoherence(self.l1getCoherenceDictionaryP0.get(l1block.number)())
                l1block.setAddress(self.l1getAddressDictionaryP0.get(l1block.number)())
                l1block.setData(self.l1getDataDictionaryP0.get(l1block.number)())
            return
        elif (processorNumber == 1):
            for l1block in l1blocks:
                l1block.setCoherence(self.l1getCoherenceDictionaryP1.get(l1block.number)())
                l1block.setAddress(self.l1getAddressDictionaryP1.get(l1block.number)())
                l1block.setData(self.l1getDataDictionaryP1.get(l1block.number)())
            return
        elif (processorNumber == 2):
            for l1block in l1blocks:
                l1block.setCoherence(self.l1getCoherenceDictionaryP2.get(l1block.number)())
                l1block.setAddress(self.l1getAddressDictionaryP2.get(l1block.number)())
                l1block.setData(self.l1getDataDictionaryP2.get(l1block.number)())
            return
        elif (processorNumber == 3):
            for l1block in l1blocks:
                l1block.setCoherence(self.l1getCoherenceDictionaryP3.get(l1block.number)())
                l1block.setAddress(self.l1getAddressDictionaryP3.get(l1block.number)())
                l1block.setData(self.l1getDataDictionaryP3.get(l1block.number)())
            return
        else:
            print ("Something went wrong Updating Local Cache!")
            return 

    def updateHolderCache(self, processorNumber):
        l1blocks = self.l1cache.getAllBlocks()
        if (processorNumber == 0):
            for l1block in l1blocks:
                self.l1setCoherenceDictionaryP0.get(l1block.number)(l1block.getCoherence())
                self.l1setAddressDictionaryP0.get(l1block.number)(l1block.getAddress())
                self.l1setDataDictionaryP0.get(l1block.number)(l1block.getData())
            return
        elif (processorNumber == 1):
            for l1block in l1blocks:
                self.l1setCoherenceDictionaryP1.get(l1block.number)(l1block.getCoherence())
                self.l1setAddressDictionaryP1.get(l1block.number)(l1block.getAddress())
                self.l1setDataDictionaryP1.get(l1block.number)(l1block.getData())
            return
        elif (processorNumber == 2):
            for l1block in l1blocks:
                self.l1setCoherenceDictionaryP2.get(l1block.number)(l1block.getCoherence())
                self.l1setAddressDictionaryP2.get(l1block.number)(l1block.getAddress())
                self.l1setDataDictionaryP2.get(l1block.number)(l1block.getData())
            return
        elif (processorNumber == 3):
            for l1block in l1blocks:
                self.l1setCoherenceDictionaryP3.get(l1block.number)(l1block.getCoherence())
                self.l1setAddressDictionaryP3.get(l1block.number)(l1block.getAddress())
                self.l1setDataDictionaryP3.get(l1block.number)(l1block.getData())
            return
        else:
            print("Something went wrong Updating Holder Cache!")
            return

    def handleRead(self, processorNumber, address):
        l1cacheBlocks = self.l1cache.getAllBlocks()
        # Check for hits and misses inside local cache
        for l1cacheBlock in l1cacheBlocks:
            # in case of a miss read, call cache holder if not in local blocks
            # Read Hits
            if l1cacheBlock.address == address and (l1cacheBlock.coherence == "M" or l1cacheBlock.coherence == "E" or l1cacheBlock.coherence == "S"):
                
                # Agregar casos para cada estado local en caso de hit
                
                print("P" + str(processorNumber) + ": Read Hit from local Cache L1\n")
                return l1cacheBlock.getData()
            # Read Miss
            elif l1cacheBlock.address == address and l1cacheBlock.coherence == "I":
                break # Check other caches with l1cacheDataHolder
            else:
                print ("P" + str(processorNumber) + ": Not in this local cache block: " + str(l1cacheBlock.number) + "\n")
        # Address not in local cache
        print("P" + str(processorNumber) + ": Read Miss from local Cache L1\n")   
        self.checkOtherCaches(processorNumber, address, l1cacheBlock) # Check other caches with l1cacheDataHolder
        return 

    def checkOtherCaches(self, processorNumber, address, l1cacheBlock):
        print("Processor number: "+ str(processorNumber))
        changes = 0
        # Time to search in other caches.
        if (processorNumber == 0):
            for block in self.l1getAddressDictionaryP1:
                if self.l1getAddressDictionaryP1[block]() == address and (self.l1getCoherenceDictionaryP1[block]() == "M" or self.l1getCoherenceDictionaryP1[block]() == "E" or self.l1getCoherenceDictionaryP1[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP1[block]() == "M" or self.l1getCoherenceDictionaryP1[block]() == "E" or self.l1getCoherenceDictionaryP1[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP1[block]())
                        self.l1setCoherenceDictionaryP1[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP1[block]())
                    print("P" + str(processorNumber) + ": Read Miss from Local Cache but Read Hit from P1 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1

                if self.l1getAddressDictionaryP2[block]() == address and (self.l1getCoherenceDictionaryP2[block]() == "M" or self.l1getCoherenceDictionaryP2[block]() == "E" or self.l1getCoherenceDictionaryP2[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP2[block]() == "M" or self.l1getCoherenceDictionaryP2[block]() == "E" or self.l1getCoherenceDictionaryP2[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP2[block]())
                        self.l1setCoherenceDictionaryP2[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP2[block]())
                    print("P" + str(processorNumber) + ": Read Miss from Local Cache but Read Hit from P2 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1

                if self.l1getAddressDictionaryP3[block]() == address and (self.l1getCoherenceDictionaryP3[block]() == "M" or self.l1getCoherenceDictionaryP3[block]() == "E" or self.l1getCoherenceDictionaryP3[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP3[block]() == "M" or self.l1getCoherenceDictionaryP3[block]() == "E" or self.l1getCoherenceDictionaryP3[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP3[block]())
                        self.l1setCoherenceDictionaryP3[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP3[block]())
                    print("P" + str(processorNumber) + ": Read Miss from Local Cache but Read Hit from P3 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1
            if changes == 1:
                return
            else:        
                self.handleFullReadMiss(address, processorNumber)
                return

        elif (processorNumber == 1):
            for block in self.l1getAddressDictionaryP0:
                print ("This block is: " + str(block) + " , and address: " + str(self.l1getAddressDictionaryP0[block]()))
                if self.l1getAddressDictionaryP0[block]() == address and (self.l1getCoherenceDictionaryP0[block]() == "M" or self.l1getCoherenceDictionaryP0[block]() == "E" or self.l1getCoherenceDictionaryP0[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP0[block]() == "M" or self.l1getCoherenceDictionaryP0[block]() == "E" or self.l1getCoherenceDictionaryP0[block]() != "S"):
                        
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP0[block]())
                        self.l1setCoherenceDictionaryP0[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP0[block]())
                    print("P" + str(processorNumber) + ": Read Miss from Local Cache but Read Hit from P0 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1
                    break

                if self.l1getAddressDictionaryP2[block]() == address and (self.l1getCoherenceDictionaryP2[block]() == "M" or self.l1getCoherenceDictionaryP2[block]() == "E" or self.l1getCoherenceDictionaryP2[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP2[block]() == "M" or self.l1getCoherenceDictionaryP2[block]() == "E" or self.l1getCoherenceDictionaryP2[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP2[block]())
                        self.l1setCoherenceDictionaryP2[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP2[block]())
                    print("P" + str(processorNumber) + ": Read Miss from Local Cache but Read Hit from P2 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1

                if self.l1getAddressDictionaryP3[block]() == address and (self.l1getCoherenceDictionaryP3[block]() == "M" or self.l1getCoherenceDictionaryP3[block]() == "E" or self.l1getCoherenceDictionaryP3[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP3[block]() == "M" or self.l1getCoherenceDictionaryP3[block]() == "E" or self.l1getCoherenceDictionaryP3[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP3[block]())
                        self.l1setCoherenceDictionaryP3[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP3[block]())
                    print("P" + str(processorNumber) + ": Read Miss from Local Cache but Read Hit from P3 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1
            if changes == 1:
                return
            else:        
                self.handleFullReadMiss(address, processorNumber)
                return

        elif (processorNumber == 2):
            for block in self.l1getAddressDictionaryP0:
                print ("This block is: " + str(block) + " , and address: " + str(self.l1getAddressDictionaryP0[block]()))
                if self.l1getAddressDictionaryP0[block]() == address and (self.l1getCoherenceDictionaryP0[block]() == "M" or self.l1getCoherenceDictionaryP0[block]() == "E" or self.l1getCoherenceDictionaryP0[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP0[block]() == "M" or self.l1getCoherenceDictionaryP0[block]() == "E" or self.l1getCoherenceDictionaryP0[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP0[block]())
                        self.l1setCoherenceDictionaryP0[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP0[block]())
                    print("P" + str(processorNumber) + ": Read Miss from Local Cache but Read Hit from P0 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1

                if self.l1getAddressDictionaryP1[block]() == address and (self.l1getCoherenceDictionaryP1[block]() == "M" or self.l1getCoherenceDictionaryP1[block]() == "E" or self.l1getCoherenceDictionaryP1[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP1[block]() == "M" or self.l1getCoherenceDictionaryP1[block]() == "E" or self.l1getCoherenceDictionaryP1[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP1[block]())
                        self.l1setCoherenceDictionaryP1[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP1[block]())
                    print("P" + str(processorNumber) + ": Read Miss from Local Cache but Read Hit from P1 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1

                if self.l1getAddressDictionaryP3[block]() == address and (self.l1getCoherenceDictionaryP3[block]() == "M" or self.l1getCoherenceDictionaryP3[block]() == "E" or self.l1getCoherenceDictionaryP3[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP3[block]() == "M" or self.l1getCoherenceDictionaryP3[block]() == "E" or self.l1getCoherenceDictionaryP3[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP3[block]())
                        self.l1setCoherenceDictionaryP3[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP3[block]())
                    print("P" + str(processorNumber) + ": Read Miss from Local Cache but Read Hit from P3 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1
            if changes == 1:
                return
            else:        
                self.handleFullReadMiss(address, processorNumber)
                return

        elif (processorNumber == 3):
            for block in self.l1getAddressDictionaryP0:
                print ("This block is: " + str(block) + " , and address: " + str(self.l1getAddressDictionaryP0[block]()))
                if self.l1getAddressDictionaryP0[block]() == address and (self.l1getCoherenceDictionaryP0[block]() == "M" or self.l1getCoherenceDictionaryP0[block]() == "E" or self.l1getCoherenceDictionaryP0[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP0[block]() == "M" or self.l1getCoherenceDictionaryP0[block]() == "E" or self.l1getCoherenceDictionaryP0[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP0[block]())
                        self.l1setCoherenceDictionaryP0[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP0[block]())
                    print("P" + str(processorNumber) + ": Read Hit from P0 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1

                if self.l1getAddressDictionaryP1[block]() == address and (self.l1getCoherenceDictionaryP1[block]() == "M" or self.l1getCoherenceDictionaryP1[block]() == "E" or self.l1getCoherenceDictionaryP1[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP1[block]() == "M" or self.l1getCoherenceDictionaryP1[block]() == "E" or self.l1getCoherenceDictionaryP1[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP1[block]())
                        self.l1setCoherenceDictionaryP1[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP1[block]())
                    print("P" + str(processorNumber) + ": Read Hit from P1 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1

                if self.l1getAddressDictionaryP2[block]() == address and (self.l1getCoherenceDictionaryP2[block]() == "M" or self.l1getCoherenceDictionaryP2[block]() == "E" or self.l1getCoherenceDictionaryP2[block]() == "S"):
                    if (self.l1getCoherenceDictionaryP2[block]() == "M" or self.l1getCoherenceDictionaryP2[block]() == "E" or self.l1getCoherenceDictionaryP2[block]() != "S"):
                        self.l1cache.getL1BlockByNumber(block).setCoherence("S")
                        self.l1cache.getL1BlockByNumber(block).setAddress(address)
                        self.l1cache.getL1BlockByNumber(block).setData(self.l1getDataDictionaryP2[block]())
                        self.l1setCoherenceDictionaryP2[block]("S")
                        self.memory.blocksDictionary[address].setData(self.l1getDataDictionaryP2[block]())
                    print("P" + str(processorNumber) + ": Read Hit from P2 Cache L1\n")
                    self.updateLocalCache(processorNumber)
                    self.updateHolderCache(processorNumber)
                    changes = 1
            if changes == 1:
                return
            else:        
                self.handleFullReadMiss(address, processorNumber)
                return
        else:
            print("Something went wrong, no processor number given?")
            return
                
    def handleFullReadMiss(self, address, processorNumber):
        # Time to search in memory
        l1cacheBlocks = self.l1cache.getAllBlocks()
        for block in l1cacheBlocks:
            if block.getCoherence() == "I":
                block.setCoherence("E")
                break
        block.setData(self.memory.blocksDictionary[address].getData())
        block.setAddress(address)
        print("P" + str(processorNumber) + ": Read data from memory\n")
        self.updateHolderCache(processorNumber)
        self.updateLocalCache(processorNumber)
        return 

    def handleWrite(self, processorNumber, address, data):
        print("P"+ str(processorNumber) +": Hey! This data value is: " + str(data))
        l1cacheBlocks = self.l1cache.getAllBlocks()
        for block in l1cacheBlocks:
            if block.address == address and block.coherence == "E":
                block.setCoherence("M")
                block.data = data
                block.address = address
                self.updateHolderCache(processorNumber)
                self.updateLocalCache(processorNumber)

                #print("P" + str(processorNumber) + ": Write Hit from local Cache L1, current state: "+ str(self.l1getCoherenceDictionaryP0[0]()) + "\n")
                return
            elif block.address == address and block.coherence == "M":
                block.data = data
                block.address = address
                self.updateHolderCache(processorNumber)
                self.updateLocalCache(processorNumber)

                #print("P" + str(processorNumber) + ": Write Hit from local Cache L1\n")
                return
            elif block.address == address and block.coherence == "I":
                block.setCoherence("E")
                block.data = data
                block.address = address
                self.updateHolderCache(processorNumber)
                self.invalidateOtherCaches(processorNumber, address, data)
                self.updateLocalCache(processorNumber)

                return
            elif block.address == address and block.coherence == "S":
                block.setCoherence("M")
                block.data = data
                block.address = address
                self.updateHolderCache(processorNumber)
                self.invalidateOtherCaches(processorNumber, address, data)
                self.updateLocalCache(processorNumber)

                return
            else:
                # Write Miss, write new data in invalid block
                for block in l1cacheBlocks:
                    if block.coherence == "I":
                        block.coherence = "M"
                        block.data = data
                        block.address = address
                        self.updateHolderCache(processorNumber)
                        self.updateLocalCache(processorNumber)

                        break
                    else:
                        pass
                print("P" + str(processorNumber) + ": Write Miss from local Cache L1\n")
                print("Writing in Invalid or Shared state block")
                return
        #print("P"+ str(processorNumber) +": Hey! This block data value is: " + str(block.))
        return

    def invalidateOtherCaches(self, processorNumber, address, data):
        if (processorNumber == 0):
            for block in self.l1getCoherenceDictionaryP0:
                if self.l1getAddressDictionaryP0[block]() == address and self.l1getAddressDictionaryP0[block]() != data:
                    self.l1setCoherenceDictionaryP0[block]("I")
                if self.l1getAddressDictionaryP1[block]() == address:
                    self.l1setCoherenceDictionaryP1[block]("I")
                if self.l1getAddressDictionaryP2[block]() == address:
                    self.l1setCoherenceDictionaryP2[block]("I")
                if self.l1getAddressDictionaryP3[block]() == address:
                    self.l1setCoherenceDictionaryP3[block]("I")
                else:
                    print ("P" + str(processorNumber) + ": No blocks to invalidate from other caches in this " + str(block) + " round")
            return
        elif (processorNumber == 1):
            for block in self.l1getCoherenceDictionaryP0:
                if self.l1getAddressDictionaryP0[block]() == address:
                    self.l1setCoherenceDictionaryP0[block]("I")
                if self.l1getAddressDictionaryP1[block]() == address and self.l1getAddressDictionaryP1[block]() != data:
                    self.l1setCoherenceDictionaryP1[block]("I")
                if self.l1getAddressDictionaryP2[block]() == address:
                    self.l1setCoherenceDictionaryP2[block]("I")
                if self.l1getAddressDictionaryP3[block]() == address:
                    self.l1setCoherenceDictionaryP3[block]("I")
                else:
                    print ("P" + str(processorNumber) + ": No blocks to invalidate from other caches in this " + str(block) + " round")
            return
        elif (processorNumber == 2):
            for block in self.l1getCoherenceDictionaryP0:
                if self.l1getAddressDictionaryP0[block]() == address:
                    self.l1setCoherenceDictionaryP0[block]("I")
                if self.l1getAddressDictionaryP1[block]() == address:
                    self.l1setCoherenceDictionaryP1[block]("I")
                if self.l1getAddressDictionaryP2[block]() == address and self.l1getAddressDictionaryP2[block]() != data:
                    self.l1setCoherenceDictionaryP2[block]("I")
                if self.l1getAddressDictionaryP3[block]() == address:
                    self.l1setCoherenceDictionaryP3[block]("I")
                else:
                    print ("P" + str(processorNumber) + ": No blocks to invalidate from other caches in this " + str(block) + " round")
            return
        elif (processorNumber == 3):
            for block in self.l1getCoherenceDictionaryP0:
                if self.l1getAddressDictionaryP0[block]() == address:
                    self.l1setCoherenceDictionaryP0[block]("I")
                if self.l1getAddressDictionaryP1[block]() == address:
                    self.l1setCoherenceDictionaryP1[block]("I")
                if self.l1getAddressDictionaryP2[block]() == address:
                    self.l1setCoherenceDictionaryP2[block]("I")
                if self.l1getAddressDictionaryP3[block]() == address and self.l1getAddressDictionaryP3[block]() != data:
                    self.l1setCoherenceDictionaryP3[block]("I")
                else:
                    print ("P" + str(processorNumber) + ": No blocks to invalidate from other caches in this " + str(block) + " round")
            return
        else:
            print("Something went wrong, no processor number specified?")
            return
