import base64
import hashlib
import hmac
import datetime
from email.mime.image import MIMEImage
from urllib import parse
import urllib.parse
from huobi.exception.huobiapiexception import HuobiApiException
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import time
from datetime import datetime
import numpy as np
import email.mime.multipart
import email.mime.text
import smtplib
from huobi.model.bararray import BarArray
from huobi.model.tradeinfoarray import TradeInfoArray


class MyEmailContent():

    def __init__(self):
        self.title = ''
        self.msg_array = []
        self.summary_array = []
        self.send_flag = 0
        self.onemin_time = ''

    def set_subject(self, subject):
        self.title = subject

    def add_msg(self, msg):
        self.msg_array.append(msg)

    def add_summary(self, summary):
        self.summary_array.append(summary)

    def get_msg(self):
        for aa in range(len(self.msg_array)):
            print(self.msg_array[aa])

    def get_summary(self):
        for aa in range(len(self.summary_array)):
            print(self.summary_array[aa])

    def msg(self):
        return self.msg_array

    def summary(self):
        return self.summary_array

    def to_str(self):

        a = """
        {}
        """.format("\n".join(self.msg_array[:]))
        return a

    def summary_to_str(self):

        a = """
        {}
        """.format("\n".join(self.summary_array[:]))
        return a

    def send_sms(self, zb1, z1, zb2, z2):

        t1 = time.time() - self.init_time
        self.write_log(t1)

        if t1 <= 240:
            return

        client = AcsClient('dd', 'dd', 'cn-hangzhou')
        time2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dd')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', "dd")
        request.add_query_param('SignName', "dd")
        request.add_query_param('TemplateCode', "dd")
        request.add_query_param('TemplateParam',
                                "{\"zb1\": \"" + zb1 + "\",\"z1\": \"" + z1 + "\",\"zb2\":\"" + zb2 + "\",\"z2\":\"" + z2 + "\",\"time\":\"" + time2 + "\"}")
        self.write_log(f"{zb1},{z1},{zb2},{z2}")

        # response = client.do_action(request)
        # python2:  print(response)
        # self.write_log(str(response, encoding = 'utf-8'))
        self.sendmail(zb1 + "-" + time2, z1 + ',' + zb2 + ',' + z2)

    # 接受：收件人，主题，内容
    # 返回：邮件发送结果
    def sendmail(self, to_title, to_content: str):

        ret = True
        FROM_MAIL = "ddm"  # 发件人
        TO_MAIL = "dd"  # 收件人
        SMTP_SERVER = 'dd'  # qq邮箱服务器
        SSL_PORT = '465'  # 加密端口
        USER_NAME = FROM_MAIL  # qq邮箱用户名
        USER_PWD = "dd"  # qq邮箱授权码
        msg = email.mime.multipart.MIMEMultipart()  # 实例化email对象
        msg['from'] = FROM_MAIL  # 对应发件人邮箱昵称、发件人邮箱账号
        msg['to'] = TO_MAIL  # 对应收件人邮箱昵称、收件人邮箱账号
        msg['subject'] = to_title  # 邮件的主题
        txt1 = email.mime.text.MIMEText(self.summary_to_str())
        msg.attach(txt1)
        txt = email.mime.text.MIMEText(to_content)
        msg.attach(txt)
        # fp = open("d:/cv/image_2.png", 'rb')
        # images = MIMEImage(fp.read())
        # fp.close()
        # msg.attach(images)
        try:
            # 纯粹的ssl加密方式
            smtp = smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT)  # 邮件服务器地址和端口
            smtp.ehlo()  # 用户认证
            smtp.login(USER_NAME, USER_PWD)  # 括号中对应的是发件人邮箱账号、邮箱密码
            smtp.sendmail(FROM_MAIL, TO_MAIL, str(msg))  # 收件人邮箱账号、发送邮件
            smtp.quit()  # 等同 smtp.close()  ,关闭连接
        except Exception as e:
            ret = False
            print(">>>>>>>:" + str(e))
        return ret

    def generate_report(self, bar: BarArray, tradeinfo: TradeInfoArray, Interval):
        # #####Market#####
        """
        Current Market Price。max，min，changes more than target , volume more than target.
        """
        # current price bar.open, bar.close, bar.high, bar.low
        s_flag = 0

        if Interval == '1 min':
            self.onemin_time = int(bar.id_array[-1])

        tmin = datetime.fromtimestamp(self.onemin_time).strftime("%M")
        thour = datetime.fromtimestamp(self.onemin_time).strftime("%H")
        date_time = datetime.fromtimestamp(bar.id_array[-1]).strftime("%Y-%m-%d %H:%M:%S")
        #  generating status report ##

        self.add_msg('## Market Details ## ' + str(Interval) + " " + date_time)
        self.add_msg(bar.to_str())
        self.add_msg(tradeinfo.boll_to_str())
        self.add_msg('')
        self.add_msg(tradeinfo.trade_to_str())
        td = bar.td()
        self.add_msg('TD Value: ' + str(round(td, 2)))
        rsi = bar.rsi(6)
        self.add_msg('RSI Value: ' + str(round(rsi, 2)))
        self.add_msg('')

        if Interval == '1 min':
            return

        elif Interval == '5 min':
            if int(tmin) % 5 != 0:
                return

        elif Interval == '15 min':
            if int(tmin) % 15 != 0:
                return

        elif Interval == '30 min':
            if int(tmin) % 30 != 0:
                return

        elif Interval == '60 min':
            if int(tmin) != 0:
                return

        elif Interval == '4 hours':
            if int(thour) % 4 != 0 or int(tmin) != 0:
                return

        elif Interval == '1d':
            if int(thour) != 0 or int(tmin) != 0:
                return
        self.add_summary('----周期为：' + str(Interval) + '-----')
        # Price change more than xx in xx minutes/hours
        if Interval == '5 min':
            if abs(bar.high[-2] - bar.low[-2]) >= bar.high[-2] * 0.005:
                self.add_summary('价格变动超过0.5%: ' + str(bar.high[-2] - bar.low[-2]))
                s_flag = 1
        # Volume more than target
        if Interval == '1 min':
            if bar.volume[-2] >= 100000:
                self.add_summary('交易量超过10万: ' + str(bar.volume[-2]))
                s_flag = 1

        elif Interval == '5 min':
            if bar.volume[-2] >= 300000:
                self.add_summary('交易量超过30万: ' + str(bar.volume[-2]))
                s_flag = 1
        elif Interval == '15 min':
            if bar.volume[-2] >= 1500000:
                self.add_summary('交易量超过150万: ' + str(bar.volume[-2]))
                s_flag = 1

        # #####RSI#####

        # RSI value has exceed target value
        if (rsi >= 75 or rsi <= 25):
            self.add_summary('RSI Value超过阈值: ' + str(round(rsi, 2)))
            s_flag = 1

        ######TD########
        # TD Vaule is 7 or 13

        if abs(td) >= 13 or abs(td) == 9:
            self.add_summary('TD Value: ' + str(round(td, 2)))
            s_flag = 1

        ######TOP Trader######
        # TTSI Value, Changes
        if abs(tradeinfo.ttsi_buy_ratio[-1] - tradeinfo.ttsi_buy_ratio[-2]) >= 0.02:
            self.add_summary('TTSI: ' + str(tradeinfo.ttsi_buy_ratio[-1]) + ' , Prior TTSI: ' + str(
                tradeinfo.ttsi_buy_ratio[-2]))
            self.add_summary(
                'Change of TTSI buy_ratio： ' + str(
                    round(tradeinfo.ttsi_buy_ratio[-1] - tradeinfo.ttsi_buy_ratio[-2], 2)))
            s_flag = 1
        # TTMU Value, Changes
        if abs(tradeinfo.ttmu_buy_ratio[-1] - tradeinfo.ttmu_buy_ratio[-2]) >= 0.01:
            self.add_summary('TTMU: ' + str(tradeinfo.ttmu_buy_ratio[-1]) + ' , Prior TTMU: ' + str(
                tradeinfo.ttmu_buy_ratio[-2]))
            self.add_summary(
                'Change of TTMU buy_ratio： ' + str(
                    round(tradeinfo.ttmu_buy_ratio[-1] - tradeinfo.ttmu_buy_ratio[-2], 3)))
            s_flag = 1
        # Position Value, Changes
        if tradeinfo.market_position[-1] - tradeinfo.market_position[-2] != 0:
            self.add_summary('POS: ' + str(tradeinfo.market_position[-1]) + ' , Prior POS: ' + str(
                tradeinfo.market_position[-2]))
            self.add_summary(
                'Change of market_position： ' + str(
                    round(tradeinfo.market_position[-1] - tradeinfo.market_position[-2], 2)))

        ########BOLL ###########
        # boll.to_str

        if (bar.close[-1] > tradeinfo.boll_up_array[-1] and bar.close[-2] > tradeinfo.boll_up_array[-2]):
            self.add_summary('连续两个周期收盘价突破上限！')
            s_flag = 1
        if (bar.close[-1] < tradeinfo.boll_down_array[-1] and bar.close[-2] < tradeinfo.boll_down_array[-2]):
            self.add_summary('连续两个周期收盘价突破下限！')
            s_flag = 1
        if tradeinfo.boll_up_cnt_array[-1] >= 8 and tradeinfo.boll_up_cnt_array[-1] % 3 == 0:
            self.add_summary('连续在中线上方运行次数：' + str(tradeinfo.boll_up_cnt_array[-1]))
            s_flag = 1
        if tradeinfo.boll_up_brk_cnt_array[-1] >= 5 and tradeinfo.boll_up_brk_cnt_array[-1] % 3 == 0:
            self.add_summary('连续突破上限次数限！' + str(tradeinfo.boll_up_brk_cnt_array[-1]))
            s_flag = 1
        if tradeinfo.boll_down_cnt_array[-1] >= 8 and tradeinfo.boll_down_cnt_array[-1] % 3 == 0:
            self.add_summary(' ,连续在中线下方运行次数：' + str(tradeinfo.boll_down_cnt_array[-1]))
            s_flag = 1
        if tradeinfo.boll_down_brk_cnt_array[-1] >= 5 and tradeinfo.boll_down_brk_cnt_array[-1] % 3 == 0:
            self.add_summary('连续突破下限次数限！' + str(tradeinfo.boll_down_brk_cnt_array[-1]))
            s_flag = 1

        if s_flag == 1:
            self.send_flag = 1

        # if Interval == '1 min':
        #     if s_flag == 1:
        #         self.send_flag = 1
        #
        # elif Interval == '5 min':
        #     if int(tmin) % 5 == 0:
        #         if s_flag == 1:
        #             self.send_flag = 1
        #
        # elif Interval == '15 min':
        #     if int(tmin) % 15 == 0:
        #         if s_flag == 1:
        #             self.send_flag = 1
        # elif Interval == '30 min':
        #     if int(tmin) % 30 == 0:
        #         if s_flag == 1:
        #             self.send_flag = 1
        # elif Interval == '60 min':
        #     if int(tmin) == 0:
        #         if s_flag == 1:
        #             self.send_flag = 1
        # elif Interval == '4 hours':
        #     if int(thour) % 4 == 0 and int(tmin) == 0:
        #         if s_flag == 1:
        #             self.send_flag = 1
        # elif Interval == '1d':
        #     if int(thour) == 0 and int(tmin) == 0:
        #         if s_flag == 1:
        #             self.send_flag = 1

        self.add_summary(' ')
