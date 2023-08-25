#!/bin/python3

# If you get an error, change the environment variable above

import time
import sys
import psutil

def move_cursor_up(lines):
    """Move the cursor up by a specified number of lines."""
    sys.stdout.write(f"\033[{lines}A")

def cpu_usage_generator():
    while True:
        yield psutil.cpu_percent(interval=1)

def cpu_temperature_generator():
    while True:
        temps = psutil.sensors_temperatures()
        core_temps = temps.get('coretemp', [])
        yield core_temps[0].current if core_temps else "N/A"

def load_average_generator():
    while True:
        yield psutil.getloadavg()[0]

def memory_usage_generator():
    while True:
        mem = psutil.virtual_memory()
        yield mem.percent

def display_values(titles, generators, delay=2):
    """
    Display titles and iteratively update their values using generators.

    :param titles: A list of titles to be displayed.
    :param generators: A list of generator functions.
    :param delay: The delay in seconds between value updates.
    """
    num_titles = len(titles)
    if len(generators) != num_titles:
        raise ValueError("Number of titles must match number of generators.")
    
    try:
        while True:
            for i in range(num_titles):
                print(f"{titles[i]}: {next(generators[i])}")
            move_cursor_up(num_titles)
            time.sleep(delay)
    except KeyboardInterrupt:
        pass
    finally:
        for i in range(num_titles):
            print(f"{titles[i]}: ")  # Clears the last values, keeping only the titles.

# Usage:
titles = ["CPU Usage", "CPU Temperature", "Load Average", "Memory Usage"]
generators = [cpu_usage_generator(), cpu_temperature_generator(), load_average_generator(), memory_usage_generator()]
display_values(titles, generators)

