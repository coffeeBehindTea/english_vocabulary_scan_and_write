import pytesseract
from PIL import Image

import return_dir
# from PIL import ImageEnhance

def GetWordList(dir):
    # 获取目录下图片
    PicList = return_dir.GetPicList(dir)    #! 要返回的单词列表
    word_list = []

    # 单词数量检测
    flag = 1
    check_time = 0

    # 遍历图片
    while flag:
        for pic in PicList:

            #! 图片绝对地址
            head = f"C:\\Users\\ldd\\Desktop\\tuxiang\\{dir}\\{pic}"
            # 读取图片
            img = Image.open(head)
            #! 转成灰度图，增加单词识别准确率
            img = img.convert('L')
            # img.show()
            # 识别文字
            string = pytesseract.image_to_string(img, lang='eng',)
            # print(string)
            #! 按照行拆分
            string = string.split('\n')
            #! 添加到单词列表
            for word in string:
                if not(string in word_list):
                    word_list += word
        # 检测单词列表的长度
        if len(word_list) == 80:
            break
        else:
            check_time += 1     
            if check_time >= 3:
                print("单词图片不全或其他问题")
                quit()  
    # 返回单词列表
    return word_list