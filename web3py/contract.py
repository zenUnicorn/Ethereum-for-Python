from web3 import Web3

url = "https://speedy-nodes-nyc.moralis.io/6c0d2f82056b058545553c5/eth/mainnet" #you can change the eth to bsc or avax
web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())

#looking up information from smart contract
abi = "" #they are reusable for tokens on the same chain, just chnage the CA, but you can call a function using the wrong abi
contract_address = web3.toChecksumAddress("")

contract = web3.eth.contract(address=contract_address, abi=abi)
print(contract)

#now that we have the contract, we can call the functions in the contract.
name = contract.functions.name().call()
print(contract) #we can get the type (which is a class), then from the class we can get the name.
 
symbol = contract.functions.symbol().call()
print(symbol)

decimals = contract.functions.decimals().call()
print(decimals) #ether is 8 while BSC is 9

#we can get the accurate supply, instead of using (print(totalSupply/ 10 **9)), cos we may be working with muiltiple chains

DECIMAL = 10 **decimals

totalSupply = contract.functions.totalSupply().call()
print(totalSupply/ DECIMAL)

balancofaddy = contract.functions.balanceOf('address').call()
print(balancofaddy)

owner = contract.functions.owner().call()
print(owner)

#there are also some functions that takes in two parameters
allowance = contract.functions.allowance('','').call()
print(allowance)






