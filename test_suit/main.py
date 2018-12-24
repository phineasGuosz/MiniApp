from airtest import __main__
import datetime
import time
import os

if __name__ == '__main__':
    # __main__.main("run ../test_case/untitled.air --device Android:///b91467d0 --log ../test_report".split(" "))
    # __main__.main("report ../test_case/untitled.air --log_root ../test_report --outfile ../test_report/log.html --lang zh".split(" "))
    suit_name = str(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
    suit_path = "../test_report/%s" % (suit_name)
    os.mkdir(suit_path)
    case_name = "untitled.air"
    case_dir = "../test_case/"
    case_path = "../test_case/"
    dirs = os.listdir(case_path)
    

    file_dir = case_path + case_name
    report_name = case_name + ".report"
    # 连接设备
    device = "Android:///b91467d0"
    # log文件路径
    log = "../test_report/%s/%s" % (suit_name, report_name)
    # 录屏mp4
    recording = "../test_report/%s/%s" % (suit_name, report_name)

    log_root = log
    # 静态资源文件路径
    static_root = "../../../resource/report"
    # html文件路径
    outfile = log + "/report.html"

    run_exe = "run %s --device %s --log %s --recording %s" % (file_dir, device, log, recording)
    report_exe = "report %s --log_root %s --static_root %s --outfile %s --lang zh" % (
        file_dir, log_root, static_root, outfile)
    __main__.main(run_exe.strip().split(" "))
    __main__.main(report_exe.strip().split(" "))
