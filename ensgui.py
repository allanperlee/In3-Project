import PySimpleGUI as sg
import in3

#Tested the API with the "depraz.eth" domain and returned exactly what should be returned based on the In3 documentation

sg.theme('Topanga')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys

layout = [
    [sg.Text('Please enter Domain')],
    [sg.Text('Domain', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Resolve ENS to an Ethereum Address', layout)  

while True:                             # The Event Loop
    event, values = window.read()
    def _print():
        sg.Print('\nAddress for {} @ {}: {}'.format(domain, chain, address))
        sg.Print('Owner for {} @ {}: {}'.format(domain, chain, owner))
    
    domain = str(values[0])

    # Instantiate In3 Client for Goerli
    chain = 'goerli'
    client = in3.Client(chain, cache_enabled=False)
    address = client.ens_address(domain)
    owner = client.ens_owner(domain)
    _print()

    # Instantiate In3 Client for Mainnet
    chain = 'mainnet'
    client = in3.Client(chain, cache_enabled=False)
    address = client.ens_address(domain)
    owner = client.ens_owner(domain)
    _print()

    # Instantiate In3 Client for Kovan
    chain = 'kovan'
    client = in3.Client(chain, cache_enabled=True)
    try:
        address = client.ens_address(domain)
        owner = client.ens_owner(domain)
    except in3.ClientException:
        sg.Print('\nENS is not available on Kovan.')   


window.close()