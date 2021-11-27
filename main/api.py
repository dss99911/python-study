import requests
url = "http://httpbin.org/get"
#%% get
params = {'param1': 'value1', 'param2': 'value'}
headers = {'Content-Type': 'application/json; charset=utf-8'}
cookies = {'session_id': 'sorryidontcare'}
response = requests.get(url, params=params, headers= headers, cookies=cookies)
response.text
response.request # 내가 보낸 request 객체에 접근 가능
response.status_code # 응답 코드
response.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발동
response.json() # json response일 경우 딕셔너리 타입으로 바로 변환


#%% post
import json
data = {'outer': {'inner': 'value'}}
res = requests.post(url, data=json.dumps(data))
