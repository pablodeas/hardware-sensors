import psutil as ps
#import keyboard as key
import os, time

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def check_stats(cpu, memory, temperature):
    print(f"""
    > CPU:          {cpu}%
    > Memory:       {int(memory)}%
    > Temperature:  {int(temperature)}°C
    """)

try:
    while True:
        mem = ps.virtual_memory()
        temperatures = ps.sensors_temperatures()

        cores = temperatures['coretemp']
        current_temps = [temp.current for temp in cores]
        average_temp = sum(current_temps) / len(current_temps)

        cpu = ps.cpu_percent()
        memory = mem.percent
        temperature = average_temp

        clear()
        check_stats(cpu, memory, temperature)

        time.sleep(3)

except Exception as e:
    print(f"> Programa finalizado - {e}")