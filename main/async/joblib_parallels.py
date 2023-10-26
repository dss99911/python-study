from math import sqrt
from joblib import Parallel, delayed
import time


def task(i):
    print("start", i)
    time.sleep(3)
    return i ** 2


def error_on_jupyter_notebook():
    # https://stackoverflow.com/questions/55955330/printed-output-not-displayed-when-using-joblib-in-jupyter-notebook

    from joblib import Parallel, delayed
    Parallel(n_jobs=8, backend='multiprocessing')(delayed(print)(i) for i in range(10))

if __name__ == '__main__':
    print(Parallel(n_jobs=5)(delayed(task)(i) for i in range(5)))
