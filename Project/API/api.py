import requests
from crypto import CryptoCurrency  as crypto 
#it works onle when crypto.py file is near api.py


class API:
    def __init__ (self, Url):
        self.url = Url
    def Get(self, param, path = ""):
        return requests.get(self.url + path, params=param)
    def CryptoHistory(cryptoCurrency, StartTime):
        pass
    pass

class CryptoCompareAPI(API):
    def __init__(self, CurUrl, ApiKey = ""):
        self.APIKey="e36fb2eb6780b35f452822a0f457e755589be9020a8f957c645a3410f9bf2239"
        super().__init__(CurUrl)
    def CurrentCost(self, cryptoCurrency):
        print(cryptoCurrency.type)
        param = {
            "fsym": cryptoCurrency.type,
            "tsyms": cryptoCurrency.convertionType,
            "api_key": self.APIKey
        }        
        return self.Get(param)        
class BinanceAPI(API):
    def __init__(self, CurUrl = "https://fapi.binance.com"):
        super().__init__(CurUrl)
    def CurrentCost(self, cryptoCurrency):
        print(cryptoCurrency.type)
        path = "/fapi/v1/ticker/price"
        param = {
            "symbol": cryptoCurrency.type + cryptoCurrency.convertionType
        }        
        print(param)
        return self.Get(param, path)        
    
    def CostChanges(self, cryptoCurrency): # time == 24hours
        print(cryptoCurrency.type)
        path = "/fapi/v1/ticker/24hr"
        param = {
            "symbol": cryptoCurrency.type + cryptoCurrency.convertionType
        }        
        print(param)
        return self.Get(param, path)        
    