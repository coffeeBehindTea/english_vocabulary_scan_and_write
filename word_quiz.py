import pyautogui as pg
import time
import random

import get_word_from_pic


pg.PAUSE = 0.1


# with open("eng_word.txt", 'r') as f:
#     data = f.read()

# lst = data.split('\n')
# random.shuffle(lst)

dir = str(input("dir is: "))

time.sleep(5)

# 获取单词表
word_list = get_word_from_pic.GetWordList(dir)
# 打乱单词表
random.shuffle(word_list)
# print(word_list)

char_list = [',','.','']

# 计数变量
index = 1
# 遍历整个单词表
for word in word_list:
    #! 一列40个词，留出5s换行时间
    if index == 40:
        print("move your mouse!")
        time.sleep(5)
        index += 1
    #! 因为单词间空隙大，中间会间隔一行空行
    elif not (word in char_list or len(word) == 1):
        print(word)
        pg.typewrite(word)
        pg.press('down')
        index += 1

# f.close()
