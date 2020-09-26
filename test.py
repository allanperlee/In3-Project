import in3

in3_client = in3.Client()

# Sends a request to the Incubed Network, that in turn will collect proofs from the Ethereum client, 
# attest and sign the response, then send back to the client, that will verify signatures and proofs. 
block_number = in3_client.eth.block_number()

