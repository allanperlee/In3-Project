import in3
#address = "0x6C095A05764A23156eFD9D603eaDa144a9B1AF33"

client = in3.Client()
latest_block = client.eth.block_number()
gas_price = client.eth.gas_price()

client = in3.Client('kovan')
latest_block = client.eth.block_number()
gas_price = client.eth.gas_price()

client = in3.Client('goerli')
latest_block = client.eth.block_number()
gas_price = client.eth.gas_price()