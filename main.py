#! python3
#! -*- coding:utf-8 -*-

import os, sys, threading, time, random


def ProgressBar(cur_page, total_page, total_time):
    sys.stdout.write(' '*50 + '\r')

    i = 0
    per_time = total_time / 50
    while i <= 50:
        sys.stdout.write('(' + str(cur_page) + '/' + str(total_page) + ')[' + '='*i + ('>' if i < 50 else '') + (50-i-1)*'-' + '] ' + str(int((per_time*i/total_time)*100)) + '%'+ ' '*(3-len(str(i))) +'\r')
        sys.stdout.flush()
        i+=1
        time.sleep(per_time)
        #time.sleep(0.01)

def tap(page):   
    w = 890
    #h = 1670 # 最上边的位置是：980；最下边的位置是：1670，每两个之间隔：180
    #h = 980

    f = open('./tb.txt')
    #content = f.read()
    lines = f.readlines(100000)
    f.close()

    for line in lines:
        line = line.rstrip("\n")
        if line == '' or line[0] == '#':
            continue

        if line == 'swipe':
            os.system('adb shell input swipe %d %d %d %d' % (500, 1500, 500, 1000))
            continue

        arr = line.split(',')

        h = int(arr[0])
        c = int(arr[1])

        for i in range(0, c):
            os.system('adb shell input tap %d %d' % (w, h))

            time.sleep(3)

            os.system('adb shell input swipe %d %d %d %d' % (500, 800, 500, 650))

            ProgressBar(i, page, 16)
            
            os.system('adb shell input keyevent 4')

            time.sleep(3)
    #print(hs)
    #sys.exit()

# 使用方法： py main.py -p 10
if __name__ == '__main__':
    #get_bgcolor()
    #sys.exit()
    # 读取当前进程ID，可以通过以下命令方式暂停/继续：pssuspend [-r: 继续运行] pid
    pid = os.getpid()
    print('当前PID: %s' % pid)

    tap(1)

    print('\007')
