
### 사용하고 있는 라이브러리와 버전을 txt파일에 저장
```shell
pip freeze > requirements.txt
```

### install libraries from requirements
```shell
pip install -r requirements.txt
```

### note python version
- for running project on same version, mention python version on README.md
- because, library versions are mentioned on requirements.txt. but python version is not mentioned


### create & activate venv
python -m venv pyspark_venv
source pyspark_venv/bin/activate

### install on venv
pip3 install geopy
- pip를 하면 안되는 경우가 있음. pip3 show geopy 를 해서, 설치 위치가 가상환경인지 확인

### deactivate
```shell
deactivate
```