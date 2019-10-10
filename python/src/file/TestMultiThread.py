# -*- coding: utf-8 -*-

# __author__ = xiaobao
# __date__ = 2019/09/06 10:30:09

# desc: desc
# import threading
# import time

# exitFlag = 0

# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)

# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("退出主线程")

import time
import threading
import _thread

class myThread (threading.Thread):
    def __init__(self, szName):
        threading.Thread.__init__(self)
        print("创建对象")
        self.bLoop = True
        pass
    def run(self):
        print("开始线程")
        while self.bLoop:
            print("循环中")
            time.sleep(1)
    def __del__(self):
        print("线程结束")
    
    def stop(self):
        print("stop111")
        self.bLoop = False
        self.join()
    pass

thread1 = myThread("xjc")
def TailThreadFun(szLogPath):
    print("TailThreadFun")
    thread1.start()
    print("TailThreadFunEnd")

_thread.start_new_thread(TailThreadFun, ("xjc",))

time.sleep(10)

thread1.stop()

print("主进程结束")
