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
# L1CacheData from IPs/l1cache.py and processorInstructionData from instructionHolder.py
def updateL1Data(window):
    window["individualB"].update(disabled=False)
    print("individualB disabled")
    return

# Testing tools
#print (binaryToDecimal("101"))
#print (hexadecimalToDecimal("ab"))