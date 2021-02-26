import json
from web3 import Web3, HTTPProvider

class Client:

	def __init__(self, blockchain_address, compiled_contract_path, deployed_contract_address):
		
		with open(compiled_contract_path) as file:
			contract_json = json.load(file)  # load contract info as JSON
			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
		

		self.web3 = Web3(HTTPProvider(blockchain_address))
		self.web3.eth.defaultAccount = self.web3.eth.accounts[0]

		self.contract = self.web3.eth.contract(address=deployed_contract_address, abi=contract_abi)


	def addWorkspace(self, _id, _x, _y):
		self.contract.functions._creaPostazione(_id, _x, _y)
#call contract functions with self.contract.*function name*.*call()|transact()*

	

