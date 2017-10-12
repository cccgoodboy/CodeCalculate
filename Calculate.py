import subprocess
import os
import time

# 需要统计的代码文件路径(需要替换成你需要统计的代码文件夹的路径)
codeFilePath = '/Users/hatsuhodohodo/Documents/work/SHBao/SHBao/SHBao'
# 保存统计文件的路径(需要替换成你想写入的文件地址 将/Users/hatsuhodohodo/Documents/代码行数统计   替换即可，codeLine.txt是文件名)
writePath = '/Users/hatsuhodohodo/Documents/代码行数统计/codeLine.txt'


def main():
    openFilePath(codeFilePath)


# 跳转到文件路径下
def openFilePath(filePath):
    os.chdir(filePath)
    os.getcwd()
    if calculateCodeLine() == 1:
        print('code line calculator failed')
    else:
        newFileString = str(calculateCodeLine(),encoding="utf-8")
        dateString = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        oldFileString = getOldFileContent(writePath)
        writeContent = '%s\n%s%s' % (oldFileString,dateString,newFileString)
        writeInFile(writePath,writeContent)


# 返回统计代码行数
def calculateCodeLine():
    commandString = 'find . -name "*.m" -or -name "*.h" -or -name "*.xib" -or -name "*.c" -or -name "*.swift" |xargs ' \
                    'grep -v "^$"|wc -l '
    progress = subprocess.Popen(commandString, shell=True, stdout=subprocess.PIPE)
    progress.wait()
    if progress.returncode != 0:

        return 1
    else:
        return progress.stdout.read()


# 读取老的数据统计数据
def getOldFileContent(filePath):
    try:
        with open(filePath,'r') as f:
            return f.read()
    except:
        return ''


# 统计数据写入文件
def writeInFile(filePath, writeContent):

    with open(filePath, 'w') as file:
        file.write(writeContent)


if __name__ == '__main__':
    main()
