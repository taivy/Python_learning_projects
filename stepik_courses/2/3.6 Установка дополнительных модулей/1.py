import requests
f = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
while f.text[:2] != 'We':
    f = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + f.text)
    print(f.text)
