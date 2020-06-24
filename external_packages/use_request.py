import requests

url = 'https://detik.com'
#response = requests.get(url)
#if response.status_code == 200:
#    print('sukses')
#elif response.status_code == 404:
#    print('not found')

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success Response = {response.status_code}')
        print(f'content{response.text}')
    else:
        print(f'Wah ada kesalahan {response.status_code}')
except Exception as e:
    print('There is an error',e)
print('Program end')