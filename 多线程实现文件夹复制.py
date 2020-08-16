
# --*-- coding: utf-8 --*--
# @Date     : 2019/12/8
# @Author   : mrqinglang
# @software : PyCharm
"""

import threading
import os

# 创建拷贝任务
def copy_work(source_dir, dest_dir, file_name):
    # 打开目标文件
    old_f = open(source_dir + '/' + file_name,'rb')
    new_f = open(dest_dir + '/' + file_name, 'wb')
    #connect = old_f.read()
    while True:
        line = old_f.readline()
        if not line:
            break
        new_f.write(line)
    old_f.close()
    new_f.close()

def main():
    # 指定源目录和目标目录
    source_dir = input("请输入拷贝的文件名称：")
    dest_dir = input("输入目标目录")
    if os.path.exists(source_dir):# 判断是否存在
        if os.path.exists(dest_dir):
            # shutil.rmtree(dest_dir)
            print("目标文件夹已存在，如果目录内存在同名文件，将覆盖")
        else:
            # 创建目标文件夹
            os.mkdir(dest_dir)
        # 获取源目录文件列表
        source_file_list = os.listdir(source_dir)
        print("复制内容如下%s"%source_file_list)
        old_num = len(source_file_list)
        copy_num = 0
        for file_name in source_file_list:
            copy_thread = threading.Thread(target=copy_work, args=(source_dir, dest_dir, file_name))
            copy_thread.start()
            print("\r%s完成复制"%file_name,end='')
            copy_num+=1
            print("\r拷贝进度为%.2f%%"%(copy_num*100/old_num),end='')
    else:
        print("请确认源目录是否存在或者是否拼写错误")


if __name__ == '__main__':
    main()
