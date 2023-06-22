from enums import Crypto
import crypto as cr


def change_coin_type(crypto_type):
    if crypto_type == Crypto.BTC:
        return cr.CryptoCurrency('BTC')
    if crypto_type == Crypto.BNB:
        return cr.CryptoCurrency('BNB')
    if crypto_type == Crypto.ETH:
        return cr.CryptoCurrency('ETH')
    if crypto_type == Crypto.YFI:
        return cr.CryptoCurrency('YFI')
    if crypto_type == Crypto.LTC:
        return cr.CryptoCurrency('LTC')
    if crypto_type == Crypto.PAXG:
        return cr.CryptoCurrency('PAXG')
    return "Exception"



