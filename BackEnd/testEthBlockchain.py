from web3pkg.BlockchainClient import Client

client = Client("http://127.0.0.1:8545")

print(client.getWorkspacePosition("123321"))