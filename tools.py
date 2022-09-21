# Analyze instruction for each processors' delivery, gets instruction and instructionHolder as args.
def analyzeInstruction(instruction, procinstrdata):
    processor = instruction[:2]

    if (processor == "p0"):
        procinstrdata.setInstruction0(instruction[4:])
        procinstrdata.setInstruction0Read(0)
        return 0
    elif (processor == "p1"):
        procinstrdata.setInstruction1(instruction[4:])
        procinstrdata.setInstruction1Read(0)
        return 0
    elif (processor == "p2"):
        procinstrdata.setInstruction2(instruction[4:])
        procinstrdata.setInstruction2Read(0)
        return 0
    elif (processor == "p3"):
        procinstrdata.setInstruction3(instruction[4:])
        procinstrdata.setInstruction3Read(0)
        return 0
    else:
        print("Not a valid instruction, processor's name is wrong.\n")
        return 1

# Hexadecimal dictionary for convertion purposes.
hexadecimalDictionary = {"0": 0,
                         "1": 1,
                         "2": 2,
                         "3": 3,
                         "4": 4,
                         "5": 5,
                         "6": 6,
                         "7": 7,
                         "8": 8,
                         "9": 9,
                         "a": 10,
                         "b": 11,
                         "c": 12,
                         "d": 13,
                         "e": 14,
                         "f": 15}

# Binary dictionary for convertion purposes.           
binaryDictionary = {"0": 0,
                    "1": 1}

# Functions as tools for GUI data management.
# This functions turns objects sharers into strings for GUI data update purposes.
def listToString(sharers):
    if not (sharers):
        return ""
    else:
        return ",".join([str(proc) for proc in sharers])

# This function turns any decimal number into binary.
def decimalToBinary(decimalNumber):
    result = bin(decimalNumber).replace("0b", "")
    resultLen = len(result)
    while (resultLen != 3):
        result = "0" + result
        resultLen += 1

    return result

# This function turns any hexadecimal number into binary.
def decimalToHexadecimal(decimalNumber):
    result = hex(decimalNumber).replace("0x", "")
    resultLen = len(result)
    while (resultLen != 4):
        result = "0" + result
        resultLen += 1

    return result

# This function turns binary number (type str) into decimal number (type int).
def binaryToDecimal(binaryNumber):
    try:
        result = 0
        exp = 0
        binaryNumber = binaryNumber[::-1]
        for digit in binaryNumber:
            result += binaryDictionary.get(digit) * (2**exp)
            exp += 1
        return result
    except:
        print("P" + "str(self.number)" + ": Instruction memory address is not valid\n")
        return -1  

# This function turns hexadecimal number (type str) into decimal number (type int).
def hexadecimalToDecimal(hexadecimalNumber):
    try:    
        result = 0
        exp = 0
        hexadecimalNumber = hexadecimalNumber[::-1]
        for digit in hexadecimalNumber:
            result += hexadecimalDictionary.get(digit) * (16**exp)
            exp += 1
        return result
    except:
        print("P" + "str(self.number)" + ": Instruction data value is not valid\n")
        return -1

# Functions as tools for GUI assests management.
# This function is used to update L1 cache data.
def updateMemoryData(window, memory):
    memblock0 = memory.getBlock0()
    memblock1 = memory.getBlock1()
    memblock2 = memory.getBlock2()
    memblock3 = memory.getBlock3()
    memblock4 = memory.getBlock4()
    memblock5 = memory.getBlock5()
    memblock6 = memory.getBlock6()
    memblock7 = memory.getBlock7()

    window["memValue0"].update(decimalToHexadecimal(memblock0.getData()))
    window["memValue1"].update(decimalToHexadecimal(memblock1.getData()))
    window["memValue2"].update(decimalToHexadecimal(memblock2.getData()))
    window["memValue3"].update(decimalToHexadecimal(memblock3.getData()))
    window["memValue4"].update(decimalToHexadecimal(memblock4.getData()))
    window["memValue5"].update(decimalToHexadecimal(memblock5.getData()))
    window["memValue6"].update(decimalToHexadecimal(memblock6.getData()))
    window["memValue7"].update(decimalToHexadecimal(memblock7.getData()))

    return

def updateL1Data(window, l1cachedata, procinstrdata):
    window["currentTime"].update(procinstrdata.getInstructionTime())
    # For P0:
    window["instructionP0"].update(procinstrdata.getInstruction0())
    window["lastInstructionP0"].update(procinstrdata.getOldInstruction0())

    window["l1coherenceP0B0"].update(l1cachedata.getCoherence00())
    window["l1addressP0B0"].update(decimalToBinary(l1cachedata.getAddress00()))
    window["l1valueP0B0"].update(decimalToHexadecimal(l1cachedata.getData00()))

    window["l1coherenceP0B1"].update(l1cachedata.getCoherence01())
    window["l1addressP0B1"].update(decimalToBinary(l1cachedata.getAddress01()))
    window["l1valueP0B1"].update(decimalToHexadecimal(l1cachedata.getData01()))

    window["l1coherenceP0B2"].update(l1cachedata.getCoherence02())
    window["l1addressP0B2"].update(decimalToBinary(l1cachedata.getAddress02()))
    window["l1valueP0B2"].update(decimalToHexadecimal(l1cachedata.getData02()))

    window["l1coherenceP0B3"].update(l1cachedata.getCoherence03())
    window["l1addressP0B3"].update(decimalToBinary(l1cachedata.getAddress03()))
    window["l1valueP0B3"].update(decimalToHexadecimal(l1cachedata.getData03()))

    # For P1:
    window["instructionP1"].update(procinstrdata.getInstruction1())
    window["lastInstructionP1"].update(procinstrdata.getOldInstruction1())

    window["l1coherenceP1B0"].update(l1cachedata.getCoherence10())
    window["l1addressP1B0"].update(decimalToBinary(l1cachedata.getAddress10()))
    window["l1valueP1B0"].update(decimalToHexadecimal(l1cachedata.getData10()))

    window["l1coherenceP1B1"].update(l1cachedata.getCoherence11())
    window["l1addressP1B1"].update(decimalToBinary(l1cachedata.getAddress11()))
    window["l1valueP1B1"].update(decimalToHexadecimal(l1cachedata.getData11()))

    window["l1coherenceP1B2"].update(l1cachedata.getCoherence12())
    window["l1addressP1B2"].update(decimalToBinary(l1cachedata.getAddress12()))
    window["l1valueP1B2"].update(decimalToHexadecimal(l1cachedata.getData12()))
    
    window["l1coherenceP1B3"].update(l1cachedata.getCoherence13())
    window["l1addressP1B3"].update(decimalToBinary(l1cachedata.getAddress13()))
    window["l1valueP1B3"].update(decimalToHexadecimal(l1cachedata.getData13()))
    
    # For P2:
    window["instructionP2"].update(procinstrdata.getInstruction2())
    window["lastInstructionP2"].update(procinstrdata.getOldInstruction2())

    window["l1coherenceP2B0"].update(l1cachedata.getCoherence20())
    window["l1addressP2B0"].update(decimalToBinary(l1cachedata.getAddress20()))
    window["l1valueP2B0"].update(decimalToHexadecimal(l1cachedata.getData20()))

    window["l1coherenceP2B1"].update(l1cachedata.getCoherence21())
    window["l1addressP2B1"].update(decimalToBinary(l1cachedata.getAddress21()))
    window["l1valueP2B1"].update(decimalToHexadecimal(l1cachedata.getData21()))

    window["l1coherenceP2B2"].update(l1cachedata.getCoherence22())
    window["l1addressP2B2"].update(decimalToBinary(l1cachedata.getAddress22()))
    window["l1valueP2B2"].update(decimalToHexadecimal(l1cachedata.getData22()))

    window["l1coherenceP2B3"].update(l1cachedata.getCoherence23())
    window["l1addressP2B3"].update(decimalToBinary(l1cachedata.getAddress23()))
    window["l1valueP2B3"].update(decimalToHexadecimal(l1cachedata.getData23()))

    # For P3:
    window["instructionP3"].update(procinstrdata.getInstruction3())
    window["lastInstructionP3"].update(procinstrdata.getOldInstruction3())

    window["l1coherenceP3B0"].update(l1cachedata.getCoherence30())
    window["l1addressP3B0"].update(decimalToBinary(l1cachedata.getAddress30()))
    window["l1valueP3B0"].update(decimalToHexadecimal(l1cachedata.getData30()))

    window["l1coherenceP3B1"].update(l1cachedata.getCoherence31())
    window["l1addressP3B1"].update(decimalToBinary(l1cachedata.getAddress31()))
    window["l1valueP3B1"].update(decimalToHexadecimal(l1cachedata.getData31()))

    window["l1coherenceP3B2"].update(l1cachedata.getCoherence32())
    window["l1addressP3B2"].update(decimalToBinary(l1cachedata.getAddress32()))
    window["l1valueP3B2"].update(decimalToHexadecimal(l1cachedata.getData32()))
    
    window["l1coherenceP3B3"].update(l1cachedata.getCoherence33())
    window["l1addressP3B3"].update(decimalToBinary(l1cachedata.getAddress33()))
    window["l1valueP3B3"].update(decimalToHexadecimal(l1cachedata.getData33()))
    return
# Testing tools
#print (binaryToDecimal("101"))
#print (hexadecimalToDecimal("ab"))