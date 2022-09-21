import PySimpleGUI as sg
from multiprocessing import Process, Manager, Value, Lock
from tools import *
import instructionGenerator as instGen
from multiprocessing import Process, Manager, Value, Lock
import l1cache as l1c
import l1cacheDataHolder as l1cdh
import memory as mem
import instructionHolder as ih
import control as ctrl
import processor as proc

# UI element declaration
sg.theme("SandyBeach")

# Define blocks' layout

# Processor 0, column layout
processor0Col = [ [sg.Text(text="Processor #0", justification="center", font=("Any", 10))],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Executing: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="instructionP0")],
                [sg.Text(text="Last. Exec.: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="lastInstructionP0")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="L1 cache content", justification="center", font=("Any", 10))],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 0:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP0B0")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP0B0")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP0B0")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 1:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP0B1")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP0B1")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP0B1")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 2:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP0B2")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP0B2")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP0B2")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 3:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP0B3")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP0B3")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP0B3")],
                [sg.Text(text="|__________________________________________|", justification="center")] ]

# Processor 1, column layout
processor1Col = [ [sg.Text(text="Processor #1", justification="center", font=("Any", 10))],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Executing: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="instructionP1")],
                [sg.Text(text="Last. Exec.: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="lastInstructionP1")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="L1 cache content", justification="center", font=("Any", 10))],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 0:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP1B0")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP1B0")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP1B0")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 1:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP1B1")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP1B1")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP1B1")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 2:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP1B2")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP1B2")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP1B2")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 3:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP1B3")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP1B3")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP1B3")],
                [sg.Text(text="|__________________________________________|", justification="center")] ]

# Processor 2, column layout
processor2Col = [ [sg.Text(text="Processor #2", justification="center", font=("Any", 10))],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Executing: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="instructionP2")],
                [sg.Text(text="Last. Exec.: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="lastInstructionP2")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="L1 cache content", justification="center", font=("Any", 10))],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 0:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP2B0")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP2B0")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP2B0")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 1:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP2B1")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP2B1")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP2B1")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 2:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP2B2")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP2B2")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP2B2")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 3:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP2B3")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP2B3")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP2B3")],
                [sg.Text(text="|__________________________________________|", justification="center")] ]

# Processor 3, column layout
processor3Col = [ [sg.Text(text="Processor #3", justification="center", font=("Any", 10))],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Executing: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="instructionP3")],
                [sg.Text(text="Last. Exec.: ", justification="left", font=("Any", 10)), sg.Text(text="XXXXX XXX;XXXX", justification="right", font=("Any", 10), key="lastInstructionP3")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="L1 cache content", justification="center", font=("Any", 10))],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 0:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP3B0")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP3B0")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP3B0")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 1:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP3B1")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP3B1")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP3B1")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 2:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP3B2")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP3B2")],
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP3B2")],
                [sg.Text(text="|__________________________________________|", justification="center")],

                [sg.Text(text="Block 3:", justification="left", font=("Any", 10))],
                [sg.Text(text="Coherence State:", justification="left", font=("Any", 10)), sg.Text(text="X", justification="right", font=("Any", 10), key="l1coherenceP3B3")],
                [sg.Text(text="Mem. Adress:", justification="left", font=("Any", 10)), sg.Text(text="XXX", justification="right", font=("Any", 10), key="l1addressP3B3")], 
                [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="l1valueP3B3")],
                [sg.Text(text="|__________________________________________|", justification="center")] ]

# Whole memory blocks' layout
memBlock0 = [ [sg.Text(text="Address:", justification="left", font=("Any", 10)), sg.Text(text="0", justification="right", font=("Any", 10))],
              [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memValue0")] ]

memBlock1 = [ [sg.Text(text="Address:", justification="left", font=("Any", 10)), sg.Text(text="1", justification="right", font=("Any", 10))],
              [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memValue1")] ]

memBlock2 = [ [sg.Text(text="Address:", justification="left", font=("Any", 10)), sg.Text(text="2", justification="right", font=("Any", 10))],
              [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memValue2")] ]

memBlock3 = [ [sg.Text(text="Address:", justification="left", font=("Any", 10)), sg.Text(text="3", justification="right", font=("Any", 10))],
              [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memValue3")] ]

memBlock4 = [ [sg.Text(text="Address:", justification="left", font=("Any", 10)), sg.Text(text="4", justification="right", font=("Any", 10))],
              [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memValue4")] ]

memBlock5 = [ [sg.Text(text="Address:", justification="left", font=("Any", 10)), sg.Text(text="5", justification="right", font=("Any", 10))],
              [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memValue5")] ]

memBlock6 = [ [sg.Text(text="Address:", justification="left", font=("Any", 10)), sg.Text(text="6", justification="right", font=("Any", 10))],
              [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memValue6")] ]

memBlock7 = [ [sg.Text(text="Address:", justification="left", font=("Any", 10)), sg.Text(text="7", justification="right", font=("Any", 10))],
              [sg.Text(text="Value:", justification="left", font=("Any", 10)), sg.Text(text="0000", justification="right", font=("Any", 10), key="memValue7")] ]

# Define main layout
layout = [
    [sg.Text(text="General Controllers: ", size=(15, 1), justification="left", font=("Any", 10)),
     sg.Button(button_text="Pause", font=("Any", 10), disabled=False, key="pauseB"), 
     sg.Button(button_text="Step", font=("Any", 10), disabled=False, key="stepB")],

    [sg.Text(text="Add Instruction: ", size=(15, 1), justification="left", font=("Any", 10)),
     sg.InputText(disabled=False, key="newInstructionIn"), 
     sg.Button(button_text="Add", font=("Any", 10), disabled=False, key="addInstructionB")],

    [sg.Text(text="Select Mode: ", size=(15, 1), justification="left", font=("Any", 10)),
     sg.Button(button_text="Continuos Individual Execution", font=("Any", 10), disabled=False, key="individualB"), 
     sg.Button(button_text="Continuous Simultaneous Execution", font=("Any", 10), disabled=False, key="simultaneousB"),
     sg.Button(button_text="Generate Individual", font=("Any", 10), disabled=False, key="individualGenB"), 
     sg.Button(button_text="Generate Simultaneous", font=("Any", 10), disabled=False, key="simultaneousGenB")],

    [sg.Text(text="Execution time per instruction: ", justification="left", font=("Any", 10)), 
     sg.Text(text="XX", justification="center", font=("Any", 10), key="currentTime"),
     sg.Text(text=" seconds", justification="center", font=("Any", 10)),
     sg.InputText(disabled=False, key="executionTimeIn"), 
     sg.Button(button_text="Change Time", font=("Any", 10), disabled=False, key="changeExecutionTimeB")],

    [sg.Text(text="Status: ", size=(20, 1), justification="left", font=("Any", 10, "bold"))],
    [sg.Text(text="Last instruction generated: ", size=(20, 1), justification="left", font=("Any", 10)), 
     sg.Text(text="XX: XXXXX XXX;XXXX", justification="center", font=("Any", 10), key="lastInstruction")],
    [sg.Text(text="Next Instruction: ", size=(20, 1), justification="right", font=("Any", 10)), 
     sg.Text(text="XX: XXXXX XXX;XXXX", justification="center", font=("Any", 10), key="nextInstruction")],

    [sg.Text(text="<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->", size=(160, 1), justification="left")],

    [sg.Column(layout=processor0Col, element_justification="center"), 
     sg.Column(layout=processor1Col, element_justification="center"), 
     sg.Column(layout=processor2Col, element_justification="center"), 
     sg.Column(layout=processor3Col, element_justification="center")],

    [sg.Text(text="<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->", size=(160, 1), justification="left")],

    [
     [sg.Text(text="Memory Content:", size=(20, 1), justification="left", font=("Any", 10, "bold"))],
     sg.Column(layout=memBlock0, element_justification="center"), 
     sg.Column(layout=memBlock1, element_justification="center"), 
     sg.Column(layout=memBlock2, element_justification="center"), 
     sg.Column(layout=memBlock3, element_justification="center"), 
     sg.Column(layout=memBlock4, element_justification="center"), 
     sg.Column(layout=memBlock5, element_justification="center"), 
     sg.Column(layout=memBlock6, element_justification="center"), 
     sg.Column(layout=memBlock7, element_justification="center")]]

# Define window GUI with title
window = sg.Window(title="MESI Protocol for Multiprocessor Systems", layout=layout)

def createProcessorsAux(number, memory, instructionHolder, l1cacheDataHolder, mutex):
    processor = proc.Processor(number, memory, instructionHolder, l1cacheDataHolder, mutex, instGen.InstructionGenerator())
    processor.readOperation()

def createProcessors(memory, instructionHolder, l1cacheDataHolder, mutex):
    Process(target=createProcessorsAux, args=(0, memory, instructionHolder, l1cacheDataHolder, mutex,), daemon=True).start()
    Process(target=createProcessorsAux, args=(1, memory, instructionHolder, l1cacheDataHolder, mutex,), daemon=True).start()
    Process(target=createProcessorsAux, args=(2, memory, instructionHolder, l1cacheDataHolder, mutex,), daemon=True).start()
    Process(target=createProcessorsAux, args=(3, memory, instructionHolder, l1cacheDataHolder, mutex,), daemon=True).start() 
    return

# Main function of this program
def main():
    # Testing class
    manager = Manager()
    memory = mem.Memory(manager)
    l1cacheDataHolder = l1cdh.L1CacheDataHolder(manager)
    instructionHolder = ih.InstructionsHolder(manager)
    mutex = Lock()

    createProcessors(memory, instructionHolder, l1cacheDataHolder, mutex)

    generator = instGen.InstructionGenerator()
    instruction = ""
    pause = True
    individual = True

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "pauseB":
            window["individualB"].update(disabled=False)
            window["simultaneousB"].update(disabled=False)
            window["pauseB"].update(disabled=True)
            window["stepB"].update(disabled=False)
            window["individualGenB"].update(disabled=False)
            window["simultaneousGenB"].update(disabled=False)
            window["newInstructionIn"].update(disabled=False)
            window["addInstructionB"].update(disabled=False)
            pause = True
            individual = True
            instructionHolder.setInstruction0Read(1)
            instructionHolder.setInstruction1Read(1)
            instructionHolder.setInstruction2Read(1)
            instructionHolder.setInstruction3Read(1)
            instructionHolder.setAutoGeneratedInstruction0(0)
            instructionHolder.setAutoGeneratedInstruction1(0)
            instructionHolder.setAutoGeneratedInstruction2(0)
            instructionHolder.setAutoGeneratedInstruction3(0)

        if event == "individualB":
            window["individualB"].update(disabled=True)
            window["simultaneousB"].update(disabled=True)
            window["pauseB"].update(disabled=False)
            window["stepB"].update(disabled=True)
            window["individualGenB"].update(disabled=True)
            window["simultaneousGenB"].update(disabled=True)
            window["newInstructionIn"].update(disabled=True)
            window["addInstructionB"].update(disabled=True)
            pause = False
            individual = True

        if event == "simultaneousB":
            window["individualB"].update(disabled=True)
            window["simultaneousB"].update(disabled=True)
            window["pauseB"].update(disabled=False)
            window["stepB"].update(disabled=True)
            window["individualGenB"].update(disabled=True)
            window["simultaneousGenB"].update(disabled=True)
            window["newInstructionIn"].update(disabled=True)
            window["addInstructionB"].update(disabled=True)
            pause = False
            individual = False

        if event == "addInstructionB":
            instruction = values["newInstructionIn"].lower()
            window["nextInstruction"].update(instruction)
            individual = True

        if event == "stepB":
            if not (individual):
                instructionHolder.setInstruction0Read(0)
                instructionHolder.setInstruction1Read(0)
                instructionHolder.setInstruction2Read(0)
                instructionHolder.setInstruction3Read(0)
            elif (instruction != ""):
                if not analyzeInstruction(instruction, instructionHolder):
                    window["lastInstruction"].update(instruction)
                instruction = ""
                window["nextInstruction"].update(instruction)
            else:
                print("Set an instruction please.")

        if event == "individualGenB":
            individual = True
            instruction = generator.generateInstructionForProcessor()
            window["nextInstruction"].update(instruction)

        if event == "simultaneousGenB":
            individual = False
            instructionHolder.setAutoGeneratedInstruction0(1)
            instructionHolder.setAutoGeneratedInstruction1(1)
            instructionHolder.setAutoGeneratedInstruction2(1)
            instructionHolder.setAutoGeneratedInstruction3(1)

        if event == "changeExecutionTimeB":
            time = values["executionTimeIn"]
            if (time != ""):
                try:
                    time = int(time)
                    if (time < 100):
                        instructionHolder.setInstructionTime(time)
                    else:
                        print("Set a lower time please.\n")
                except:
                    print("Set a valid time please.\n")
            else:
                print("Set a time please\n")

        updateL1Data(window, l1cacheDataHolder, instructionHolder)        
        updateMemoryData(window, memory)

        if not pause:
            if individual and instructionHolder.getInstruction0Read() and instructionHolder.getInstruction1Read() and instructionHolder.getInstruction2Read() and instructionHolder.getInstruction3Read():
                instructionHolder.setAutoGeneratedInstruction0(0)
                instructionHolder.setAutoGeneratedInstruction1(0)
                instructionHolder.setAutoGeneratedInstruction2(0)
                instructionHolder.setAutoGeneratedInstruction3(0)
                instruction = generator.generateInstructionForProcessor()
                window["lastInstruction"].update(instruction)
                analyzeInstruction(instruction, instructionHolder)
            elif not individual:
                instructionHolder.setAutoGeneratedInstruction0(1)
                instructionHolder.setAutoGeneratedInstruction1(1)
                instructionHolder.setAutoGeneratedInstruction2(1)
                instructionHolder.setAutoGeneratedInstruction3(1)
                instructionHolder.setInstruction0Read(0)
                instructionHolder.setInstruction1Read(0)
                instructionHolder.setInstruction2Read(0)
                instructionHolder.setInstruction3Read(0)

    window.close()

if __name__ == "__main__":    
    main()