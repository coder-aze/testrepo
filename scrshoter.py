import pyautogui  #pip install pyautogui
import time
import random
import os
os.chdir(r"C:\Users\ANONYMOUS\Desktop")
#name identification as random
names=random.choices(["a","b","c","d","e","f","g","h","i"],k=6)
#standby time: second
time.sleep(2)

screen=pyautogui.screenshot()
screen.save(str(names)+".png")


