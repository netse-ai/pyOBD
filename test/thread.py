import threading
import time

class MyThread(threading.Thread):
    def __init__(self, number):
        super(MyThread, self).__init__()
        self.number = number
    def run(self):
        time.sleep(0.1)
        print("Running" + str(self.number))


thread_list = []

for i in range(4):
    thread = MyThread(i)
    thread_list.append(thread)
    thread.start()


for thread in thread_list:
    try:
        print(thread.number , ':', thread.is_alive())
    except:
        print(thread.getName())

