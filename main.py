import datetime
import time
import os
import sys
import fileinput
import random

test = ''

sdsjdkjsdk = ''
#if os.path.exists(fname):

timeNow = datetime.datetime.now()
#txtName = "AAA_99_" + str(timeNow.year) + str(timeNow.month).zfill(2) + str(timeNow.day).zfill(2) + "_" + str(timeNow.hour).zfill(2) + str(timeNow.minute).zfill(2) + "_0000.TXT"
txtName = "AAA_99_" + timeNow.strftime('%Y%m%d') + "_" + timeNow.strftime('%H%M') + "_0000.TXT"

fobj = open(txtName, "w+")
sdsdsd = ''
hjkjkj = ''
jkj = ''

Num = 0
fileinput.input()

Num = input("请输入个数：")

fobj.write("1554002017060820170608205752201706082058590000038827\n")

fobj.write("1554002017060820170608205752201706082058590000038827\n")

fobj.seek(14,0)


fobj.write(timeNow.strftime('%Y%m%d'))

fobj.seek(0,os.SEEK_END)
fobj.write("1554002017060820170608205752201706082058590000038827\n")

fhead = "000000" + timeNow.strftime('%Y%m%d')

tab = '\t'
streamNum = 0

ConnectNumber = ""
IMSINumber = ""
InputPackets = 0
OutputPackets = 0
AcSID = ""

ClID = ""

print('输出多个数字%d%d' %(1,1))

fobj.write(str(streamNum) + "\t1\t2\t4\t" + ConnectNumber + "\t" + IMSINumber +"\t\t\t" + "10.62.128.69\t" + "ctnet@mycdma.cn\t\t\t"+ "AAAWxPo4\t" + "\t\t\t\t\t" + tab * 10 + "3223\n")

print(txtName)
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

now=datetime.datetime.now()

print(now.strftime('%Y%m%d'))

"sdsds".zfill(2)

class FlowSheet:
    #定义基本属性
    ConnectNumber = ""
    IMSINumber = ""
    InputPackets = 0
    OutputPackets = 0
    #定义私有属性

    #定义构造方法
    def __init__(self, cnum, inum, ips, ops):
        self.ConnectNumber = cnum
        self.IMSINumber = inum
        self.InputPackets = ips
        self.OutputPackets = ops

    #定义写出方法
    #def writeFile(self, fo):
        #arow =
        #fo.write(self.ConnectNumber)

def hex66(num):
    #转换成66进制字符
    chars = 'AaBbCcj78KkLlMmN_nOoPpQ+qR1234rSsTtUuVvDdEe/FfGgHhIiJWw-XxYyZz0569'
    a = []
    while num != 0:
        mo = num % 66
        a.append(chars[mo])
        num = num / 66
    a.reverse()
    out = ''.join(a)
    return out


def getId():
    chars = 'AaBbCcj78KkLlMmN_nOoPpQ+qR1234rSsTtUuVvDdEe/FfGgHhIiJWw-XxYyZz0569'
    a = []
    count = 0
    while count < 8:
        a.append(chars[random.randint(0, 65)])
        count = count + 1
    out = ''.join(a)
    return out



#获取唯一标识
#def getId():
    #66进制位数对应10进制数范围参考：
    #1位：0-65
    #2位：66-4355
    #3位：4355-287495
    #4位：287495-18974736
    #5位：18974736-1252332576
    #6位：1252332576-82653950016

print(getId())