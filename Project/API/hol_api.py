from binance.client import Client
import datetime
import pandas as pd
import datetime, time


class HOL_API:
    def __init__(self):
        self.client = Client()

    def GetHistoricalData(self, howLong, coin_type, interval):
        showLong = howLong
        # Calculate the timestamps for the binance api function
        untilThisDate = datetime.datetime.now()
        sinceThisDate = untilThisDate - datetime.timedelta(days = howLong)
        # Execute the query from binance - timestamps must be converted to strings !
        if interval == '1mt':
            candle = self.client.get_historical_klines(coin_type+"USDT", Client.KLINE_INTERVAL_1MONTH, str(sinceThisDate), str(untilThisDate))
        if interval == '1w':
            candle = self.client.get_historical_klines(coin_type+"USDT", Client.KLINE_INTERVAL_1WEEK, str(sinceThisDate), str(untilThisDate))
        elif interval == '1d':
            candle = self.client.get_historical_klines(coin_type+"USDT", Client.KLINE_INTERVAL_1DAY, str(sinceThisDate), str(untilThisDate))
        elif interval == '1h':
            candle = self.client.get_historical_klines(coin_type+"USDT", Client.KLINE_INTERVAL_1HOUR, str(untilThisDate), str(untilThisDate))
        elif interval == '1m':
            candle = self.client.get_historical_klines(coin_type+"USDT", Client.KLINE_INTERVAL_1MINUTE, str(untilThisDate), str(untilThisDate))
        else:
            return False

        # Create a dataframe to label all the columns returned by binance so we work with them later.
        df = pd.DataFrame(candle, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
        # as timestamp is returned in ms, let us convert this back to proper timestamps.
        if howLong < 365:
            df.dateTime = pd.to_datetime(df.dateTime, unit='ms').dt.strftime('%d,%m')
        else:
            df.dateTime = pd.to_datetime(df.dateTime, unit='ms').dt.strftime('%d,%m,%y')
        df.set_index('dateTime', inplace=True)

        # Get rid of columns we do not need
        df = df.drop(['closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol','takerBuyQuoteVol', 'ignore'], axis=1)
        dates = []
        values = []
        max_value = 0
        for ind in df.index:
            dates.append(ind)
        for value in df.get('high'):
            if float(value) > max_value:
                max_value = float(value)
            values.append(int(float(value)))
        pard = ParsedData(dates, values, max_value, len(dates))
        return pard


class ParsedData:
    def __init__(self, dates, values, max_value, format):
        self.dates = dates
        self.values = values
        self.max_value = max_value
        self.format = format
