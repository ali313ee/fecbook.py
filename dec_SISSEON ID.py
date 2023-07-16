#Decoded By Hso : @sis_f  On Bot : @sis_ff_bot 



copyright = '@psh_team'
import webbrowser
webbrowser.open('https://t.me/bsx_h2')
import requests
import time
import os
linux = 'clear'
windows = 'cls'
L = '\x1b[1;95m'
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'

def login():
    time1 = time.localtime()
    time2 = time.strftime('%d/%m/%Y')
    time3 = time.strftime('%H:%M:%S')
    print(f'''{F}[استمتع بوقتك] ''')
    print(f'''{Z}[Date] :{C} [{time2}]''')
    print(f'''{C}[The time] :{Z} [{time3}]''')
    username = str(input(f'''{F}يوزلر الحساب : {Z}'''))
    password = str(input(f'''{F}باسورد الحساب : {Z}'''))
    os.system([
        linux,
        windows][os.name == 'nt'])
    url = 'https://www.instagram.com/accounts/login/ajax/'
    data = {
        'username': f'''{username}''',
        'enc_password': f'''#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}''',
        'queryParams': '{}',
        'optIntoOneTap': 'false' }
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '275',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
        'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': 'bc3d5af829ea',
        'x-requested-with': 'XMLHttpRequest' }
    k = requests.post(url, headers, data, **('headers', 'data'))
    if 'authenticated":true' in k.text or 'userId' in k.text:
        print(F + ' login True')
        print(L + '============================================================')
        os.system([
            linux,
            windows][os.name == 'nt'])
        sessionid = k.cookies['sessionid']
        print(sessionid)
    else:
        print(k.text)
        login()

login()

#Decoded By Hso : @sis_f  On Bot : @sis_ff_bot 

