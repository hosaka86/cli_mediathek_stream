#!/usr/bin/env python3

import configparser
import subprocess



config = configparser.ConfigParser()
config.read('config.ini')

playerbin = config['mediaplayer']['play']

prog1_name = config['prog1']['name']
prog1_url  = config['prog1']['url']

prog2_name = config['prog2']['name']
prog2_url  = config['prog2']['url']

prog3_name = config['prog3']['name']
prog3_url  = config['prog3']['url']
prog4_name = config['prog4']['name']
prog4_url  = config['prog4']['url']
prog5_name = config['prog5']['name']
prog5_url  = config['prog5']['url']
prog6_name = config['prog6']['name']
prog6_url  = config['prog6']['url']
prog7_name = config['prog7']['name']
prog7_url  = config['prog7']['url']

print("##LINUX CLI MEDIATHEK##")



print(f"1. {prog1_name}")
print(f"2. {prog2_name}")
print(f"3. {prog3_name}")
print(f"4. {prog4_name}")
print(f"5. {prog5_name}")
print(f"6. {prog6_name}")
print(f"7. {prog7_name}")


choise = input("Wähle deinen Sender: ")



if choise == "1":#
    subprocess.run([playerbin, prog1_url])
elif choise == "2":
    subprocess.run([playerbin, prog2_url])
elif choise == "3":
    subprocess.run([playerbin, prog3_url])
elif choise == "4":
    subprocess.run([playerbin, prog4_url])
elif choise == "5":
    subprocess.run([playerbin, prog5_url])
elif choise == "6":
    subprocess.run([playerbin, prog6_url])
elif choise == "7":
    subprocess.run([playerbin, prog7_url])
else:

    print("ende")
