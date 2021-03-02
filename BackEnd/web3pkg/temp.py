from BlockchainClient import Client
from time import sleep

client=Client(compiled_contract_path=r"C:\Users\ivanp\Desktop\uni\swe\git\swe-poc\Ethereum\StanzaPoc\private\truffle\build\contracts\SimpleStorage.json")

print(client.addWorkspace("posta101",10,10,"stato3"))

sleep(5)
print(client.getWorkspacePosition("posta101"))