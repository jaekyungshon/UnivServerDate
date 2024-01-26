import urllib.request
import time

while True:
    date = urllib.request.urlopen('https://info.hansung.ac.kr/').headers['Date']
    #info = ''.join(list(date)[17:25])
    time.sleep(0.001)
    #print(info)
    print(date)

