from enums import Crypto

class CryptoCurrency:
    def __init__(self, type="BTC", convertionType="USDT"):
        self.type = type
        self.convertionType=convertionType

    pass


def change_coin_type(crypto_type):
    if crypto_type == Crypto.BTC:
        return CryptoCurrency('BTC')
    if crypto_type == Crypto.BNB:
        return CryptoCurrency('BNB')
    if crypto_type == Crypto.ETH:
        return CryptoCurrency('ETH')
    if crypto_type == Crypto.WTC:
        return CryptoCurrency('WTC')

