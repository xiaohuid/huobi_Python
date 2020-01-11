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
