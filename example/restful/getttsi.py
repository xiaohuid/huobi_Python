from huobi import RequestClient
from datetime import date

request_client = RequestClient()

symbol_list = ["BTC"]
for symbol_row in symbol_list:
    trade_statistics = request_client.get_ttsi('BTC','60min')
    print("---- Statistics ----",trade_statistics[-1].print_object())

    ttmu2 = request_client.get_ttmu('BTC', '60min')
    t2 = int(ttmu2[-1].timestamp)/1000
    date_time = date.fromtimestamp(t2).strftime("%Y-%m-%d, %H:%M:%S")
    print("---- Statistics ----", ttmu2[-1].print_object())

