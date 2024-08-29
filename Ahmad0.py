import requests, random, os, webbrowser, time
import datetime

now = datetime.datetime.now()
ta = now.year
bu = now.month
ha = now.day
ho = now.hour
hs = now.minute

#####mortada######
E = '\033[1;31m'
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[2;35m"
B = '\033[2;36m'
Y = '\033[1;34m'
M = '\x1b[1;37m'
S = '\033[1;33m'
U = '\x1b[1;37m'
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
O = '\x1b[1;34m'
R = '\x1b[1;35m'
G = '\x1b[1;36m'
BPurple = '\x1b[1;35m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a26 = '\x1b[38;5;5m'
#####mortada######


os.system('clear')
print(f'\n{Z}\n\n                   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n                 ¶¶¶¶¶¶             ¶¶¶¶¶¶¶\n              ¶¶¶¶                       ¶¶¶¶\n             ¶¶¶                             ¶¶\n            ¶¶                                ¶¶\n           ¶¶                                 ¶¶\n          ¶¶                                   ¶¶\n          ¶¶ ¶¶                             ¶¶ ¶¶\n          ¶¶ ¶¶                             ¶¶  ¶\n          ¶¶ ¶¶                             ¶¶  ¶\n          ¶¶  ¶¶                            ¶¶ ¶¶\n          ¶¶  ¶¶                           ¶¶  ¶¶\n           ¶¶ ¶¶   ¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶   ¶¶ ¶¶\n            ¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶\n             ¶¶¶ ¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶ ¶¶¶\n    ¶¶¶       ¶¶  ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶  ¶¶      ¶¶¶¶\n   ¶¶¶¶¶     ¶¶   ¶¶¶¶¶¶¶   ¶¶¶   ¶¶¶¶¶¶¶   ¶¶     ¶¶¶¶¶¶\n  ¶¶   ¶¶    ¶¶     ¶¶¶    ¶¶¶¶¶    ¶¶¶     ¶¶    ¶¶   ¶¶\n ¶¶¶    ¶¶¶¶  ¶¶          ¶¶¶¶¶¶¶          ¶¶  ¶¶¶¶    ¶¶¶\n¶¶         ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶        ¶¶\n¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶      ¶¶¶¶¶¶¶¶\n  ¶¶¶¶ ¶¶¶¶¶      ¶¶¶¶¶              ¶¶¶ ¶¶     ¶¶¶¶¶¶ ¶¶¶\n          ¶¶¶¶¶¶  ¶¶¶  ¶¶           ¶¶  ¶¶¶  ¶¶¶¶¶¶\n              ¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶\n                  ¶¶ ¶¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶¶\n                ¶¶¶¶  ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶   ¶¶¶¶¶\n            ¶¶¶¶¶ ¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶   ¶¶ ¶¶¶¶¶\n    ¶¶¶¶¶¶¶¶¶¶     ¶¶                 ¶¶      ¶¶¶¶¶¶¶¶¶\n   ¶¶           ¶¶¶¶¶¶¶             ¶¶¶¶¶¶¶¶          ¶¶\n    ¶¶¶     ¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶     ¶¶¶\n      ¶¶   ¶¶¶           ¶¶¶¶¶¶¶¶¶           ¶¶¶   ¶¶\n      ¶¶  ¶¶                                   ¶¶  ¶¶\n       ¶¶¶¶                                     ¶¶¶¶\n\n       المطور مرتضى ☠️ | @M_R_Q_P')
print('\n')
print(f'{X}▭▬▭'*20)
token = input(f"{Z}[{Z}?{Z}]{Z} 𝗧𝗢𝗞𝗘𝗡 : {B}")
print(f'{F}▭▬▭'*20)
iD = input(f"{F}[{F}?{F}]{F} 𝗜𝗗 : {F}")
os.system('clear')
print(f"""
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{C}[{X}1{C}]{X} user | #_#_#
{C}[{X}2{C}]{X} user | #__#_#
{C}[{X}3{C}]{X} user | ####_
{C}[{X}4{C}]{X} user | ####
{C}[{X}5{C}]{X} user | #_###
{C}[{X}6{C}]{X} user | #.#.#
{C}[{X}7{C}]{X} user | ##_##
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{C}[{X}8{C}]{R} Username programmer{B} : MORTADA
{C}[{X}9{C}]{R} Username CHNALL{B} : PYTHON
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
""")
x2 = input(f"{B}[{B}?{B}]{X} CHOSE : {F}")
os.system('clear')
def mortada():
    while True:
	    m = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm"))
	    o = "".join(random.choices("_"))
	    r = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
	    t = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
	    s = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
	    R6 = "".join(random.choices("QWERTYUIOPASDFGHJKLZXCVBNM0123456789"))
	    R7 = "".join(random.choices("QWERTYUIOPASDFGHJKLZXCVBNM0123456789"))
	    d = "".join(random.choices("QWERTYUIOPASDFGHJKLZXCVBNM0"))
	    
	    if x2 == "1":
	        user = m + '_' + r + '_' + t 
	    elif x2 == "2":
	        user = m + '__'+r+'_'+t
	    elif x2 == "3":
	        user = m + o + s + o + '_'
	    elif x2 == "4":
	        user = m + r + t + s
	    elif x2 == "5":
	        user = d + '_' + t + s + d
	    elif x2 == "6":
	        user = d + '.' + s + '.' + d 
	    elif x2 == "7":
	        user = d + t + '_' + s + m
	    elif x2 == '8':
	        webbrowser.open('https://t.me/M_R_Q_P')
	        time.sleep(2)
	        exit()
	    elif x2 == '9':
	        webbrowser.open('https://t.me/MHND_X1')
	        time.sleep(2)
	        exit()
	    
	    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
	    headers = {
	        'accept': '*/*',
	        'accept-encoding': 'gzip, deflate, br',
	        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	        'content-length': '56',
	        'content-type': 'application/x-www-form-urlencoded',
	        'cookie': 'mid=WzoscQAEAAF_6GtVX1t5dOYWEp8t; ig_did=46CAAE8B-316F-4CAC-8FC3-17F9B8A1ABBF; ig_nrcb=1; datr=WUqAZNpT7esRe8Zvmlyg6e9w; csrftoken=yEqvi73A3qJCryIWsy5kYhEy0A2wMrol; ds_user_id=2167209024',
	        'dnt': '1',
	        'dpr': '1',
	        'origin': 'https://www.instagram.com',
	        'referer': 'https://www.instagram.com/accounts/emailsignup/',
	        'sec-ch-prefers-color-scheme': 'light',
	        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
	        'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Google Chrome";v="109.0.5414.120", "Chromium";v="109.0.5414.120"',
	        'sec-ch-ua-mobile': '?0',
	        'sec-ch-ua-model': '',
	        'sec-ch-ua-platform': '"Windows"',
	        'sec-ch-ua-platform-version': '"0.1.0"',
	        'sec-fetch-dest': 'empty',
	        'sec-fetch-mode': 'cors',
	        'sec-fetch-site': 'same-origin',
	        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
	        'viewport-width': '478',
	        'x-asbd-id': '129477',
	        'x-csrftoken': 'yEqvi73A3qJCryIWsy5kYhEy0A2wMrol',
	        'x-ig-app-id': '936619743392459',
	        'x-ig-www-claim': '0',
	        'x-instagram-ajax': '1009679609',
	        'x-requested-with': 'XMLHttpRequest'
	    }
	    data = {
	        'email': '',
	        'first_name': '',
	        'username': user,
	        'opt_into_one_tap': 'false'
	    }
	
	    res = requests.post(url, headers=headers, data=data).text
	    if "You can't start your username with a period." in res or \
	       "This username isn't available. Please try another." in res or \
	       "You can't end your username with a period." in res or \
	       "A user with that username already exists." in res:
	        print(f'{Z} Bad User : {user}')
	        print(f'{X}▭▬▭'*20)
	    else:
	        print(f" {F} Good : {C}{user} ")
	        print(f'{X}▭▬▭'*20)
	        tlg = f'''
	<───━𓆩𝘔𝘖𝘙𝘛𝘈𝘋𝘈𓆪‏━───>
	✅ 𝘜𝘚𝘌𝘙  : {user}
	🇮🇶𝘗𝘖𝘙𝘎𝘙𝘈𝘔 ☠️ - @M_R_Q_P - 𝘔𝘖𝘙𝘛𝘈𝘋𝘈
	𝗧𝗜𝗠𝗘 𖢝 : {ta} / {bu} / {ha}
	<───━𓆩𝘔𝘖𝘙𝘛𝘈𝘋𝘈𓆪‏━───>'''
	
	        requests.post(f"https://api.telegram.org/bot{token}/sendvideo?chat_id={iD}&video=https://t.me/dkdhdkdv/5&caption=" + str(tlg))
	        
mortada()