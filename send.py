import json
import in3
import time


# On Metamask, be sure to be connected to the correct chain, click on the `...` icon on the right corner of
# your Account name, select `Account Details`. There, click `Export Private Key`, copy the value to use as secret.
# By reading the terminal input, this value will stay in memory only. Don't forget to cls or clear terminal after ;)
sender_secret = input("Sender secret: ")
receiver = input("Receiver address: ")
#     1000000000000000000 == 1 ETH
#              1000000000 == 1 Gwei Check https://etherscan.io/gasTracker.
value_in_wei = 1463926659
# None for Eth mainnet
chain = 'kovan'
client = in3.Client(chain if chain else 'mainnet')
# A transaction is only final if a certain number of blocks are mined on top of it.
# This number varies with the chain's consensus algorithm. Time can be calculated over using:
# wait_time = blocks_for_consensus * avg_block_time_in_secs
# For mainnet and paying low gas, it might take 10 minutes.
confirmation_wait_time_in_seconds = 30
etherscan_link_mask = 'https://{}{}etherscan.io/tx/{}'

print('-= Ethereum Transaction using Incubed =- \n')
try:
    sender = client.eth.account.recover(sender_secret)
    tx = in3.eth.NewTransaction(to=receiver, value=value_in_wei)
    print('[.] Sending {} Wei from {} to {}. Please wait.\n'.format(tx.value, sender.address, tx.to))
    tx_hash = client.eth.account.send_transaction(sender, tx)
    print('[.] Transaction accepted with hash {}.'.format(tx_hash))
    add_dot_if_chain = '.' if chain else ''
    print(etherscan_link_mask.format(chain, add_dot_if_chain, tx_hash))
    while True:
        try:
            print('\n[.] Waiting {} seconds for confirmation.\n'.format(confirmation_wait_time_in_seconds))
            time.sleep(confirmation_wait_time_in_seconds)
            receipt: in3.eth.TransactionReceipt = client.eth.transaction_receipt(tx_hash)
            print('[.] Transaction was sent successfully!\n')
            print(json.dumps(receipt.to_dict(), indent=4, sort_keys=True))
            print('[.] Mined on block {} used {} GWei.'.format(receipt.blockNumber, receipt.gasUsed))
            break
        except Exception:
            print('[!] Transaction not mined yet, check https://etherscan.io/gasTracker.')
            print('[!] Just wait some minutes longer than the average for the price paid!')
except in3.PrivateKeyNotFoundException as e:
    print(str(e))
except in3.ClientException as e:
    print('Client returned error: ', str(e))
    print('Please try again.')
