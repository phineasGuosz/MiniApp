import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import re
import configparser
import os


filename = ""
filename1 = ""
filename2 = ""
#处理邮件内容
def mailcontent(dict):
    global filename1
    global filename2
    message = MIMEMultipart()
    message['From'] = '18844188849q@163.com'
    message['To'] = 'guoshenzhen@zhuanzhuan.com'
    subject = '步数换UI自动化执行报告'
    message['Subject'] = Header(subject, 'utf-8')




    #print(content)
    #获取字典长度，改长度为执行的总用例条数
    a = len(dict)
    #获取执行成功条数，执行成功的用例的valuelist为空
    b = 0
    for value in dict.values():
        if len(value):
            b += 1
    #获取执行失败的条数
    c = a - b
    content = "总共执行用例： %d 条，执行失败： %d 条，执行成功： %d 条" % (a,b,c)
    #构造邮件内容
    message.attach(MIMEText(content,'plain','utf-8'))

    for value in dict.values():
        if len(value):
            for filevalue in value:
                #清空filename1，及filename2值
                filename1 = ""
                filename2 = ""

                # 匹配出来的是log文件
                searchresult1 = re.search(r'[0-9]+/(.*?).air.report/(.*).txt', filevalue, re.M | re.I)

                try:
                    filename = searchresult1.group(1)
                    filename1 = searchresult1.group(2)
                except Exception  as err:
                    print('执行成功的用例')
                searchresult2 = re.search(r'[0-9]+/(.*?).air.report/(.*?).mp4', filevalue, re.M | re.I)
                try:
                    filename = searchresult2.group(1)
                    filename2 = searchresult2.group(2)
                except Exception  as err:
                    print('匹配视频文件')
                if len(filename1) != 0  and  len(filename2) == 0:
                    att1 = MIMEText(open(filevalue, 'rb').read(), 'base64', 'utf-8')
                    att1["Content-Type"] = 'application/octet-stream'
                    att1["Content-Disposition"] = 'attachment;filename=' +filename+ filename1 + ".txt"
                    message.attach(att1)
                else:
                    att1 = MIMEText(open(filevalue, 'rb').read(), 'base64', 'utf-8')
                    att1["Content-Type"] = 'application/octet-stream'
                    att1["Content-Disposition"] = 'attachment;filename=' +filename+ filename2 + ".mp4"
                    message.attach(att1)
                '''
                if filename1:
                    print(filename1)

                
                else:
                    # 匹配出来的是mp4文件
                    searchresult2 = re.search(r'[0-9]+/(.*?).air.report/recording_0.mp4', filevalue, re.M | re.I)
                    filename2 = searchresult2.group(1)
                    print(searchresult2)
                    print(filename2)
                '''


    mail_host = "smtp.163.com"
    # mail_user = "guosz"
    mail_pass = "PGMpressure123"
    conf = configparser.ConfigParser()
    curdir = os.path.dirname(os.path.realpath(__file__))
    # print(curdir)
    configpath = curdir + "/../conf/mailconf.ini"
    # print(configpath)
    conf.read(configpath)
    sender = conf.get("email", "mail_sender")
    # print(sender)
    receivers = conf.get("email", "mail_receiver")
    # 收件人使用list接受
    list = receivers.split(",")
    # print(list)
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    print(sender)
    print(receivers)
    print(message.as_string())
    smtpObj.login(sender, mail_pass)  # 登录验证
    for receiver in list:

        smtpObj.sendmail(sender, receiver, message.as_string())  # 发送
    print("mail has been send successfully.")
    '''
    #解析dict，取出list，将文件进行压缩
    def mailattch(self,message,dict):
        for value in dict.values():
            if len(value):
                for filevalue in value:
                    #匹配出来的是log文件
                    searchresult1 = re.search(r'[0-9]+/(.*?).air.report/log.txt', filevalue, re.M | re.I)
                    filename1 = searchresult1.group(1)
                    #匹配出来的是mp4文件
                    searchresult2 = re.search(r'[0-9]+/(.*?).air.report/recording_0.mp4', filevalue, re.M | re.I)
                    filename2 = searchresult2.group(1)
                    att1 = MIMEText(open(filevalue,'rb').read(),'base64','utf-8')
                    att1["Content-Type"] = 'application/octet-stream'
                    if filename1:
                        att1["Content-Disposition"] = 'attachment;filename='+filename1+".txt"
                    else:
                        att1["Content-Disposition"] = 'attachment;filename=' + filename2 + ".mp4"
                    message.attach(att1)
    '''
    '''
    #解析配置文件，取出发件人，收件人
    def mailpersons(self,message):
        mail_host = "smtp.163.com"
        #mail_user = "guosz"
        mail_pass = "PGMpressure123"
        conf = configparser.ConfigParser()
        curdir = os.path.dirname(os.path.realpath(__file__))
        #print(curdir)
        configpath = curdir+"/../conf/mailconf.ini"
        #print(configpath)
        conf.read(configpath)
        sender = conf.get("email","mail_sender")
        #print(sender)
        receivers = conf.get("email","mail_receiver")
        #收件人使用list接受
        list = receivers.split(",")
        #print(list)
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(sender, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")

'''









