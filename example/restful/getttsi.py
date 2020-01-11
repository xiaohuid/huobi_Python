from huobi import RequestClient
from datetime import date
from huobi.model import *
import talib
import numpy as np

request_client = RequestClient()

symbol_list = ["BTC"]

class ArrayManager(object):
    """
    For:
    1. time series container of bar data
    2. calculating technical indicator value
    """

    def __init__(self, size=100):
        """Constructor"""
        self.count = 0
        self.size = size
        self.inited = False

        self.open_array = np.zeros(size)
        self.high_array = np.zeros(size)
        self.low_array = np.zeros(size)
        self.close_array = np.zeros(size)
        self.volume_array = np.zeros(size)

    def update_bar(self, bar: list):
        """
        Update new bar data into array manager.
        """
        self.count += 1
        if not self.inited and self.count >= self.size:
            self.inited = True

        self.open_array[:-1] = self.open_array[1:]
        self.high_array[:-1] = self.high_array[1:]
        self.low_array[:-1] = self.low_array[1:]
        self.close_array[:-1] = self.close_array[1:]
        self.volume_array[:-1] = self.volume_array[1:]

        self.open_array[-1] = bar.open
        self.high_array[-1] = bar.high
        self.low_array[-1] = bar.low
        self.close_array[-1] = bar.close
        self.volume_array[-1] = bar.volume

    @property
    def open(self):
        """
        Get open price time series.
        """
        return self.open_array

    @property
    def high(self):
        """
        Get high price time series.
        """
        return self.high_array

    @property
    def low(self):
        """
        Get low price time series.
        """
        return self.low_array

    @property
    def close(self):
        """
        Get close price time series.
        """
        return self.close_array

    @property
    def volume(self):
        """
        Get trading volume time series.
        """
        return self.volume_array

    def sma(self, n, array=False):
        """
        Simple moving average.
        """
        result = talib.SMA(self.close, n)
        if array:
            return result
        return result[-1]

    def kama(self, n, array=False):
        """
        KAMA.
        """
        result = talib.KAMA(self.close, n)
        if array:
            return result
        return result[-1]

    def wma(self, n, array=False):
        """
        WMA.
        """
        result = talib.WMA(self.close, n)
        if array:
            return result
        return result[-1]

    def apo(self, n, array=False):
        """
        APO.
        """
        result = talib.APO(self.close, n)
        if array:
            return result
        return result[-1]

    def cmo(self, n, array=False):
        """
        CMO.
        """
        result = talib.CMO(self.close, n)
        if array:
            return result
        return result[-1]

    def mom(self, n, array=False):
        """
        MOM.
        """
        result = talib.MOM(self.close, n)
        if array:
            return result
        return result[-1]

    def ppo(self, n, array=False):
        """
        PPO.
        """
        result = talib.PPO(self.close, n)
        if array:
            return result
        return result[-1]

    def roc(self, n, array=False):
        """
        ROC.
        """
        result = talib.ROC(self.close, n)
        if array:
            return result
        return result[-1]

    def rocr(self, n, array=False):
        """
        ROCR.
        """
        result = talib.ROCR(self.close, n)
        if array:
            return result
        return result[-1]

    def rocp(self, n, array=False):
        """
        ROCP.
        """
        result = talib.ROCP(self.close, n)
        if array:
            return result
        return result[-1]

    def rocr_100(self, n, array=False):
        """
        ROCR100.
        """
        result = talib.ROCR100(self.close, n)
        if array:
            return result
        return result[-1]

    def trix(self, n, array=False):
        """
        TRIX.
        """
        result = talib.TRIX(self.close, n)
        if array:
            return result
        return result[-1]

    def std(self, n, array=False):
        """
        Standard deviation.
        """
        result = talib.STDDEV(self.close, n)
        if array:
            return result
        return result[-1]

    def obv(self, n, array=False):
        """
        OBV.
        """
        result = talib.OBV(self.close, self.volume)
        if array:
            return result
        return result[-1]

    def cci(self, n, array=False):
        """
        Commodity Channel Index (CCI).
        """
        result = talib.CCI(self.high, self.low, self.close, n)
        if array:
            return result
        return result[-1]

    def atr(self, n, array=False):
        """
        Average True Range (ATR).
        """
        result = talib.ATR(self.high, self.low, self.close, n)
        if array:
            return result
        return result[-1]

    def natr(self, n, array=False):
        """
        NATR.
        """
        result = talib.NATR(self.high, self.low, self.close, n)
        if array:
            return result
        return result[-1]

    def rsi(self, n, array=False):
        """
        Relative Strenght Index (RSI).
        """
        result = talib.RSI(self.close, n)
        if array:
            return result
        return result[-1]

    def macd(self, fast_period, slow_period, signal_period, array=False):
        """
        MACD.
        """
        macd, signal, hist = talib.MACD(
            self.close, fast_period, slow_period, signal_period
        )
        if array:
            return macd, signal, hist
        return macd[-1], signal[-1], hist[-1]

    def adx(self, n, array=False):
        """
        ADX.
        """
        result = talib.ADX(self.high, self.low, self.close, n)
        if array:
            return result
        return result[-1]

    def adxr(self, n, array=False):
        """
        ADXR.
        """
        result = talib.ADXR(self.high, self.low, self.close, n)
        if array:
            return result
        return result[-1]

    def dx(self, n, array=False):
        """
        DX.
        """
        result = talib.DX(self.high, self.low, self.close, n)
        if array:
            return result
        return result[-1]

    def minus_di(self, n, array=False):
        """
        MINUS_DI.
        """
        result = talib.MINUS_DI(self.high, self.low, self.close, n)
        if array:
            return result
        return result[-1]

    def plus_di(self, n, array=False):
        """
        PLUS_DI.
        """
        result = talib.PLUS_DI(self.high, self.low, self.close, n)
        if array:
            return result
        return result[-1]

    def willr(self, n, array=False):
        """
        WILLR.
        """
        result = talib.WILLR(self.high, self.low, self.close, n)
        if array:
            return result
        return result[-1]

    def ultosc(self, array=False):
        """
        Ultimate Oscillator.
        """
        result = talib.ULTOSC(self.high, self.low, self.close)
        if array:
            return result
        return result[-1]

    def trange(self, array=False):
        """
        TRANGE.
        """
        result = talib.TRANGE(self.high, self.low, self.close)
        if array:
            return result
        return result[-1]

    def boll(self, n, dev, array=False):
        """
        Bollinger Channel.
        """
        mid = self.sma(n, array)
        std = self.std(n, array)

        up = mid + std * dev
        down = mid - std * dev

        return up, down

    def keltner(self, n, dev, array=False):
        """
        Keltner Channel.
        """
        mid = self.sma(n, array)
        atr = self.atr(n, array)

        up = mid + atr * dev
        down = mid - atr * dev

        return up, down

    def donchian(self, n, array=False):
        """
        Donchian Channel.
        """
        up = talib.MAX(self.high, n)
        down = talib.MIN(self.low, n)

        if array:
            return up, down
        return up[-1], down[-1]

    def aroon(self, n, array=False):
        """
        Aroon indicator.
        """
        aroon_up, aroon_down = talib.AROON(self.high, self.low, n)

        if array:
            return aroon_up, aroon_down
        return aroon_up[-1], aroon_down[-1]

    def aroonosc(self, n, array=False):
        """
        Aroon Oscillator.
        """
        result = talib.AROONOSC(self.high, self.low, n)

        if array:
            return result
        return result[-1]

    def minus_dm(self, n, array=False):
        """
        MINUS_DM.
        """
        result = talib.MINUS_DM(self.high, self.low, n)

        if array:
            return result
        return result[-1]

    def plus_dm(self, n, array=False):
        """
        PLUS_DM.
        """
        result = talib.PLUS_DM(self.high, self.low, n)

        if array:
            return result
        return result[-1]

    def mfi(self, n, array=False):
        """
        Money Flow Index.
        """
        result = talib.MFI(self.high, self.low, self.close, self.volume, n)
        if array:
            return result
        return result[-1]

    def ad(self, n, array=False):
        """
        AD.
        """
        result = talib.AD(self.high, self.low, self.close, self.volume, n)
        if array:
            return result
        return result[-1]

    def adosc(self, n, array=False):
        """
        ADOSC.
        """
        result = talib.ADOSC(self.high, self.low, self.close, self.volume, n)
        if array:
            return result
        return result[-1]

    def bop(self, array=False):
        result = talib.BOP(self.open, self.high, self.low, self.close)
        if array:
            return result
        return result[-1]

    def td(self, array=False):
        close_np = self.close
        close_shift = np.empty_like(self.close)
        close_shift[:4] = 0
        close_shift[4:] = close_np[:-4]
        compare_array = close_np > close_shift
        result = np.empty(len(close_np), int)
        counting_number: int = 0
        for i in range(len(close_np)):
            if np.isnan(close_shift[i]):
                result[i] = 0
            else:
                compare_bool = compare_array[i]
                if compare_bool:
                    if counting_number >= 0:
                        counting_number += 1
                    else:
                        counting_number = 1
                else:
                    if counting_number <= 0:
                        counting_number -= 1
                    else:
                        counting_number = -1
                result[i] = counting_number
        if array:
            return result
        return result[-1]

    def td(self, array=False):
        close_np = self.close
        close_shift = np.empty_like(self.close)
        close_shift[:4] = 0
        close_shift[4:] = close_np[:-4]
        compare_array = close_np > close_shift
        result = np.empty(len(close_np), int)
        counting_number: int = 0
        for i in range(len(close_np)):
            if np.isnan(close_shift[i]):
                result[i] = 0
            else:
                compare_bool = compare_array[i]
                if compare_bool:
                    if counting_number >= 0:
                        counting_number += 1
                    else:
                        counting_number = 1
                else:
                    if counting_number <= 0:
                        counting_number -= 1
                    else:
                        counting_number = -1
                result[i] = counting_number
        if array:
            return result
        return result[-1]


class BollArray(object):
    """
    For:
    1. time series container of bar data
    2. calculating technical indicator value
    """

    def __init__(self, size=100):
        """Constructor"""
        self.count = 0
        self.size = size
        self.inited = False
        self.count = 0
        self.boll_up = 0
        self.boll_down = 0
        self.boll_mid = 0
        self.boll_up_cnt = 0
        self.boll_up_brk_cnt = 0
        self.boll_down_cnt = 0
        self.boll_down_brk_cnt = 0

        self.boll_up_array = np.zeros(size)
        self.boll_down_array = np.zeros(size)
        self.boll_mid_array = np.zeros(size)
        self.boll_up_cnt_array = np.zeros(size)
        self.boll_up_brk_cnt_array = np.zeros(size)
        self.boll_down_cnt_array = np.zeros(size)
        self.boll_down_brk_cnt_array = np.zeros(size)

    def update_boll(self, bar, am):
        """
        Update new bar data into array manager.
        """
        self.count += 1
        if not self.inited and self.count >= self.size:
            self.inited = True

        self.boll_up_array[:-1] = self.boll_up_array[1:]
        self.boll_down_array[:-1] = self.boll_down_array[1:]
        self.boll_mid_array[:-1] = self.boll_mid_array[1:]
        self.boll_up_cnt_array[:-1] = self.boll_up_cnt_array[1:]
        self.boll_up_brk_cnt_array[:-1] = self.boll_up_brk_cnt_array[1:]
        self.boll_down_cnt_array[:-1] = self.boll_down_cnt_array[1:]
        self.boll_down_brk_cnt_array[:-1] = self.boll_down_brk_cnt_array[1:]

        self.boll_up, self.boll_down = am.boll(20, 2)
        self.boll_mid = (self.boll_up + self.boll_down) / 2

        if bar.low_price > self.boll_mid:
            self.boll_up_cnt = self.boll_up_cnt + 1
            self.boll_down_cnt = 0
        else:
            self.boll_up_cnt = 0

        if bar.high_price < self.boll_mid:
            self.boll_down_cnt = self.boll_down_cnt + 1
            self.boll_up_cnt = 0
        else:
            self.boll_down_cnt = 0

        if bar.high_price > self.boll_up:
            self.boll_up_brk_cnt = self.boll_up_brk_cnt + 1
        else:
            self.boll_up_brk_cnt = 0

        if bar.low_price < self.boll_down:
            self.boll_down_brk_cnt = self.boll_down_brk_cnt + 1
        else:
            self.boll_down_brk_cnt = 0

        self.boll_up_array[-1] = self.boll_up
        self.boll_down_array[-1] = self.boll_down
        self.boll_mid_array[-1] = self.boll_mid
        self.boll_up_cnt_array[-1] = self.boll_up_cnt
        self.boll_up_brk_cnt_array[-1] = self.boll_up_brk_cnt
        self.boll_down_cnt_array[-1] = self.boll_down_cnt
        self.boll_down_brk_cnt_array[-1] = self.boll_down_brk_cnt

    def boll(self, array=False):

        if array:
            return self.boll_up_array, self.boll_up_cnt_array, self.boll_up_brk_cnt_array, self.boll_down_array, self.boll_down_cnt_array, self.boll_down_brk_cnt_array
        return self.boll_up, self.boll_up_cnt, self.boll_up_brk_cnt, self.boll_down, self.boll_down_cnt, self.boll_down_brk_cnt

    def to_str(self):
        tt: str = """ Boll Array
        self.boll_up: {}, self.boll_up_cnt: {}, self.boll_up_brk_cnt: {}, self.boll_down: {}, self.boll_down_cnt：{}, self.boll_down_brk_cnt：{}
        """.format(self.boll_up, self.boll_up_cnt, self.boll_up_brk_cnt, self.boll_down, self.boll_down_cnt, self.boll_down_brk_cnt)
        return tt



class MyEmailContent():

    def __init__(self):
        self.title = ''
        self.msg_array = []

    def set_subject(self, subject):
        self.title = subject

    def add_msg(self, msg):
        self.msg_array.append(msg)

    def get_msg(self):
        for aa in range(len(self.msg_array)):
            print(self.msg_array[aa])

    def msg(self):
        return self.msg_array


dd = MyEmailContent()

trade_statistics = request_client.get_ttsi('BTC', '60min')
ttmu2 = request_client.get_ttmu('BTC', '60min')
position2 = request_client.get_position('BTC', 'quarter', '60min', '48', '1')

dd.add_msg(trade_statistics[-1].to_str())
dd.add_msg(trade_statistics[-2].to_str())
dd.add_msg('TTSI buy_ratio： '+ str(round(trade_statistics[-1].buy_ratio - trade_statistics[-2].buy_ratio ,2 ) ))
dd.add_msg(ttmu2[-1].to_str())
dd.add_msg(ttmu2[-2].to_str())
dd.add_msg('TTMU buy_ratio： '+ str(round(ttmu2[-1].buy_ratio - ttmu2[-2].buy_ratio,2) ))
dd.add_msg(position2[0].to_str())
dd.add_msg(position2[1].to_str())
dd.add_msg('持仓量变化： '+ str(position2[0].volume - position2[1].volume ))

dd.get_msg()
# print("---- Ttmu ----")
#
# for tt in range(len(ttmu2)):
#     print(ttmu2[tt].to_str())
#
# for cc in range(len(position2)):
#     print(position2[cc].to_str())
candlestick_list_1 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN1, 100)
candlestick_list_5 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN5, 100)
candlestick_list_15 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN15, 100)
candlestick_list_30 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN30, 100)
candlestick_list_60 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN60, 100)
candlestick_list_1d = request_client.get_candlestick("BTC_CQ", CandlestickInterval.DAY1, 100)

am_1 = ArrayManager()
am_5 = ArrayManager()
am_15 = ArrayManager()
am_30 = ArrayManager()
am_60 = ArrayManager()
am_1d = ArrayManager()


ccc = np.zeros(150)
for cc in range(len(candlestick_list_1)) :
    am_1.update_bar(candlestick_list_1[cc])
    am_5.update_bar(candlestick_list_5[cc])
    am_15.update_bar(candlestick_list_15[cc])
    am_30.update_bar(candlestick_list_30[cc])
    am_60.update_bar(candlestick_list_60[cc])
    am_1d.update_bar(candlestick_list_1d[cc])

rsi = talib.RSI(am_1.close,6)
rsi5 = talib.RSI(am_5.close,6)
rsi15 = talib.RSI(am_15.close,6)
rsi30 = talib.RSI(am_30.close,6)
rsi60 = talib.RSI(am_60.close,6)
rsi1d = talib.RSI(am_1d.close,6)
print(am_1.rsi(6))
print(rsi5)
print(rsi15)
print(rsi30)
print(rsi60)
print(rsi1d)

print( am_1.td())
print( am_5.td())
print( am_15.td())
print( am_30.td())
print( am_60.td())
print( am_1d.td())



