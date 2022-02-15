import joblib
# 주로, 객체를 압축하여 저장 및 로드를 사용.
# 그외, memory캐시와, parallel지원 함.

# pickle과 비교
# pickle이 3.8버전부터는 large numpy array에도 더 빠르다는 것 같음.
# joblib을 쓰는 경우는 memory캐시나 parallel을 사용하는 경우에만 사용.. 하지만, 어떤 식으로 사용하는지 잘 모름.

lst = [('text', [1, 2, 3])]

filename = 'test.joblib'

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f'A({self.a}, {self.b})'


a = A(1,2)

#%%
joblib.dump(lst, filename)
# 기본적으로 joblib.dump()는 zlib 압축 방법을 사용하지만, gzip으로도 가능
joblib.dump(lst, filename + '.gz', compress=('gzip', 3))

joblib.dump(a, filename + "-A")

#%%
print(joblib.load(filename))
print(joblib.load(filename + "-A"))  # class 자동으로 로딩함