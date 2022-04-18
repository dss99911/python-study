# https://dojang.io/mod/page/view.php?id=2427
from functools import wraps
from typing import List


#%%
def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')

    return wrapper  # wrapper 함수 반환


@trace  # @데코레이터
def hello():
    print('hello')


@trace  # @데코레이터
def world():
    print('world')


hello()  # 함수를 그대로 호출
world()  # 함수를 그대로 호출

#%% multi decorator
def decorator1(func):
    def wrapper():
        print('decorator1')
        func()

    return wrapper


def decorator2(func):
    def wrapper():
        print('decorator2')
        func()

    return wrapper


# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')


hello()

#%% decorator with parameter


def cols_required(cols: List[str], index=0):
    def col_required_decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            df = args[index]
            for col in cols:
                if not col in df.columns:
                    raise Exception("Column {} is required".format(col))
            return f(*args, **kwargs)
        return decorated_function
    return col_required_decorator

def cols_returns(cols: List[str], index=0):
    def col_required_decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            df = f(*args, **kwargs)

            for col in cols:
                if not cols in df.columns:
                    raise Exception("Column {} is not returned".format(col))
            return
        return decorated_function
    return col_required_decorator


@cols_required(["col1", "col2"])
@cols_required(["col3", "col4"], index=1)
@cols_returns(["col5"])
def aa(df1, df2):
    pass