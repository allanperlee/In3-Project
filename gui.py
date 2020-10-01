import PySimpleGUI as sg
from test import client, latest_block, gas_price

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
[sg.Button("Ethereum Main Network")],
[sg.Button("Kovan Test Network")],
[sg.Button("Goerli Test Network")],
[sg.Button("Send Transaction")],
[sg.Button("Resolve ENS")],
[sg.Button("List of Nodes")],
[sg.Button("Exit")]
 ]

# Create the Window
window = sg.Window('Fetch Ethereum Data', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == "Ethereum Main Network":
        sg.Print('Latest BN: {}\nGas Price: {} Wei'.format(latest_block, gas_price))
    elif event == "Kovan Test Network":
        sg.Print('Latest BN: {}\nGas Price: {} Wei'.format(latest_block, gas_price))
    elif event == "Goerli Test Network":
        sg.Print('Latest BN: {}\nGas Price: {} Wei'.format(latest_block, gas_price))
    elif event == "Send Transaction":
        exec(open('dp2.py').read())
    elif event == "Resolve ENS":
        exec(open('ensgui.py').read())
    else:
        exec(open('uinodes.py').read())
    

window.close()