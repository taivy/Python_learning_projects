import requests
import json
import re
from time import sleep

url = 'https://www.reddit.com/r/todayilearned/new/.json'

while True:
    req = requests.get(url).text

    j = json.loads(req)
    print(j)

    data = j.get('data', {}).get('children', [])
    print(data)
    for item in data:
        title = item.get('data', {}).get('title')
        re.sub(r'(TIL)|(Today I learned)|(Today I learned that)', '', title)
        url = item.get('data', {}).get('url')
        print(title, url)
    sleep(30)


print(data)
