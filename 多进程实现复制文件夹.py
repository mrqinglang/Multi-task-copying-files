# --*-- coding: utf-8 --*--
# @Date     : 2019/10/10
# @Author   : mrqinglang
# @software : PyCharm

import os
import multiprocessing
import time

def copy_file(q,file_name, old_folder_name, new_folder_name):
    #print("%s-->%s文件名为%s"%(old_folder_name, new_folder_name, file_name))
    old_f = open(old_folder_name+"/"+file_name,'rb')
    new_f = open(new_folder_name + "/" + file_name, 'wb')
    #connect = old_f.read()
    while True:
        line = old_f.readline()
        if not line:
            break
        new_f.write(line)

    old_f.close()
    new_f.close()
    q.put(file_name)

def main():
    #输入文件名字
    old_folder_name = input("请输入拷贝的文件名称")
    #创建新的文件夹
    try:
        new_folder_name = old_folder_name + "复件"
        os.mkdir(new_folder_name)
    except:
        pass
    #获取文件夹内所有文件  listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)
    #创建进程池
    po = multiprocessing.Pool(3)
    #创建队列
    q = multiprocessing.Manager().Queue()
    #向进程池中添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))
    po.close()
    po.join()
    copy_num = 0
    old_num = len(file_names)
    #print(old_num)
    while True:
        #file_name = q.get()
        copy_num += 1
        #print("已经完成copy%s"%file_name)
        print("\r拷贝进度为%.2f%%"%(copy_num*100/old_num),end='')
        time.sleep(0.05)
        if copy_num >= old_num:
            break
    copy_num = 0
    while True:
        file_name = q.get()
        print("\r已经完成%s的拷贝"%file_name,end='')
        time.sleep(0.05)
        copy_num += 1
        if copy_num >= old_num:
            break


if __name__ == "__main__":
    main()
