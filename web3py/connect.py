import moralis
from moralis import evm_api
from web3 import Web3

eth = ""
web3 = Web3(Web3.HTTPProvider(eth))
print(web3.isConnected())

block = web3.eth.get_block('latest')
print(block)

block_num = web3.eth.get_block_number
print(block_num)




#using moralis instead of infura
api_key = "XEceY8Qs9Bh7ihFQcEzVONv2ClhadHp46fHVQQD9WxZenC0p1aKT9Q9arYTp7YKj"

# it prints {'version': '0.0.53'}
print(moralis.utils.web3_api_version(api_key='XEceY8Qs9Bh7ihFQcEzVONv2ClhadHp46fHVQQD9WxZenC0p1aKT9Q9arYTp7YKj'))

params = {
    "address": "0x05B4CCe36a206C8419B84C27Fd22bfAF64Adc268", 
    "chain": "eth", 
}

result = evm_api.balance.get_native_balance(
    api_key=api_key,
    params=params,
)

print(result)


