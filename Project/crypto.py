from enums import Crypto


class CryptoCurrency:
    def __init__(self, type="BTC", convertionType="USDT"):
        self.type = type
        self.convertionType=convertionType
    pass


def change_coin_type(crypto_type):
    global coin
    if crypto_type == Crypto.BTC:
        coin = CryptoCurrency('BTC')
    if crypto_type == Crypto.DOGE:
        coin = CryptoCurrency('DOGE')
    if crypto_type == Crypto.ETH:
        coin = CryptoCurrency('ETH')
    if crypto_type == Crypto.USDT:
        coin = CryptoCurrency('USDT')
    pass


coin = CryptoCurrency('USDT')

