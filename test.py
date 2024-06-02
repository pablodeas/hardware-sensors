#
import psutil as ps
import os
import time

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


while True:
    print(ps.cpu_percent(interval=3))

