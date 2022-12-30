#interacting with blockchain and working with the data themselves(Using Ethereum)
#We are getting information from the mainnet so we will use Infura,
import json
from web3 import Web3

#using infura to connect to an ethereum node
infura_url = "https://mainnet.infura.io/v3/8e741b80953647d3ae8c1bde742180f8"

#connecting to the blockchain
web3 = Web3(Web3.HTTPProvider(infura_url))
#Getting data
latest = web3.eth.blockNumber #the latest block number
print(latest)

getblock = web3.eth.getBlock(latest)
print(getblock)

#get a transaction usimng the hash
hash = '0x28623891fae4e7b52a329127c90dfbf2a1f8f806a5d7c314dee5a58288b38912'
print(web3.eth.getTransactionByBlock(hash, 2))


#building  Dapp without metamask
#first create a new account
account = web3.eth.account.create()
print(account.address)
print(web3.toHex(account.privateKey))
#We cant save the private key on the db, so we have to encrypt it

keystore = account.encrypt('password')
print(keystore)

#To decrypt the private key
web3.eth.account.decrypt(keystore, 'password')

#signing transactions
account.signTransaction()