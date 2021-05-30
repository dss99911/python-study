# Wheel

## Reference
- https://realpython.com/python-wheels/


## Summary
- pip install을 할 때, Source Distribution 대신에 Wheel용 Distribution에서 다운 받아서 설치하는 것을 의미 하는 것 같음. 
- Source Distribution보다 빠르다
    - Source Distribution은 소스 Repo같은 것 같음.
    - 소스를 다운받아서, 빌드하기 때문에, 빌드가 오래 걸리는 만큼 설치 시간이 오래걸림.
- 디폴트로, wheel distribution에서 다운 받아 설치하고, wheel에 없으면 source distribution에서 다운 받아 설치해서, package 사용자는 설치시 특별히 설정할 필요는 없는 것 같음.

## Wheel의 장점
- https://realpython.com/python-wheels/#advantages-of-python-wheels