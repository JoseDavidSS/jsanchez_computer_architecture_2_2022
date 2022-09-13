

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

# Functions as tools for GUI assests management.
# This function is used to update L1 cache data.
# L1CacheData from IPs/l1cache.py and processorInstructionData from instructionHolder.py
def updateL1Data(window):
    window["individualB"].update(disabled=False)
    print("individualB disabled")
    return