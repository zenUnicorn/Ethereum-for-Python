from web3 import Web3

url = "https://speedy-nodes-nyc.moralis.io/6c0d2f82056b058545553c5/eth/mainnet" #you can change the eth to bsc or avax
web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())

fromAddress = web3.toChecksumAddress('')
toAddress = web3.toChecksumAddress('')

privatekey = ""



nonce = web3.eth.getTransactionCount(fromAddress) #number of transactions, receiving address don't need a nonce only the sending address
#the transaction
tx = {
    'chainId': 56, #for BSC, you can get chainid on www.chainlist.org
    'nonce': nonce,
    'to': toAddress,
    'value': web3.toWei(0.05, 'ether'),
    'gas': 100000,
    'gasprice': web3.toWei(5, 'ether')
}

#We have to sign the transactiom
sign_tx = web3.eth.account.sign_transaction(tx, privatekey)

#Get the transaction hash
tx_hash = web3.eth.send_raw_transaction(sign_tx.raw_transaction)
print(web3.toHex(tx_hash))