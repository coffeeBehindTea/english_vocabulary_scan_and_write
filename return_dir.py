import os

def GetPicList(dir):
    # 获取目录下文件
    file_list = os.listdir(dir)
    #! 图片后缀
    pic_list = [".jpg",".png",".jpeg"]
    #! 图片列表
    pic_file_list = []

    # 遍历文件列表
    for file in file_list:
        #! 提取后缀
        ext = os.path.splitext(file)[-1]
        #! 如果是文件就添加
        if ext in pic_list:
            pic_file_list.append(file)
    # 返回图片列表
    return pic_file_list