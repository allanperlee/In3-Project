import PySimpleGUI as sg
import json
import in3
import time

# Tested the UI with a Private Key provided by Ganache CLI and kept asking for the sender secret, still needs to be tested with a real private key

sg.theme('Topanga')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys

layout = [
    [sg.Text('Please enter your Private Key, Amount, Recipient, & Chain')],
    [sg.Text('Private Key', size=(15, 1)), sg.InputText()],
    [sg.Text('Amount', size=(15, 1)), sg.InputText()],
    [sg.Text('Recipient', size=(15, 1)), sg.InputText()],
    [sg.Text('Chain', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

sender_secret = ""
receiver = ""
#     1000000000000000000 == 1 ETH
#              1000000000 == 1 Gwei Check https://etherscan.io/gasTracker.
value_in_wei = 0

# A transaction is only final if a certain number of blocks are mined on top of it.
# This number varies with the chain's consensus algorithm. Time can be calculated over using:
# wait_time = blocks_for_consensus * avg_block_time_in_secs
# For mainnet and paying low gas, it might take 10 minutes.
confirmation_wait_time_in_seconds = 30
etherscan_link_mask = 'https://{}{}etherscan.io/tx/{}'

window = sg.Window('Send Ether with In3', layout)


# Event Loop to process "events" and get the "values" of the inputs
while True:                             # The Event Loop
    event, values = window.read()
    sender_secret = str(values[0])
    value_in_wei = values[1]  # the input data looks like a simple list when auto numbered
    receiver = str(values[2])
    chain = str(values[3])
    client = in3.Client(chain)

    if event == "Submit":
        try:
            sender = client.eth.account.recover(sender_secret)
            tx = in3.eth.NewTransaction(to=receiver, value=value_in_wei)
            sg.Print('[.] Sending {} Wei from {} to {}. Please wait.\n'.format(tx.value, sender.address, tx.to))
            tx_hash = client.eth.account.send_transaction(sender, tx)
            sg.Print('[.] Transaction accepted with hash {}.'.format(tx_hash))
            add_dot_if_chain = '.' if chain else ''
            sg.Print(etherscan_link_mask.format(chain, add_dot_if_chain, tx_hash))
            while True:
                try:
                    sg.Print('\n[.] Waiting {} seconds for confirmation.\n'.format(confirmation_wait_time_in_seconds))
                    time.sleep(confirmation_wait_time_in_seconds)
                    receipt: in3.eth.TransactionReceipt = client.eth.transaction_receipt(tx_hash)
                    sg.Print('[.] Transaction was sent successfully!\n')
                    sg.Print(json.dumps(receipt.to_dict(), indent=4, sort_keys=True))
                    sg.Print('[.] Mined on block {} used {} GWei.'.format(receipt.blockNumber, receipt.gasUsed))
                    break
                except Exception:
                    sg.Print('[!] Transaction not mined yet, check https://etherscan.io/gasTracker.')
                    sg.Print('[!] Just wait some minutes longer than the average for the price paid!')
        except in3.PrivateKeyNotFoundException as e:
            sg.Print(str(e))
        except in3.ClientException as e:
            sg.Print('Client returned error: ', str(e))
            sg.Print('Please try again.')
    else:
        break
window.close()