import base64
import hashlib
import hmac
import datetime
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

    def set_subject(self, subject):
        self.title = subject

    def add_msg(self, msg):
        self.msg_array.append(msg)

    def get_msg(self):
        for aa in range(len(self.msg_array)):
            print(self.msg_array[aa])

    def msg(self):
        return self.msg_array

    def to_str(self):

        a="""
        {}
        """.format("\n".join(self.msg_array[:]))
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
        request.set_domain('ddcs.com')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-dd")
        request.add_query_param('PhoneNumbers', "dd")
        request.add_query_param('SignName', "园区宝")
        request.add_query_param('TemplateCode', "d")
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
        FROM_MAIL = "dd"  # 发件人
        TO_MAIL = "dd"  # 收件人
        SMTP_SERVER = 'dd'  # qq邮箱服务器
        SSL_PORT = '465'  # 加密端口
        USER_NAME = FROM_MAIL  # qq邮箱用户名
        USER_PWD = "dd"  # qq邮箱授权码
        msg = email.mime.multipart.MIMEMultipart()  # 实例化email对象
        msg['from'] = FROM_MAIL  # 对应发件人邮箱昵称、发件人邮箱账号
        msg['to'] = TO_MAIL  # 对应收件人邮箱昵称、收件人邮箱账号
        msg['subject'] = to_title  # 邮件的主题
        txt = email.mime.text.MIMEText(to_content)
        msg.attach(txt)
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

    def sendmaila(self, to_title, to_content: []):

        ret = True
        FROM_MAIL = "ddm"  # 发件人
        TO_MAIL = "ddg"  # 收件人
        SMTP_SERVER = 'dd'  # qq邮箱服务器
        SSL_PORT = '465'  # 加密端口
        USER_NAME = FROM_MAIL  # qq邮箱用户名
        USER_PWD = "dd"  # qq邮箱授权码
        msg = email.mime.multipart.MIMEMultipart()  # 实例化email对象
        msg['from'] = FROM_MAIL  # 对应发件人邮箱昵称、发件人邮箱账号
        msg['to'] = TO_MAIL  # 对应收件人邮箱昵称、收件人邮箱账号
        msg['subject'] = to_title  # 邮件的主题
        for nn in range(len(to_content)):
            txt = email.mime.text.MIMEText(to_content[nn])
            msg.attach(txt)
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
        ######Market#####
        """
        Current Market Price。max，min，changes more than target , volume more than target.
        """
        # current price bar.open, bar.close, bar.high, bar.low

        t2 = int(bar.id_array[-1])
        date_time = datetime.fromtimestamp(t2).strftime("%Y-%m-%d, %H:%M:%S")
        self.add_msg('######## Current Market Details######### ' + str(Interval) + " " + date_time)
        self.add_msg(
            'bar.open, bar.close, bar.high, bar.low' + str(bar.open[-1]) + ' ,' + str(bar.close[-1]) + ' ,' + str(
                bar.high[-1]) + ' ,' + str(bar.low[-1]))

        # Price change more than xx in xx minutes/hours

        # Volume more than target

        ######RSI#####

        # RSI value has exceed target value
        rsi = bar.rsi(6)
        self.add_msg('RSI Value: ' + str(round(rsi, 2)))

        ######TD########
        # TD Vaule is 7 or 13
        td = bar.td()
        self.add_msg('TD Value: ' + str(round(td, 2)))

        ######TOP Trader######
        # TTSI Value, Changes
        self.add_msg('TTSI: ' + str(tradeinfo.ttsi_buy_ratio[-1]) + ' , Prior TTSI: ' + str(
            tradeinfo.ttsi_buy_ratio[-2]))
        if tradeinfo.ttsi_buy_ratio[-1] - tradeinfo.ttsi_buy_ratio[-2] != 0:
            self.add_msg(
                'Change of TTSI buy_ratio： ' + str(
                    round(tradeinfo.ttsi_buy_ratio[-1] - tradeinfo.ttsi_buy_ratio[-2], 2)))
        # TTMU Value, Changes
        self.add_msg('TTMU: ' + str(tradeinfo.ttmu_buy_ratio[-1]) + ' , Prior TTSI: ' + str(
            tradeinfo.ttmu_buy_ratio[-2]))
        if tradeinfo.ttmu_buy_ratio[-1] - tradeinfo.ttmu_buy_ratio[-2] != 0:
            self.add_msg(
                'Change of TTMU buy_ratio： ' + str(
                    round(tradeinfo.ttmu_buy_ratio[-1] - tradeinfo.ttmu_buy_ratio[-2], 3)))
        # Position Value, Changes

        ########BOLL ###########
        # boll.to_str
        self.add_msg(tradeinfo.to_str())
