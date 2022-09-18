import numpy as np
from tools import *

class InstructionGenerator:
    def __init__(self):
        self.generator = np.random.default_rng()

    # Función principal que genera la instrucción de manera aleatoria
    def generateInstructionForProcessor(self):

        processor = round(self.generator.uniform(0, 3))                 #Define de manera aleatoria a cuál procesador se le va a asignar la instrucción
        instructionType = round(self.generator.uniform(0, 2))           #Define de manera aleatoria el tipo de operación que va a generar 

        if (instructionType == 0):                                      # Si es 0, genera la instrucción "calc"
            instruction = self.generateCalc(processor, False)

        address = round(self.generator.uniform(0, 7))                   # Define la dirección de memoria de manera aleatoria

        if (instructionType == 1):                                      # Si es 1, genera la instrucción "read"
            instruction = self.generateRead(processor, address, False)

        if (instructionType == 2):                                      # Si es 2, genera la instrucción "write"
            data = round(self.generator.uniform(0, 65535))
            instruction = self.generateWrite(processor, address, data, False)
        return instruction

    # Función principal que genera la instrucción de manera aleatoria con procesador definido.
    def generateInstructionFromProcessor(self, processor):
        instructionType = round(self.generator.uniform(0, 2))
        if (instructionType == 0):
            instruction = self.generateCalc(processor, True)
        address = round(self.generator.uniform(0, 7))
        if (instructionType == 1):
            instruction = self.generateRead(processor, address, True)
        if (instructionType == 2):
            data = round(self.generator.uniform(0, 65535))
            instruction = self.generateWrite(processor, address, data, True)
        return instruction

    # Función principal que genera la instrucción "calc", caso 0.
    def generateCalc(self, processor, source):
        if not (source):
            return "p" + str(processor) + ": calc"
        else:
            return "calc"

    # Función principal que genera la instrucción "read", caso 1.
    def generateRead(self, processor, address, source):
        address = decimalToBinary(address)
        if not (source):
            return "p" + str(processor) + ": read " + address
        else:
            return "read " + address

    # Función principal que genera la instrucción "read", caso 2.
    def generateWrite(self, processor, address, data, source):
        address = decimalToBinary(address)
        data = decimalToHexadecimal(data)
        if not (source):
            return "p" + str(processor) + ": write " + address + ";" + data
        else:
            return "write " + address + ";" + data

# Testing class.
generator = InstructionGenerator()
print(generator.generateInstructionForProcessor())
print(generator.generateInstructionForProcessor())
print(generator.generateInstructionForProcessor())
print(generator.generateInstructionForProcessor())