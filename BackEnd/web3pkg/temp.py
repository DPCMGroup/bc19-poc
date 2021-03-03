from BlockchainClient import Client
from time import sleep

client=Client(compiled_contract_path=r"C:\Users\ivanp\Desktop\uni\swe\git\swe-poc\Ethereum\StanzaPoc\private\truffle\build\contracts\SimpleStorage.json")

#print(client.addWorkspace("posta102",15,15,"stato3"))

#sleep(15)
#print(client.getWorkspacePosition("posta102"))

#print(client.getTransactionsHashes())

client.log_loop()


