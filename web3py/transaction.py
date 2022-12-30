from web3 import Web3

#using moralis instead of infura
# XEceY8Qs9Bh7ihFQcEzVONv2ClhadHp46fHVQQD9WxZenC0p1aKT9Q9arYTp7YKj
eth = 'https://deep-index.moralis.io/api/v2'
web3 = Web3(Web3.HTTPProvider(eth))
print(web3.isConnected())
