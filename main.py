'''
    Chef:厨师
    Diners：食客
    Bread：面包
'''
import os
import signal
from multiprocessing import Process
import threading
from threading import Thread
import time
import multiprocessing
start = time.time()
Bread=500
D=0
sleep=0
class Chef(Thread):
    username = ""
    mutex1 = threading.Lock()
    count = 0
    def run(self) -> None:
        global Bread
        global D
        global sleep
        while True:
            self.mutex1.acquire()
            if D<6:
                if Bread <500:
                    Bread = Bread + 1
                    self.count=self.count+1
                    print(self.username, "-------------造了一个面包！还剩", Bread, "个面包！已经造了", self.count, "个面包！")
                else:
                    for i in range(6):
                        time.sleep(1)
                        print(".",end="")
            else:
                self.mutex1.release()
                os.kill(os.getpid(), signal.SIGTERM)
            self.mutex1.release()

class  Diners(Thread):
    mutex=threading.Lock()
    username = ""
    count = 0
    def run(self) -> None:
        global D
        money=3000
        global Bread
        while True:
                self.mutex.acquire()
                if money>0:
                    if Bread >0:
                        Bread = Bread - 1
                        money = money - 2.5
                        self.count=self.count+1
                        print(self.username, "--------------抢了1个面包！还剩",Bread, "个面包！！已经买了", self.count, "个面包！","还剩下",money)
                        time.sleep(0.1)
                    else:
                        for i in range(3):
                            time.sleep(1)

                    self.mutex.release()
                else:
                    print(self.username,"没钱了！")
                    D = D + 1
                    self.mutex.release()
                    time.sleep(50000)





Chef01=Chef()
Chef02=Chef()
Chef03=Chef()
Chef01.username="厨师01"
Chef02.username="厨师02"
Chef03.username="厨师03"

Chef01.start()
Chef02.start()
Chef03.start()

Diners01=Diners()
Diners02=Diners()
Diners03=Diners()
Diners04=Diners()
Diners05=Diners()
Diners06=Diners()

Diners01.username="食客01"
Diners02.username="食客02"
Diners03.username="食客03"
Diners04.username="食客04"
Diners05.username="食客05"
Diners06.username="食客06"


Diners01.start()
Diners02.start()
Diners03.start()
Diners04.start()
Diners05.start()
Diners06.start()

