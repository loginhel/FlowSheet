mport datetime
import time
import os
import random
import glob

global tab
tab = '\t'

class FlowSheet:
    def _init(self, mdn, msid, upFlowCount, downFlowCount):
        if mdn.__len__() == 15:
            self._mdn = mdn
        else:
            self._mdn = '86' + mdn
        self._msid = msid
        self._upFlowCount = upFlowCount
        self._downFlowCount = downFlowCount

    def setStreamId(self,streamId):
        self._streamId = streamId

    def getRandomId(self):
        chars = 'AaBbCcj78KkLlMmN_nOoPpQ+qR1234rSsTtUuVvDdEe/FfGgHhIiJWw-XxYyZz0569'
        a = []
        count = 0
        while count < 8:
            a.append(chars[random.randint(0, 65)])
            count = count + 1
        out = ''.join(a)
        return out

    def getflowSheet(self):
        return str(self._streamId) + '\t2\t2\t1\t' + str(self._mdn) + '\t' + str(self._msid) + "\t6089FFE9\tE8000000001FD9\t10.62.128.69\tctnet@mycdma.cn\t\t\t" + \
               self.getRandomId() +tab + self.getRandomId() + "\t1\t1\t1|1\t1|255\t115.169.21.95\t115.168.75.199\t172.26.98.199\t372A00525B41\t" + \
               "\t6800a8c0006b000000ac14852102000000|00a8c0006b000000ac14852102010361\t460030\t0\t\t33\t1\t1\t2\t0\t\t0\t" + str(self._upFlowCount) + '\t' +\
               str(self._downFlowCount) + '\t0\t' + str(int(time.time())) + "\t1118\t1\t0\t0\t1496246074\t" + "0\t" * 7 + "1|255|15|0\t\t1\t116\t287\t241\t1\t0\t0\t\t\t1\t" + tab*4 + '\n'

#获取文件名编号
def getFileNameNum(fileNameHead):
    count= 0
    #查找文件的简单方法！
    for file in glob.iglob(fileNameHead+ '*.TXT'):
        count = count + 1
    return count

#获取文件名
currentDate = datetime.datetime.now()
fileNameHead = "AAA_99_" + currentDate.strftime('%Y%m%d') + "_" + currentDate.strftime('%H%M') + "_"
fileName = fileNameHead + str(getFileNameNum(fileNameHead)).zfill(4) + ".TXT"

#写文件
fileHandle = open(fileName,'w+')
fileHead = "000000"+datetime.datetime.now().strftime('%Y%m%d')+"0" * 38 + "\n"
fileHandle.write(fileHead)

#写文件+更新文件头
def writeFile(fh, data, count):
    #写文件
    flowSheet = FlowSheet()
    flowSheet._init(inData[0], inData[1], inData[2], inData[3])
    flowSheet.setStreamId(recordCount)
    fileHandle.write(flowSheet.getflowSheet())
    #更新文件头
    currentDate = datetime.datetime.now()
    #如果是第一条数据
    if count == 1:
        fileHandle.seek(14, 0)
        fileHandle.write(currentDate.strftime('%Y%m%d'))
        fileHandle.write(currentDate.strftime('%H%M%S'))

    fileHandle.seek(28, 0)
    fileHandle.write(currentDate.strftime('%Y%m%d'))
    fileHandle.write(currentDate.strftime('%H%M%S'))
    fileHandle.write(str(recordCount).zfill(10))
    fileHandle.seek(0, os.SEEK_END)

#开始作业
print("Inputs:用户接入号码、IMSI号、上行流量、下行流量、话单条数N(可选)")
print("Output:话单文件\n按q键结束输入！")

recordCount = 0
#循环写入
while True:
    line = input("please inpt user data:")
    inData = str(line).split()
    if len(inData) == 5:
        # 获取个数N
        perCount = int(inData[4])
        #循环
        for i in range(0, perCount):
            recordCount = recordCount + 1
            writeFile(fileHandle, inData, recordCount)
            i = i+1

    elif len(inData) == 4:
        recordCount = recordCount + 1
        writeFile(fileHandle, inData, recordCount)

    elif (len(inData) == 1) and (inData[0] == 'q'):
        break
    else:
        print("Inpt Error!")

#关闭文件
fileHandle.close()
