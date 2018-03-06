import time,threading

begin = time.time()
def foo(n):
    print(threading.current_thread()) # 打印所属线程
    print('foo%s'%n)
    time.sleep(1)
def fool(n):
    print(threading.current_thread())
    print('foop%s'%n)
    time.sleep(3)
t1 = threading.Thread(target=foo, args=(1,))  # 创建线程对象,并行运行
t2 = threading.Thread(target=fool, args=(2,))  # 创建线程对象,并行运行
threads = []
threads.append(t1)
threads.append(t2)
if __name__=="__main__":
    for i in threads:
        print(threading.current_thread())
        i.setDaemon(True)
        i.start() # 启动线程
    i.join() #线程阻塞
    print(threading.current_thread())
    print(threading.active_count())
    end = time.time()
    print( end - begin)

