from web3 import Web3

url = "https://speedy-nodes-nyc.moralis.io/6c0d2f82056b058545553c5/eth/mainnet" #you can change the eth to bsc or avax
web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())

#create account
account = web3.eth.account.create()

#another way is to import the Account class
from eth_account import Account
accounts = Account.create()
print(accounts.address)
print(web3.toHex(accounts.key))





