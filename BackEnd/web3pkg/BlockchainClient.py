from web3 import Web3, HTTPProvider
from threading import Thread
import time

class Client:


	def __init__(self, blockchain_address = "http://127.0.0.1:8545"):
		'''
		Costruisce un client per la comunicazione con la blockchain
		:param str blockchain_address: l'indirizzo, solitamente url, della blockchain
		'''
		self.web3 = Web3(HTTPProvider(blockchain_address))
		self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
		#il tread che si sta utilizzando per ascoltare la blockchain, se esistente, altrimento None
		self.listeningThread = None
		#quando running è false e il thread lo legge, esso si ferma
		self.running = False



	def sendTransaction(self, dataString):
		'''
		Invia una transazione dall'account di default all'account di default con il parametro dataString, convertito in byte, come contenuto.
		Resituisce l'hash della transazione che verrà compiuta
		:param str dataString: la stringa da inviare come contenuto della transazione
		Restituisce l'hash della transazione
		'''
		byteData = bytes(dataString, 'utf-8')
		return self.web3.eth.send_transaction({'to': self.web3.eth.defaultAccount, 'from': self.web3.eth.defaultAccount, 'data': byteData})


	def addWorkspace(self, id, x, y):
		'''
		Restituisce l'hash della transazione
		'''
		return sendTransaction( f"\{ \"azione\": \"aggiungi postazione\", \"id postazione\": \"{id}\", \"x\": \"{x}\", \"y\":\"{y}\" \}" )

	def removeWorkspace(self, id):
		'''
		Restituisce l'hash della transazione
		'''
		return sendTransaction( f"\{ \"azione\": \"rimuovi postazione\", \"{id}\": \"post1\"\}" )

	def setWorkspaceState(self, id, state):
		'''
		Restituisce l'hash della transazione
		'''
		return sendTransaction( f"\{ \"azione\": \"imposta stato postazione\", \"id postazione\": \"{id}\", \"stato\": \"{state}\"\}" )


	def log_loop(self, event_filter, poll_interval, callback_function):
		'''
		:param event_filter: il filtro usato per sleezionare solo alcune tra tutte le transazioni che verranno minate
		:param float poll_interval: l'intervallo tra le ispezioni eseguite sulla blockchain per trovare nuove transazioni minate
		:param callback_function: la funziona che verrà chiamata quando verrà rilevata una transazione eseguita
		'''
	    while self.running and True:
	        for event in event_filter.get_new_entries():
	            callback_function(event)
	        time.sleep(poll_interval)
	    print("end of thread")
	


	def startListening(self, callback_function):
		'''
		:param callback_function: la funziona che verrà chiamata quando verrà rilevata una transazione minata.
									Vi si può passare anche una funzione esterna a questa classe.
		'''
		#block_filter = self.web3.eth.filter('latest')
		tx_filter = self.web3.eth.filter('pending')
		self.listeningThread = Thread(target=self.log_loop, args=(tx_filter, 5, callback_function), daemon=True) #daemon=True non so se sia la cosa giusta da usare
		self.running = True
		self.listeningThread.start()
		
		print("started listening")

	def stopListening(self):
		self.running = False
		self.listeningThread.join()
		self.listeningThread = None
		print("stopped listening")
    
	




	

