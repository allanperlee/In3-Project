import PySimpleGUI as sg
import in3

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
[sg.Button("Mainnet")],
[sg.Button("Kovan")],
[sg.Button("Goerli")],
[sg.Button("EWC")],
[sg.Button("Exit")]
 ]

# Create the Window
window = sg.Window('Fetch Ethereum Data', layout)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == "Mainnet":
        # on every event, the client is instantiated differently and the list of client nodes are refreshed
        client = in3.Client("Mainnet")
        node_list = client.refresh_node_list()

        sg.Print('\nIncubed Registry:')
        sg.Print('\ttotal servers:{}'.format(node_list.totalServers))
        sg.Print('\tlast updated in block:{}'.format(node_list.lastBlockNumber))
        sg.Print('\tregistry ID:{}'.format(node_list.registryId))
        sg.Print('\tcontract address:{}'.format(node_list.contract))
        sg.Print('\nNodes Registered:\n')
        for node in node_list.nodes:
            sg.Print('\turl:{}'.format(node.url))
            sg.Print('\tdeposit:', node.deposit)
            sg.Print('\tweight:', node.weight)
            sg.Print('\tregistered in block:', node.registerTime)
            sg.Print('\n')

    elif event == "Kovan":
        client = in3.Client("Kovan")
        node_list = client.refresh_node_list()

        sg.Print('\nIncubed Registry:')
        sg.Print('\ttotal servers:{}'.format(node_list.totalServers))
        sg.Print('\tlast updated in block:{}'.format(node_list.lastBlockNumber))
        sg.Print('\tregistry ID:{}'.format(node_list.registryId))
        sg.Print('\tcontract address:{}'.format(node_list.contract))
        sg.Print('\nNodes Registered:\n')
        for node in node_list.nodes:
            sg.Print('\turl:{}'.format(node.url))
            sg.Print('\tdeposit:', node.deposit)
            sg.Print('\tweight:', node.weight)
            sg.Print('\tregistered in block:', node.registerTime)
            sg.Print('\n')

    elif event == "Goerli":
        client = in3.Client("Goerli")
        node_list = client.refresh_node_list()
        
        sg.Print('\nIncubed Registry:')
        sg.Print('\ttotal servers:{}'.format(node_list.totalServers))
        sg.Print('\tlast updated in block:{}'.format(node_list.lastBlockNumber))
        sg.Print('\tregistry ID:{}'.format(node_list.registryId))
        sg.Print('\tcontract address:{}'.format(node_list.contract))
        sg.Print('\nNodes Registered:\n')
        for node in node_list.nodes:
            sg.Print('\turl:{}'.format(node.url))
            sg.Print('\tdeposit:', node.deposit)
            sg.Print('\tweight:', node.weight)
            sg.Print('\tregistered in block:', node.registerTime)
            sg.Print('\n')

    elif event == "EWC":
        client = in3.Client("EWC")
        node_list = client.refresh_node_list()

        sg.Print('\nIncubed Registry:')
        sg.Print('\ttotal servers:{}'.format(node_list.totalServers))
        sg.Print('\tlast updated in block:{}'.format(node_list.lastBlockNumber))
        sg.Print('\tregistry ID:{}'.format(node_list.registryId))
        sg.Print('\tcontract address:{}'.format(node_list.contract))
        sg.Print('\nNodes Registered:\n')
        for node in node_list.nodes:
            sg.Print('\turl:{}'.format(node.url))
            sg.Print('\tdeposit:', node.deposit)
            sg.Print('\tweight:', node.weight)
            sg.Print('\tregistered in block:', node.registerTime)
            sg.Print('\n')
    else:
        break
    

window.close()