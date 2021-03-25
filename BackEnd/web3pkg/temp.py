from BlockchainClient import Client
import time

def func1(event):
	#print(event)
	status = event['status']
	hsh = event['transactionHash']
	print(f"La transazione\n{hsh}\nè stata minata con esito: {status}")
	#print(event['status'])


client = Client();

tx_hash = client.hashAndSendData("prova 1 2 3");
print(tx_hash)
print("transaction sent")
time.sleep(3)

client.startListening(tx_hash, func1)

time.sleep(150)
#print(client.isAlive())

#time.sleep(150)
#client.stopListening()



