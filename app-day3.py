from web3 import Web3

#Day 3
#How to send transactions on Ethereum with python.We will use ganache a local node provider.
ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

#We want to send assets from account_1 to account_2 using account_1 private keys - all details gotten from Ganache 
account_1 = "0x63466D0E2F980d0a851c8bCeD108d53E238eaA04"
account_2 = "0xF5714F32C77bEc24b2Cff1Af56DBcE4d29d7e841"

private_key = "176d37723e86781b5cb907fd24f8d7a79e01431e4864b02d7e3b188b45e4d814"

#get the nonce - this helps you not to send a transaction twice
nonce = web3.eth.getTransactionCount(account_1)

#build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei(50, 'gwei')
}

#sign a transaction
sign_tx = web3.eth.account.signTransaction(tx, private_key)

#send transaction
tx_hash = web3.eth.sendRawTransaction(sign_tx.rawTransaction)

#get transaction hash
print(web3.toHex(tx_hash))


