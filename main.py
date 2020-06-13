import requests

print('heloo world')
print('oke sudah bisa')
try:
    r = requests.get('https://google.com')
    print(r.status_code)
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('Ada eror',e)

