from web3 import Web3

eth = "https://speedy-nodes-nyc.moralis.io/6c0d2f82056b058545553c5/eth/mainnet" #you can change the eth to bsc or avax
web3 = Web3(Web3.HTTPProvider(eth))
print(web3.isConnected())

balance = web3.eth.get_balance('0x05B4CCe36a206C8419B84C27Fd22bfAF64Adc268')
print(web3.fromWei(balance, 'ether'))

#transaction hash and the value sent in the transaction
tx = web3.eth.get_transaction('0x25ccd3f9e33bb62e3b703365fb3ab5388baccf85bb57ae39bc886c157bfa9f61')
print(tx['value'])

 