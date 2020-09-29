import json
import in3
import time

sender_secret = ""
receiver = ""
#     1000000000000000000 == 1 ETH
#              1000000000 == 1 Gwei Check https://etherscan.io/gasTracker.
value_in_wei = 0
# None for Eth mainnet
chain = 'goerli'
client = in3.Client(chain if chain else 'mainnet')
# A transaction is only final if a certain number of blocks are mined on top of it.
# This number varies with the chain's consensus algorithm. Time can be calculated over using:
# wait_time = blocks_for_consensus * avg_block_time_in_secs
# For mainnet and paying low gas, it might take 10 minutes.
confirmation_wait_time_in_seconds = 30
etherscan_link_mask = 'https://{}{}etherscan.io/tx/{}'

try:
    sender = client.eth.account.recover(sender_secret)
    tx = in3.eth.NewTransaction(to=receiver, value=value_in_wei)
    
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