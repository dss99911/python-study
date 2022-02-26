import json
from urllib.request import urlopen

import requests

with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)


def download_file(url, file_path):
    file = requests.get(url, allow_redirects=True)
    open(file_path, 'wb').write(file.content)


def post_call():
    url = "https://somepage.com"

    payload="{\"key\":\""+"adsflkjasdf"+"\"}\n"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.loads(response.text)