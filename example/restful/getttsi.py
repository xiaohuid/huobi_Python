from huobi import RequestClient
from datetime import date

request_client = RequestClient()

symbol_list = ["BTC"]
for symbol_row in symbol_list:
    trade_statistics = request_client.get_ttsi('BTC', '15min')
    print("---- Statistics ----", trade_statistics[-1].print_object())
    print("---- Statistics ----", trade_statistics[-2].print_object())

    for tt in range(len(trade_statistics)):
        print(trade_statistics[tt].print_object())
    print("---- Ttmu ----")

    ttmu2 = request_client.get_ttmu('BTC', '15min')
    for tt in range(len(ttmu2)):
        print(ttmu2[tt].print_object())

    position2 = request_client.get_position('BTC', 'quarter','60min','48','1')
    for cc in range(len(position2)):
        print(position2[cc].print_object())