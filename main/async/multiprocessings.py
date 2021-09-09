from multiprocessing import Pool

import time
from multiprocessing import Process
import multiprocessing as mp
#%%

# https://docs.python.org/3/library/multiprocessing.html

# Multiprocessing을 하는 이유
# 시간이 오래 걸리는 작업이 I/O 작업 위주가 아니라
# 실제로 CPU를 사용하는 복잡한 계산에 의한 것이라면 스레드보다는 프로세스를 사용하는 것이 좋습니다.
# 특히 파이썬은 GIL (Global Interpeter Lock)의 제한이 있어서
# 스레드를 여러개 사용하는 멀티 스레드의 성능이 더 좋지 않습니다
# 복잡한 작업이 I/O 위주의 작업이라면 멀티 스레드도 좋은 방법이지만 계산 위주의 작업이라면 멀티 프로세스 사용을 권장

# 큐
# 운영체제 상에서 여러 개의 프로세스를 사용하는 경우
# 각 프로세스 간에는 데이터를 공유하기 어려습니다.
# 그래서 보통은 큐(Queue)를 사용해서 프로세스 간의 데이터 전달을 처리합니다.
# 데이터를 생산하는 역할을 맞은 Producer는 데이터가 생성되면 큐에 넣어주기만 합니다.

def show_current_process():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)


def spawn_process(name):
    """
    process spawning
    부모 프로세스(Parent Proecess)가 운영체제에 요청하여 자식 프로세스(Child Process)를 새로 만들어내는 과정을 스포닝
    """
    p = mp.Process(name=name, target=_worker)
    p.start()

    # simple way
    p = Process(target=_f, args=('bob',))
    p.start()
    p.join()


def _worker():
    time.sleep(2)
    proc = mp.current_process()
    print(f"{proc.name}, {proc.pid} SubProcess End")

def _f(name):
    print('hello', name)


def use_pool():
    """make multiple sub process"""
    with Pool(5) as p:
        data = range(1, 10)
        # input arguments and return result
        print(p.map(_work, data))


def _work(x):
    time.sleep(1)
    proc = mp.current_process()
    return f"{proc.name}, {proc.pid} work : {x}"

#%%
if __name__ == '__main__':
    show_current_process()
    spawn_process("sub1")
    spawn_process("sub2")
    print("this is called before sub process")

    use_pool()


#%%
from multiprocessing.context import Process
def aa():
    time.sleep(2)
p = Process(name="test", target=aa)
p.start()

print(p.is_alive())

time.sleep(3)
print(p.is_alive())