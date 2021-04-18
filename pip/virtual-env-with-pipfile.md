
### use pipenv to create Pipfile & Pipfile.lock
```shell
pip install pipenv
```

### create Pipfile or migrate to Pipfile from requirements.txt
```shell
pipenv install
```

### update requirements & download package if not installed.
```shell
pipenv update
```

### update requirements only
```shell
pipenv lock
```

### activate 
```shell
pipenv shell
```

### install for dev env
```shell
pip install <package> --dev
```