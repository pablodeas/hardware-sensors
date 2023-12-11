#!/bin/python3

import time
import sys
import psutil
import tkinter as tk


def cpu_usage():
    print(psutil.cpu_percent())
"""    while True:
        yield psutil.cpu_percent(interval=1)
"""
    

root = tk.Tk()

label1 = tk.Label(root, text = "CPU ->")
label1.pack()

label2 = tk.Button(root, text= "BOTÃO", command=cpu_usage)
label2.pack()

root.mainloop()