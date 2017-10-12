import subprocess
import os
import time
#保存统计文件的路径
codeFilePath = '/Users/hatsuhodohodo/Documents/work/SHBao/SHBao/SHBao'
writePaht = '/Users/hatsuhodohodo/Documents/代码行数统计/codeLine.txt'
def main():
    openFilePath(codeFilePath)
#跳转到文件路径下
def openFilePath(filePath):
    os.chdir(filePath)
    os.getcwd()
    writeInFile(writePaht,str(calculateCodeLine(),encoding="utf-8"))
def calculateCodeLine():
    commandString = 'find . -name "*.m" -or -name "*.h" -or -name "*.xib" -or -name "*.c" -or -name "*.swift" |xargs grep -v "^$"|wc -l'
    progress = subprocess.Popen(commandString,shell=True, stdout=subprocess.PIPE)
    progress.wait()
    if progress.returncode !=0:
        print('code line calculator failed')
        return 1
    else:
        return progress.stdout.read()
#统计数据写入文件
def writeInFile(filePath,writeContent):
    dateString = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    with open(filePath,'r') as oldF:
        oldString = oldF.read()
    with open(filePath,'w') as file:
        file.write(oldString+'%s%s\n' % (dateString,writeContent))
if __name__ == '__main__':
    main()
