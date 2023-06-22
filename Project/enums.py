from enum import Enum


class Returns(Enum):
    NULL = 0
    EXIT = 1
    SHOW_CRYPTO_COURSE_GRAPH = 2
    SHOW_CRYPTO_COURSE_CURRENT = 3
    SHOW_SETTINGS = 4
    SELECT_BTC = 5
    SELECT_ETH = 6
    SELECT_BNB = 7
    SELECT_YFI = 8
    SELECT_LTC = 9
    SELECT_PAXG = 10
    pass


class Crypto(Enum):
    BTC = 0
    ETH = 1
    BNB = 2
    YFI = 3
    LTC = 4
    PAXG = 5
    pass
