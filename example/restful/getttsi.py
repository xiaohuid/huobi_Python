from huobi import RequestClient
from datetime import datetime
from huobi.model import *
import talib
import numpy as np
import matplotlib.pyplot as plt
from huobi.model.bararray import BarArray
from huobi.model.tradeinfoarray import TradeInfoArray
from huobi.impl.utils.emailsender import MyEmailContent

request_client = RequestClient()
dd = MyEmailContent()

# ########## 1 min data ############
candlestick_list_1 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN1, 100)
am_1 = BarArray()
am_1.update_candle(candlestick_list_1)
boll_1 = TradeInfoArray(1)
boll_1.update_boll_array(candlestick_list_1, am_1)

# ########## 5 min data ############
ttsi_5 = request_client.get_ttsi('BTC', '5min')
ttmu_5 = request_client.get_ttmu('BTC', '5min')
candlestick_list_5 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN5, 100)
am_5 = BarArray()
am_5.update_candle(candlestick_list_5)
boll_5 = TradeInfoArray(1)
boll_5.update_ttmu(ttmu_5)
boll_5.update_ttsi(ttsi_5)
boll_5.update_boll_array(candlestick_list_5, am_5)

# ########## 15 min data ############
ttsi_15 = request_client.get_ttsi('BTC', '15min')
ttmu_15 = request_client.get_ttmu('BTC', '15min')
candlestick_list_15 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN15, 100)
am_15 = BarArray()
am_15.update_candle(candlestick_list_15)
boll_15 = TradeInfoArray(1)
boll_15.update_ttmu(ttmu_15)
boll_15.update_ttsi(ttsi_15)
boll_15.update_boll_array(candlestick_list_15, am_15)

# ########## 30 min data ############
ttsi_30 = request_client.get_ttsi('BTC', '30min')
ttmu_30 = request_client.get_ttmu('BTC', '30min')
candlestick_list_30 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN30, 100)
am_30 = BarArray()
am_30.update_candle(candlestick_list_30)
boll_30 = TradeInfoArray(1)
boll_30.update_ttmu(ttmu_30)
boll_30.update_ttsi(ttsi_30)
boll_30.update_boll_array(candlestick_list_30, am_30)

# ########## 60 min data ############
ttsi_60 = request_client.get_ttsi('BTC', '60min')
ttmu_60 = request_client.get_ttmu('BTC', '60min')
pos_60 = request_client.get_position('BTC', 'quarter', '60min', '48', '1')
candlestick_list_60 = request_client.get_candlestick("BTC_CQ", CandlestickInterval.MIN60, 100)
am_60 = BarArray()
am_60.update_candle(candlestick_list_60)
boll_60 = TradeInfoArray(1)
boll_60.update_all(ttsi_60, ttmu_60, pos_60, candlestick_list_60, am_60)

# ########## 4 hours ############
ttsi_4h = request_client.get_ttsi('BTC', '4hour')
ttmu_4h = request_client.get_ttmu('BTC', '4hour')
pos_4h = request_client.get_position('BTC', 'quarter', '4hour', '48', '1')
candlestick_list_4h = request_client.get_candlestick("BTC_CQ", CandlestickInterval.HOUR4, 100)
am_4h = BarArray()
am_4h.update_candle(candlestick_list_4h)
boll_4h = TradeInfoArray(1)
boll_4h.update_all(ttsi_4h, ttmu_4h, pos_4h, candlestick_list_4h, am_4h)

# ########## 1d min data ############
ttsi_1d = request_client.get_ttsi('BTC', '1day')
ttmu_1d = request_client.get_ttmu('BTC', '1day')
pos_1d = request_client.get_position('BTC', 'quarter', '1day', '48', '1')
candlestick_list_1d = request_client.get_candlestick("BTC_CQ", CandlestickInterval.DAY1, 100)
am_1d = BarArray()
am_1d.update_candle(candlestick_list_1d)
boll_1d = TradeInfoArray(1)
boll_1d.update_all(ttsi_1d, ttmu_1d, pos_1d, candlestick_list_1d, am_1d)

# ####### generating report #######
dd.generate_report(am_1, boll_1, '1 min')
dd.generate_report(am_5, boll_5, '5 min')
dd.generate_report(am_15, boll_15, '15 min')
dd.generate_report(am_30, boll_30, '30 min')
dd.generate_report(am_60, boll_60, '60 min')
dd.generate_report(am_4h, boll_4h, '4 hours')
dd.generate_report(am_1d, boll_1d, '1d')

if dd.send_flag == 1:
    dd.get_msg()
    dd.sendmail('情况汇报', dd.to_str())



# x = np.arange(80, 100)
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# ax1.plot(x, boll_60.ttmu_buy_ratio[-20:], 'ro-', label="TTMU 1day")
# ax1.plot(x, boll_60.ttsi_buy_ratio[-20:], 'g+-', label="TTSI 1day")
# ax2.plot(x, boll_60.market_position[-20:], 'y+-', label="Position 1day")
# ax1.legend(loc=0)
# ax2.legend(loc=0)
# plt.title('RSI chart')
# plt.xlabel('Time')
# plt.ylabel('RSI')
# plt.legend()
# plt.show()
# plt.savefig("d:/cv/image_2.png")
# plt.close()
# dd.sendmail('情况汇报', dd.to_str())


