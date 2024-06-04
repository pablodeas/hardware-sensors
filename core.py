import psutil as ps
import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def get_stats():
    try:
        mem = ps.virtual_memory()
        temperatures = ps.sensors_temperatures()

        cores = temperatures['coretemp']
        current_temps = [temp.current for temp in cores]
        average_temp = sum(current_temps) / len(current_temps)

        cpu = ps.cpu_percent()
        memory = mem.percent
        temperature = average_temp

        stats_str = f"""
        CPU:          {cpu}%
        Memory:       {int(memory)}%
        Temperature:  {int(temperature)}°C
        """
        
        return stats_str
    
    except Exception as e:
        return f"> Erro: {str(e)}"
