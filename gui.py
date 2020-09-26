import PySimpleGUI as sg
from test import block_number

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Button("Print Ethereum's last block"), sg.Button('Exit')],
 ]

# Create the Window
window = sg.Window('Fetch Ethereum Data', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Print Ethereum's last block":
        sg.Print(block_number)

window.close()