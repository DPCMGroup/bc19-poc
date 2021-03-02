import json
from web3 import Web3, HTTPProvider

class Client:


	def __init__(self, blockchain_address="http://127.0.0.1:8545", compiled_contract_path=r"./Ethereum/StanzaPoc/private/truffle/build/contracts/SimpleStorage.json",deployed_contract_address="0xc6A3AeF3C1d5a707E08cc05ea99245976106072e"):
		'''
		Costruisce un client per la comunicazione con la blockchain

		:param str blockchain_address: l'indirizzo, solitamente url, della blockchain
		:param str compiled_contract_path: percorso del contratto compilato (estensione .json)
		:param str deployed_contract_address: indirizzo del contratto sulla blockchain
		'''
		with open(compiled_contract_path) as file:
			contract_json = json.load(file)  # load contract info as JSON
			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

		# Fetch deployed contract reference
		

		self.web3 = Web3(HTTPProvider(blockchain_address))
		self.web3.eth.defaultAccount = self.web3.eth.accounts[0]

		self.contract = self.web3.eth.contract(deployed_contract_address, abi=contract_abi)

	#call contract functions with self.contract.*function name*.*call()|transact()*

	'''
	.call() non memorizza alcuna transazione sulla blockchain, e quinid è gratuito. Va usato per leggere informazioni.
	.transact() memorizza una trasazione sulla blockchain, e quindi costa . Va usato per modificare informazioni.
	'''
	
	def setRoomDimensions(self, _x, _y):
		return self.contract.functions._setDimensioniStanza(_x, _y).transact()

	def addWorkspace(self, _id, _x, _y, _state):
		return self.contract.functions._creaPostazione(_id, _x, _y, _state).transact()

	def removeWorkspace(self, _id):
		return self.contract.functions._eliminaPostazione(_id).transact()

	def getWorkspacePosition(self, _id):
		return self.contract.functions.postazioni(_id).call()
		


	

