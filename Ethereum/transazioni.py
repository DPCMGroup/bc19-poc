import json
from web3 import Web3, HTTPProvider

class Client:
	def __init__(self, blockchain_address = "http://127.0.0.1:8545"):
		

		self.web3 = Web3(HTTPProvider(blockchain_address))
		self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
		#print("my account: "+self.web3.eth.defaultAccount)
	
	def sendData(self, string):
		res = bytes(string, 'utf-8')
		#print(res)
		hexString = bytes.hex(res)
		#print(hexString)
		return self.web3.eth.send_transaction({'to': self.web3.eth.defaultAccount, 'from': self.web3.eth.defaultAccount, 'value': 12345, 'data': hexString})



client = Client()

print(client.sendData("ciao"))


	

