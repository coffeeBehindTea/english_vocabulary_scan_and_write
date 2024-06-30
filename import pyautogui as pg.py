import pyautogui as pg
import time
import random

pg.PAUSE = 0.1

with open(r"C:\Users\ldd\Desktop\list22\words.txt", "r") as f:
    data = f.read().splitlines()

random.shuffle(data)
print(len(data))

time.sleep(4)
index = 0
for word in data:
    if index == 40:
        print("move your mouse")
        time.sleep(5)
    pg.typewrite(word)
    pg.press("down")
    index += 1
    


# random.shuffle(data)
# print(data)
# a = input()