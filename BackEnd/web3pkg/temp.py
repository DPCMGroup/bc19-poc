from BlockchainClient import Client
import time

def func1(event):
	print(f"La transazione\n{event}\nè stata minata")

client = Client()
'''
client.sendTransaction("prova 1 2 3")
print("transaction sent")
'''

client.startListening(func1)
time.sleep(15)
client.stopListening()



