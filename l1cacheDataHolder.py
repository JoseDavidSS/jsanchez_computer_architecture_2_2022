from ctypes import c_char_p

class L1CacheDataHolder():
    def __init__(self, manager):
        
        # Coherence codes XX, first X reference the processor, the second X reference the cache block
        self.coherence00 = manager.Value(c_char_p, "I")
        self.coherence01 = manager.Value(c_char_p, "I")
        self.coherence02 = manager.Value(c_char_p, "I")
        self.coherence03 = manager.Value(c_char_p, "I")

        self.coherence10 = manager.Value(c_char_p, "I")
        self.coherence11 = manager.Value(c_char_p, "I")
        self.coherence12 = manager.Value(c_char_p, "I")
        self.coherence13 = manager.Value(c_char_p, "I")

        self.coherence20 = manager.Value(c_char_p, "I")
        self.coherence21 = manager.Value(c_char_p, "I")
        self.coherence22 = manager.Value(c_char_p, "I")
        self.coherence23 = manager.Value(c_char_p, "I")

        self.coherence30 = manager.Value(c_char_p, "I")
        self.coherence31 = manager.Value(c_char_p, "I")
        self.coherence32 = manager.Value(c_char_p, "I")
        self.coherence33 = manager.Value(c_char_p, "I")

        # Address codes XX, first X reference the processor, the second X reference the cache block
        self.address00 = manager.Value("i", 0)
        self.address01 = manager.Value("i", 0)
        self.address02 = manager.Value("i", 0)
        self.address03 = manager.Value("i", 0)

        self.address10 = manager.Value("i", 0)
        self.address11 = manager.Value("i", 0)
        self.address12 = manager.Value("i", 0)
        self.address13 = manager.Value("i", 0)

        self.address20 = manager.Value("i", 0)
        self.address21 = manager.Value("i", 0)
        self.address22 = manager.Value("i", 0)
        self.address23 = manager.Value("i", 0)

        self.address30 = manager.Value("i", 0)
        self.address31 = manager.Value("i", 0)
        self.address32 = manager.Value("i", 0)
        self.address33 = manager.Value("i", 0)

        # Data codes XX, first X reference the processor, the second X reference the cache block
        self.data00 = manager.Value("i", 0)
        self.data01 = manager.Value("i", 0)
        self.data02 = manager.Value("i", 0)
        self.data03 = manager.Value("i", 0)

        self.data10 = manager.Value("i", 0)
        self.data11 = manager.Value("i", 0)
        self.data12 = manager.Value("i", 0)
        self.data13 = manager.Value("i", 0)

        self.data20 = manager.Value("i", 0)
        self.data21 = manager.Value("i", 0)
        self.data22 = manager.Value("i", 0)
        self.data23 = manager.Value("i", 0)

        self.data30 = manager.Value("i", 0)
        self.data31 = manager.Value("i", 0)
        self.data32 = manager.Value("i", 0)
        self.data33 = manager.Value("i", 0)

    # Get and Set functions for Coherence
    def getCoherence00(self):
        return self.coherence00.value
    def setCoherence00(self, coherence):
        self.coherence00.value = coherence
        return

    def getCoherence01(self):
        return self.coherence01.value
    def setCoherence01(self, coherence):
        self.coherence01.value = coherence
        return

    def getCoherence02(self):
        return self.coherence02.value
    def setCoherence02(self, coherence):
        self.coherence02.value = coherence
        return

    def getCoherence03(self):
        return self.coherence03.value
    def setCoherence03(self, coherence):
        self.coherence03.value = coherence
        return

    def getCoherence10(self):
        return self.coherence10.value
    def setCoherence10(self, coherence):
        self.coherence10.value = coherence
        return

    def getCoherence11(self):
        return self.coherence11.value
    def setCoherence11(self, coherence):
        self.coherence11.value = coherence
        return

    def getCoherence12(self):
        return self.coherence12.value
    def setCoherence12(self, coherence):
        self.coherence12.value = coherence
        return

    def getCoherence13(self):
        return self.coherence13.value
    def setCoherence13(self, coherence):
        self.coherence13.value = coherence
        return

    def getCoherence20(self):
        return self.coherence20.value
    def setCoherence20(self, coherence):
        self.coherence20.value = coherence
        return

    def getCoherence21(self):
        return self.coherence21.value
    def setCoherence21(self, coherence):
        self.coherence21.value = coherence
        return

    def getCoherence22(self):
        return self.coherence22.value
    def setCoherence22(self, coherence):
        self.coherence22.value = coherence
        return

    def getCoherence23(self):
        return self.coherence23.value
    def setCoherence23(self, coherence):
        self.coherence23.value = coherence
        return

    def getCoherence30(self):
        return self.coherence30.value
    def setCoherence30(self, coherence):
        self.coherence30.value = coherence
        return

    def getCoherence31(self):
        return self.coherence31.value
    def setCoherence31(self, coherence):
        self.coherence31.value = coherence
        return

    def getCoherence32(self):
        return self.coherence32.value
    def setCoherence32(self, coherence):
        self.coherence32.value = coherence
        return

    def getCoherence33(self):
        return self.coherence33.value
    def setCoherence33(self, coherence):
        self.coherence33.value = coherence
        return

    # Get and Set functions for Address
    def getAddress00(self):
        return self.address00.value
    def setAddress00(self, address):
        self.address00.value = address
        return

    def getAddress01(self):
        return self.address01.value
    def setAddress01(self, address):
        self.address01.value = address
        return

    def getAddress02(self):
        return self.address02.value
    def setAddress02(self, address):
        self.address02.value = address
        return

    def getAddress03(self):
        return self.address03.value
    def setAddress03(self, address):
        self.address03.value = address
        return

    def getAddress10(self):
        return self.address10.value
    def setAddress10(self, address):
        self.address10.value = address
        return

    def getAddress11(self):
        return self.address11.value
    def setAddress11(self, address):
        self.address11.value = address
        return

    def getAddress12(self):
        return self.address12.value
    def setAddress12(self, address):
        self.address12.value = address
        return

    def getAddress13(self):
        return self.address13.value
    def setAddress13(self, address):
        self.address13.value = address
        return

    def getAddress20(self):
        return self.address20.value
    def setAddress20(self, address):
        self.address20.value = address
        return

    def getAddress21(self):
        return self.address21.value
    def setAddress21(self, address):
        self.address21.value = address
        return

    def getAddress22(self):
        return self.address22.value
    def setAddress22(self, address):
        self.address22.value = address
        return

    def getAddress23(self):
        return self.address23.value
    def setAddress23(self, address):
        self.address23.value = address
        return

    def getAddress30(self):
        return self.address30.value
    def setAddress30(self, address):
        self.address30.value = address
        return

    def getAddress31(self):
        return self.address31.value
    def setAddress31(self, address):
        self.address31.value = address
        return

    def getAddress32(self):
        return self.address32.value
    def setAddress32(self, address):
        self.address32.value = address
        return

    def getAddress33(self):
        return self.address33.value
    def setAddress33(self, address):
        self.address33.value = address
        return

    # Get and Set functions for Data
    def getData00(self):
        return self.data00.value
    def setData00(self, data):
        self.data00.value = data
        return

    def getData01(self):
        return self.data01.value
    def setData01(self, data):
        self.data01.value = data
        return

    def getData02(self):
        return self.data02.value
    def setData02(self, data):
        self.data02.value = data
        return

    def getData03(self):
        return self.data03.value
    def setData03(self, data):
        self.data03.value = data
        return

    def getData10(self):
        return self.data10.value
    def setData10(self, data):
        self.data10.value = data
        return

    def getData11(self):
        return self.data11.value
    def setData11(self, data):
        self.data11.value = data
        return

    def getData12(self):
        return self.data12.value
    def setData12(self, data):
        self.data12.value = data
        return

    def getData13(self):
        return self.data13.value
    def setData13(self, data):
        self.data13.value = data
        return

    def getData20(self):
        return self.data20.value
    def setData20(self, data):
        self.data20.value = data
        return

    def getData21(self):
        return self.data21.value
    def setData21(self, data):
        self.data21.value = data
        return

    def getData22(self):
        return self.data22.value
    def setData22(self, data):
        self.data22.value = data
        return

    def getData23(self):
        return self.data23.value
    def setData23(self, data):
        self.data23.value = data
        return

    def getData30(self):
        return self.data30.value
    def setData30(self, data):
        self.data30.value = data
        return

    def getData31(self):
        return self.data31.value
    def setData31(self, data):
        self.data31.value = data
        return

    def getData32(self):
        return self.data32.value
    def setData32(self, data):
        self.data30.value = data
        return

    def getData33(self):
        return self.data33.value
    def setData33(self, data):
        self.data33.value = data
        return