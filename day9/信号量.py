import threading, time

class thread_sigle(threading.Thread):
    def run(self):
        semaphore.acquire()
        print(self.name)
        time.sleep(3)
        semaphore.release()
if __name__ == '__main__':
    semaphore = threading.Semaphore(5)
    threads = []
    for i in range(10):
        threads.append(thread_sigle())
    for i in threads:
        i.start()
    for i in threads:
        i.join()
