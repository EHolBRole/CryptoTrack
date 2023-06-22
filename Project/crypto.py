from enums import Crypto

class CryptoCurrency:
<<<<<<< HEAD
    def __init__(self, name = "ETH", convertionType="USDT"):
        self.name = name
        self.type = name
        self.convertionType = convertionType
=======
    def __init__(self, type="BTC", convertionType="USDT"):
        self.type = type
        self.convertionType=convertionType

>>>>>>> 659b4b66d00d179f33ce860e8037f9aec0b6a5f4
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
