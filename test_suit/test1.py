import configparser

import os
if __name__ == '__main__':
    str= 'D:/personal/tools/airtest_project/test_suit/../test_report/2018-12-20_22-47-37/ExceptionTest.air.report/recording_0.mp4';
    str1 = 'D:/personal/tools/airtest_project/test_report/2018-12-20_22-47-37/ExceptionTest.air.repor/recording_0.mp4';
    str2 = 'D:/personal/tools/airtest_project/test_report/2018-12-20_22-47-37/ExceptionTest.air.report/log.txt'
    str3 = str2[:-8]
    print(str3)

    #f  =open(str,mode="r")
    #lines = f.readlines()
    #for line in lines:
    #    print(line)
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
    for rece in list:
        print(rece)
