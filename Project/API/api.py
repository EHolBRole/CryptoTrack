import requests
import datetime
import ciso8601
from crypto import CryptoCurrency as crypto


# it works onle when crypto_control.py file is near api.py


class API:
    def __init__(self, Url):
        self.url = Url

    def Get(self, param, path=""):
        return requests.get(self.url + path, params=param)

    def CryptoHistory(self, cryptoCurrency, StartTime):
        pass

    pass


class CryptoCompareAPI(API):
    def __init__(self, CurUrl, ApiKey=""):
        self.APIKey = "e36fb2eb6780b35f452822a0f457e755589be9020a8f957c645a3410f9bf2239"
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
    def __init__(self, CurUrl="https://api.binance.com"):
        super().__init__(CurUrl)

    def make_request(self, endpoint, params):
        response = self.Get(params, endpoint)
        if response.status_code == 200:
            return response
        return response
    def get_course(self, cryptoCurrency):
        path = "/api/v1/ticker/price"
        param = {
            "symbol": cryptoCurrency.type + cryptoCurrency.convertionType
        }
        print(param)
        return self.Get(param, path)

    def getHistoryData(self, cryptoCurrency=crypto(), Interval="1m", Time=3000, limit=10):
        endTime = datetime.datetime.now()
        startTime = (endTime - datetime.timedelta(seconds=Time)).timestamp()
        endTime = endTime.timestamp()
        path = "/api/v1/klines"
        params = {
            "symbol": cryptoCurrency.type + cryptoCurrency.convertionType,
            "interval": Interval,
            "limit": limit,
            #"startTime": str(int(startTime)),
            #"endTime": str(int(endTime))
        }
        return self.make_request(path, params)

    def CostChanges(self, cryptoCurrency):  # time == 24hours
        print(cryptoCurrency.type)
        path = "/api/v1/ticker/24hr"
        param = {
            "symbol": cryptoCurrency.type + cryptoCurrency.convertionType
        }
        print(param)
        return self.make_request(path, param)
