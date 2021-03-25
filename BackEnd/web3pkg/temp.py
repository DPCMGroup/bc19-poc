from BlockchainClient import Client
import time

def func1(receipt, transaction):
	'''
	print("receipt")
	print(receipt)
	print("transaction")
	print(transaction)
	'''
	blockNumber = receipt['blockNumber']
	status = receipt['status']
	hsh = receipt['transactionHash']
	stringHash = "0x" + "".join([hex(b)[2:] for b in bytearray(hsh)])
	data = transaction['input']
	print(f"La transazione\n{stringHash}\nè stata minata con esito: {status} nel blocco {blockNumber}. \nIl suo contenuto è \n{data}")
	#print(event['status'])

def failedFunc():
	print("la transazione è in attesa da troppo tempo, forse c'è stato un errore")



client = Client()


tx_hash = client.hashAndSendData("prova prova prova")
#print(tx_hash)
print("transaction sent")
time.sleep(3)

client.startListening(tx_hash, func1, failedFunc)

time.sleep(150)



