import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
        print("sub thread start ", threading.currentThread().getName())
        time.sleep(3)
        print("sub thread end ", threading.currentThread().getName())

if __name__ == '__main__':
    print("main thread start")
    for i in range(5):
        name = "thread {}".format(i)
        t = Worker(name)                # sub thread 생성
        t.daemon = True     # for Daemeon thread. if true, then when main thread finished, sub thread terminated
        t.start()                       # sub thread의 run 메서드를 호출

    print("main thread end")
