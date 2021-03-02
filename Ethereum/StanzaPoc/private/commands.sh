geth --exec "personal.unlockAccount(eth.accounts[0],\"1234\")" attach http://127.0.0.1:8545 
geth --exec "miner.start()" attach http://127.0.0.1:8545 
(cd ./truffle && truffle compile && truffle migrate)