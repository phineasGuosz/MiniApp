import re
import os
dict = {}
def searcherror(listpath):
    for filepath in listpath:
        file = open(filepath,mode='r')
        lines = file.readlines()
        #print(isinstance(dict,dict))
        for line in lines:
            #匹配的异常
            keyword = "TargetNotFoundError"
            #print(line)
            #匹配结果
            matchresult = re.search(keyword,line)
            #print(matchresult)


            if matchresult:
                '''如果匹配到异常'''
                searchresult = re.search(r'[0-9]+/(.*?).air.report', filepath, re.M | re.I)
                key = searchresult.group(1)
                if dict[key] == [] or key not in dict:
                    loglist = []
                    loglist.append(filepath)
                    map4path=filepath[:-8]
                    loglist.append(map4path + "/recording_0.mp4")
                    dict[key] = loglist
            else:
                '''如果未匹配到异常'''
                searchresult = re.search(r'[0-9]+/(.*?).air.report', filepath, re.M | re.I)
                key = searchresult.group(1)
                #print("===="+key)
                #print(isinstance(key,str))
                if key:
                    if key not in dict:
                        loglist1 = list()
                        dict[key] = loglist1
                else:
                    continue
    return dict





    #print(dict)




#searcherror("D:/personal/tools/airtest_project/test_report/2018-12-11_19-24-51/XinRenZhuanQuShangPinDianJi.air.report/log.txt")




