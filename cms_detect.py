import os, requests, time
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
from colorama import Fore, Style


def screen_clear():
    _ = os.system('cls')


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW
pk =Fore.LIGHTMAGENTA_EX

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

def laravelcheck (star):
    if "://" in star:
      star = star
    else:
      star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/.env"
    check = requests.get(url, headers=headers, timeout=3)
    resp = check.text
    try:
        if "DB_HOST" in resp:
            print(f"{yl}[ VALID ] Laravel => {pk} {star}\n")
            mrigel = open("Laravel.txt", "a")
            mrigel.write(f'{star}.env\n')
        else:
            print(f"{bl} [ OTHER ] => {white} {star}\n")
            mrigel = open("Othercms.txt", "a")
            mrigel.write(f'{star}.env\n')
    except:
        pass
def wpcheck (star):
    if "://" in star:
      star = star
    else:
      star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/wp-content/"
    check = requests.get(url, headers=headers, timeout=3)
    try:
        if check.status_code == 200:
            print(f"{gr}[ VALID ] Wordpress => {pk} {star}\n")
            mrigel = open("/Wordpress.txt", "a")
            mrigel.write(f'{star}\n')
        else:
            print(f"{bl} [ OTHER ] => {white} {star}\n")
            mrigel = open("Othercms.txt", "a")
            mrigel.write(f'{star}.env\n')
    except:
        pass


def filter(star):
    try:
       laravelcheck(star)
       wpcheck(star)
    except:
       pass


def main():
    print(f'''    
        __                                __   _       ______     ________  ________{wh}
       / /   ____ __{bl}_PT_RUMAH_DIMAZ_{bl} __   _____  / /  | |     / / __ \   / ____/  |/  / ___/{red}
      / /   / __ `/ ___/ __ `/ | / / _ \/ /   | | /| / / /_/ /  / /   / /|_/ /\__ \ {bl}
     / /___/ /_/ / /  / /_/ /| |/ /  __/ /    | |/ |/ / ____/  / /___/ /  / /___/ / {yl}
    /_____/\__,_/_/   \__,_/ |___/\___/_/     |__/|__/_/       \____/_/  /_//____/  {gr}
                                                        {wh}        Laravel Check {red} CMS {res}                    
    ''')
    list = input(f"{wh}Masukan Listnya Bosku/{red} {gr}${res} ")
    star = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(50)
       ThreadPool.map(filter, star)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass
       
if __name__ == '__main__':
    screen_clear()
    main()