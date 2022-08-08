import urllib.request
import threading
from time import sleep
import requests
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
print('true' if connect() else quit())
import uuid
import os , sys
key = uuid.getnode()
if os.name == 'posix':
    os.system('clear')
elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
else:
    pass
count= len(open('cookie.txt','r').readlines())
print('__________________________________________\n')
print('[>___> _ *]  BOT VIRTUAL SHARE FACEBOOKS (Version 1.0)')
print(f'[>___> _ *]  NUMBER OF ACCOUNT IN USING ({count}) ')
print('__________________________________________\n')
link_ = input('[_ADD_]* => Link cần share: ')
thread_ = int(input('[_ADD_]* => Start Thread: '))
print('________________________________________')
def get_token(ck):
    link = 'https://www.facebook.com/adsmanager/manage';header={"cookie":ck}
    re = requests.get(link,headers=header).text
    try:
        try:
            link = 'https://www.facebook.com/adsmanager/manage'
            re = requests.get(link,headers=header).text
            li = re.split('window.location.replace("')[1].split('"')[0].replace('\/','/')
            link = requests.get(li,headers=header).text
            token = link.split('accessToken="')[1].split('";')[0]
        except:
            try:
                link = 'https://www.facebook.com/adsmanager/manage'
                re = requests.get(link,headers=header).text
                sleep(4)
                link = 'https://www.facebook.com/adsmanager/manage'
                re = requests.get(link,headers=header).text
                li = re.split('window.location.replace("')[1].split('"')[0].replace('\/','/')
                link = requests.get(li,headers=header).text
                token = link.split('accessToken="')[1].split('";')[0]
            except:
                link = 'https://www.facebook.com/adsmanager/manage'
                re = requests.get(link,headers=header).text
                sleep(4)
                link = 'https://www.facebook.com/adsmanager/manage'
                re = requests.get(link,headers=header).text
                li = re.split('window.location.replace("')[1].split('"')[0].replace('\/','/')
                link = requests.get(li,headers=header).text
                token = link.split('accessToken="')[1].split('";')[0]
    except:
        print('Get Token Lỗi !')
        sleep(1000)
    return token
def run(s):
    try:
        access_token = str(s).split('|')[0]
        cookie = str(s).split('|')[1]
    except:
        print('Token running ... ',end='  \r')
        access_token = get_token(s)
        print('Token Success ... ',end='  \r')
        cookie = s
    try:
        pulis = requests.get(f'https://graph.facebook.com/me/accounts?fields=access_token&limit=10000&access_token={access_token}',headers={'cookie':cookie}).json()
    except:
        raise "Not get page !!! . "
    def share(k):
        # pulished
        try:
            access_tk = pulis['data'][k]['access_token'];requests.post(f'https://graph.facebook.com/me?is_published=0&access_token={access_tk}',headers={'cookie':cookie}).json()
        except:pass
        def __start__(l):
            #share
            while(True):
                try:
                    share_ = requests.post(f'https://graph.facebook.com/me/feed?link={link_}&published=false&access_token={access_tk}',headers={'cookie':cookie});print(share_.json())
                    try:
                        if 'id' in share_.text:print('id :'+share_.json()['id'])
                    except:pass
                except:
                    pass
        for l in range(thread_):
            threading.Thread(target=__start__,args=(l,)).start()
    for k in range(len(pulis['data'])):
        threading.Thread(target=(share),args=(k,)).start()
for s in open('cookie.txt','r',encoding='utf-8').readlines():
        threading.Thread(target=(run),args=(s.strip('\n'),)).start()