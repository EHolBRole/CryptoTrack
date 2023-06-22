from enums import Crypto
import crypto as cr


def change_coin_type(crypto_type):
    global coin
    if crypto_type == Crypto.BTC:
        coin = cr.CryptoCurrency('BTC')
    if crypto_type == Crypto.DOGE:
        coin = cr.CryptoCurrency('DOGE')
    if crypto_type == Crypto.ETH:
        coin = cr.CryptoCurrency('ETH')
    if crypto_type == Crypto.USDT:
        coin = cr.CryptoCurrency('USDT')
    pass


coin = cr.CryptoCurrency('USDT')


