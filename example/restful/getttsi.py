from huobi import RequestClient

request_client = RequestClient()

symbol_list = ["BTC"]
for symbol_row in symbol_list:
    trade_statistics = request_client.get_ttsi('BTC','60min')
    print("---- Statistics ----",trade_statistics[-1].print_object())

    ttmu2 = request_client.get_ttmu('BTC', '60min')

    print("---- Statistics ----", ttmu2[-1].print_object())

