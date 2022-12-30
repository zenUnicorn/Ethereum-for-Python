from web3 import Web3

url = "https://speedy-nodes-nyc.moralis.io/6c0d2f82056b058545553c5/eth/mainnet" #you can change the eth to bsc or avax
web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())

