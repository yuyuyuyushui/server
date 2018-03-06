import threading, time
class Threading_class(threading.Thread):

    def doA(self):
        rlock.acquire()
        print(self.name,'gotdoA', time.ctime())
        rlock.acquire()
        print(self.name,'gotdoB', time.ctime())
        rlock.release()
        rlock.release()
    def doB(self):
        rlock.acquire()
        print(self.name, 'gotdoA', time.ctime())
        rlock.acquire()
        print(self.name, 'gotdoB', time.ctime())
        rlock.release()
        rlock.release()
    def run(self):
        self.doA()
        self.doB()
threads = []
rlock = threading.RLock()
for i in range(5):
    threads.append(Threading_class())
for t in threads:
    t.start()
for t in threads:
    t.join()