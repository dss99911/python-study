from math import sqrt
from joblib import Parallel, delayed
import time


def task(i):
    print("start", i)
    time.sleep(3)
    return i ** 2


if __name__ == '__main__':
    print(Parallel(n_jobs=5)(delayed(task)(i) for i in range(5)))
