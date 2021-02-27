import json
from web3 import Web3, HTTPProvider

class Client:


	def __init__(self, blockchain_address, compiled_contract_path, deployed_contract_address):
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

		self.contract = self.web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

	#call contract functions with self.contract.*function name*.*call()|transact()*

	'''
	.call() non memorizza alcuna transazione sulla blockchain, e quinid è gratuito. Va usato per leggere informazioni.
	.transact() memorizza una trasazione sulla blockchain, e quindi costa . Va usato per modificare informazioni.
	'''
	
	def setRoomDimensions(self, _x, _y):
		self.contract.functions._setDimensioniStanza(_x, _y).transact()

	def addWorkspace(self, _id, _x, _y):
		self.contract.functions._creaPostazione(_id, _x, _y).transact()

	def removeWorkspace(self, _id):
		self.contract.functions._eliminaPostazione(_id).transact()

	def getWorkspacePosition(self, _id):
		mex = self.contract.functions.postazioni(_id).call()
		return mex


	

