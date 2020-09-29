import PySimpleGUI as sg
import send

sg.theme('Topanga')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys

layout = [
    [sg.Text('Please enter your Private Key, Amount, and Recipient Address')],
    [sg.Text('Private Key', size=(15, 1)), sg.InputText()],
    [sg.Text('Amount', size=(15, 1)), sg.InputText()],
    [sg.Text('Address', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Ethereum Transaction with Incubed', layout)
event, values = window.read()
window.close()
sender_secret = values[0]
receiver = values[1]
value_in_wei = values[2]  # the input data looks like a simple list when auto numbered

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    elif event == "Submit":
        sg.Print('[.] Sending {} Wei from {} to {}. Please wait.\n'.format(tx.value, sender.address, tx.to))
        
        if tx_hash != "":
            sg.Print('[.] Transaction accepted with hash {}.'.format(tx_hash))
            sg.Print(etherscan_link_mask.format(chain, add_dot_if_chain, tx_hash))
            
            if t_receipt == True:
                sg.Print('\n[.] Waiting {} seconds for confirmation.\n'.format(confirmation_wait_time_in_seconds))
                sg.Print('[.] Transaction was sent successfully!\n')
                sg.Print(json.dumps(receipt.to_dict(), indent=4, sort_keys=True))
                sg.Print('[.] Mined on block {} used {} GWei.'.format(receipt.blockNumber, receipt.gasUsed))
    

window.close()
