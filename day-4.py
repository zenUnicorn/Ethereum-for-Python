#Interact with smart contract, Solidity, Ethereum, and python

import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

#the goal is to write the solidity code in remix, deploy it on ganache, copy the address, 
#copy the abi then interact with it using our python script

#copy and paste this code to remix.ethereum.org
'''
pragma solidity ^0.4.17;
contract Greeter {
    string public greeting;

    function GreeterClass() public {
        greeting = "Hello";
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() view public returns (string) {
        return greeting;
    }
}

'''
#gets ths first account on ganache and set is at the address we will be sending from.
web3.eth.defaultAccount = web3.eth.accounts[0]

#get this from remix
abi = json.loads('[{"constant":false,"inputs":[],"name":"GreeterClass","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')
address = web3.toChecksumAddress("0xC424c6ECe25C02c77C0e25bc9D3890Fb62B62cA0") #to check and format the address

contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.greet().call()) #this calls the greet function in the solidity code

tx_hash = contract.functions.setGreeting("Hello World!").transact() #let's set the greeting to something else using the setGreeting function 
print(web3.toHex(tx_hash))


#we have to get a receipt once the transction has been successful
web3.eth.waitForTransactionReceipt(tx_hash)

#print confirmation
print('Updated Greeting: {}'.format(
    contract.functions.greet().call()
)) 