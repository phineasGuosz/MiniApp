from airtest import __main__
import datetime
import time
import os
from utils.search import searcherror
from utils.mailutil import mailcontent
if __name__ == '__main__':
    #获取当前文件所在目录
    path = os.path.dirname(os.path.realpath(__file__))
    path = path.replace("\\","/")
    print(path)
    #由于通过本地连接，预先进行一次adb连接
    connectcmd = "adb connect 10.242.21.204"
    #远程连接设备
    device = "Android://127.0.0.1:5037/10.242.65.63:16973"
    #设置测试用例目录
    case_dir = "D:/personal/tools/airtest_project/test_case/"
    #静态资源文件路径
    static_root = path + "/../resource/report"
    #遍历目录
    list = os.listdir(case_dir)
    #adb启动微信
    startwxcmd = "adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI"
    #adb关闭微信
    stopwxcmd = "adb shell am force-stop com.tencent.mm"
    #log文件集合
    listpath = []
    # 连接手机
    #os.popen(connectcmd)
    #定义全局字典存储解析结果
    resultdict = {}
    for i in list:

        #预先关闭一次，防止微信处于打开状态，导致异常
        os.popen(stopwxcmd)
        #
        time.sleep(20)
        #开启微信
        os.popen(startwxcmd)
        #增加等待时间，微信开启有延迟
        time.sleep(20)
        #获取当前时间戳
        timestamp = str(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
        #设置Log文件路径
        log = path + "/../test_report/%s/%s" % (timestamp,i + '.report')
        print(log)
        #创建log目录
        if os.path.exists(log):
            print
            '目录已存在'
        else:
            os.makedirs(log)
        #设置报告输出目录
        report = path+"/../test_report/%s/%s" % (timestamp, i + '.report')
        #设置录屏输出目录
        mp4 = "report/%s" % (i + '.mp4')
        #拼装运行命令，调用execmd
        execmd = "airtest run %s --device %s --log %s --recording %s" % (case_dir + i,device,log,mp4)
        #execmd = "airtest run " + case_dir + i + " --device "+ device +" --log "+log
        print(execmd)
        try:
            os.system(execmd)
        except Exception  as err:
            print('执行失败')
        #指定输出报告名称
        result = report + ".html"
        #拼装报告命令，调用reportcmd
        #reportcmd = "airtest report " + case_dir + i + " --static_root " + static_root + " --outfile "+ report + ".html" + " --lang zh"
        reportcmd = "airtest report %s --log %s --static_root %s --outfile %s --lang cn" % (case_dir + i,log,static_root,result)
        print(reportcmd)
        #执行完毕后开始解析log日志
        logpath = log+"/log.txt"
        #print(isinstance(listpath,list))
        listpath.append(logpath)
        #添加报告
        os.system(reportcmd)
        # 关闭微信进程
        os.popen(stopwxcmd)
    # 将dict中的结果解析，发送邮件
    resultdict=searcherror(listpath)
    mailcontent(resultdict)