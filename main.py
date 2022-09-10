import PySimpleGUI as sg
from Tools import *

from entities.Tools.tools import updateL1Data

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
     sg.Button(button_text="Continuous Simultaneous Execution", font=("Any", 10), disabled=False, key="simultaneousB")],

    [sg.Text(text="Execution time per instruction: ", justification="left", font=("Any", 10)), 
     sg.Text(text="XX", justification="center", font=("Any", 10)),
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

# Main function of this program
def main():

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "pauseB":
            updateL1Data(window)

    window.close()

if __name__ == "__main__":    
    main()