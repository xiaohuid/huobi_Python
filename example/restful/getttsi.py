from huobi import RequestClient
from datetime import date

request_client = RequestClient()

symbol_list = ["BTC"]


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



for symbol_row in symbol_list:
    dd = MyEmailContent()

    trade_statistics = request_client.get_ttsi('BTC', '15min')
    print("---- Statistics ----", trade_statistics[-1].print_object())
    print("---- Statistics ----", trade_statistics[-2].print_object())

    for tt in range(len(trade_statistics)):
        dd.add_msg(trade_statistics[tt].to_str())
        #print(trade_statistics[tt].print_object())

    dd.get_msg()
    print("---- Ttmu ----")

    ttmu2 = request_client.get_ttmu('BTC', '15min')
    for tt in range(len(ttmu2)):
        print(ttmu2[tt].to_str())

    position2 = request_client.get_position('BTC', 'quarter','60min','48','1')
    for cc in range(len(position2)):
        print(position2[cc].to_str())



