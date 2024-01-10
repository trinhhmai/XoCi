import requests
import random
import time
import os
import getpass
from colorama import Fore
import threading

author = "LeHuuKhoa"
print("Author: " + author)
script = "AutoChat Bot Discord"
print("Script: " + script)
twitter = "@lehuukhoa1308"
print("Twitter: " + twitter)
print("=========================================\n")

__tokens = []

try:
    file = open("token.txt", "r")
    if file.readline() == "tokens-here":
        print(f"{Fore.MAGENTA}Couldnt load tokens from file 'tokens.txt'\nEnter token manually [input hidden]")
        file_loaded = False
    else:
        file_loaded = True
except Exception as e:
    print(f"{Fore.MAGENTA}Couldnt load tokens from file 'tokens.txt'\nEnter token manually [input hidden]")
    file_loaded = False

if file_loaded == False:
    token = str(getpass.getpass(f"{Fore.LIGHTMAGENTA_EX}Token used to spam : {Fore.RESET}"))
    tkin = token[:len(token)//2]
    print(f"{Fore.LIGHTMAGENTA_EX}Token begginging with {tkin}{Fore.RESET}")
    __tokens.append(token)

elif file_loaded == True:
    lines = file.readlines()
    for line in lines:
        __tokens.append(line.strip("\n"))
    print(f"{Fore.MAGENTA}Loaded {len(__tokens)} tokens")

time.sleep(1)

channel_id = input("Nhap ID channel: ")
thoigiangui = int(input("Dat thoi gian gui tin nhan(giay): "))
thoigiandelay = int(input("Dat thoi gian gui giua cac token(giay): "))

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')
# Lấy tin nhấn trong file tinnhan.txt đoc từng dòng
with open("tinnhan.txt", "r" , encoding="utf-8") as f:
    words = f.readlines()
# Lấy authorization trong file token.txt 
# Lấy authorization thì F12 vào network tìm messages , tìm tới authorization trong headers 
#with open("token.txt", "r") as f:
#    authorization = f.readline().strip()   
# ID Kenh Cách lấy id kenh
# Vào Mì Gói #ThaoLuan-Node có đường dẫn là https://discord.com/channels/833558557327884318/955649819404300289
# 955649819404300289 là id kênh
channel_id = channel_id.strip()



def start(token):
    
    while True:
        
        # requests post
        # Gửi tin nhắn
        random.shuffle(words)
        payload = {
            'content': random.choice(words).strip()
        }
        #Token
        headers = {"Authorization" : f"{token}"}
        
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages",headers=headers,data=payload)
        print(Fore.WHITE + "Tin nhan da gui: ")
        print(Fore.YELLOW + payload['content'])
        # Gửi tin nhắn
        # requests post
        
        # requests get
        # Nhận tin nhắn
        # get messages của mình từ kênh
        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
        # Check status code 
        if response.status_code == 200:
            # xuất messages dạng json 
            messages = response.json()
            if len(messages) == 0:
                is_running = False
                break
            else:
                time.sleep(thoigiangui)
        else:
            print(f'Khong nhan tin tren kenh: {response.status_code}')

        # requests get
        # Nhận tin nhắn





for token in __tokens:
    threading.Thread(target=start, args=(token,)).start()
    time.sleep(thoigiandelay)



