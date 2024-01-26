import urllib.request
import time

try:
    while True:
        date = urllib.request.urlopen('https://info.hansung.ac.kr').headers['Date']
        gmp = "".join(list(date)[17:19])
        cha = ''"
        if 0 <= int(gmp) < 15:
            cha += str(int(gmp) + 9)
        elif int(gmp) == 15:
            cha += '00'
        else:
            cha += str(int(gmp) + 9 - 24)
        time.sleep(0.001)
        print("%02d" % int(cha) + "{0}".format(''.join(list(date)[19:25])))
except:
    print("오류입니다")