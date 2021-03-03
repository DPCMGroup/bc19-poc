import json
from web3 import Web3, HTTPProvider
from time import sleep

class Client:


	def __init__(self, blockchain_address="http://127.0.0.1:8545", compiled_contract_path=r"../../Ethereum/StanzaPoc/private/truffle/build/contracts/SimpleStorage.json"):
		'''
		Costruisce un client per la comunicazione con la blockchain

		:param str blockchain_address: l'indirizzo, solitamente url, della blockchain
		:param str compiled_contract_path: percorso del contratto compilato (estensione .json)
		:param str deployed_contract_address: indirizzo del contratto sulla blockchain
		'''
		with open(compiled_contract_path) as file:
			contract_json = json.load(file)  # load contract info as JSON
			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			#print(contract_json['networks'])

			#['networks']['4224']['address'] il secondo valore cambia in base al networkid che specifichi quando inizializzi la blockchain (in startnode.sh) 
			address=contract_json['networks']['4224']['address']

		# Fetch deployed contract reference
		

		self.web3 = Web3(HTTPProvider(blockchain_address))
		self.web3.eth.defaultAccount = self.web3.eth.accounts[0]

		self.deployed_contract_address=address
		self.contract = self.web3.eth.contract(self.deployed_contract_address, abi=contract_abi)

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

	def getTransactionsHashes(self):
		#metodo molto lento

		x=1
		transs=[]
		while True:
			cur_block=self.web3.eth.get_block(x,full_transactions=False)
			print(x)
			if(len(cur_block.transactions)>0):
				transs+=cur_block.transactions
			x+=1
		
	'''
	def log_loop(self):
		event_filter = self.web3.eth.filter({'fromBlock':0, 'address':self.deployed_contract_address})
		while True:
			print("running")
			for event in event_filter.get_new_entries():
				print("got event")
				'''
				receipt = self.web3.eth.waitForTransactionReceipt(event['transactionHash'])
				result = contract.events.greeting.processReceipt(receipt)
				print(result[0]['args'])
				'''
			sleep(2)

	'''
	

