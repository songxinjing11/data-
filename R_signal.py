# -*- coding:utf-8 -*-
#1 顺序读取data_R中的文件的values值，保存成数组
#2 读取data_R第一个文件的数组，由350来判断:前面元素个数是否满足大于350
#3 从第一个满足的R点开始，向前取350，向后同理，共701个元素存入该文件对应矩阵的第一行
#4 之后每一个满足的R点都必须有如下性质:1,前后元素的个数均大于350个 2,比前一个满足的R点大至少700个
#5 每次取完的701个点，都存入新的一行
#6 按顺序读取data_R_re中的每一个文件，将每一个文件按如上方法写成矩阵，输出成C0000n.mat文件，并保存到新的data_dir文件夹中
#7 查看每一个mat文件的行数，选出最优行数

##data_R and data文件夹未更改，data_Re文件夹下为原data文件夹中.mat文件的复制版
import numpy as np
import os 
from scipy.io import loadmat
import scipy.io as io

matpath_R = '/home/student/yaoyuan/R signal/data_R'
matpath = '/home/student/yaoyuan/R signal/data_Re'



##主函数 mat_path为 B系列的位置
def necessary(mat_path):
    matname_path = os.listdir(mat_path)
    for matname in matname_path:
        matname_4 = matname[-1:-4]
        matname = os.path.join(mat_path,matname)
        array_1 = loadmat(matname)
        load = list(array_1.values())[0][0]
        m = np.transpose(load)
        print(np.shape(m))
        predict_1 = predict(m,350)
        item_1 = search(matname_4)
        matrix_generate(predict_1,item_1,350)



##每个数据产生矩阵并保存,matrix为list_r，item为A系列，k为数字大小
def matrix_generate(matrix,item,k):
    i = 0
    x = matrix.size
    y = 2*k + 1
    list_i = np.zeros((x,y))
    while i < x:
        m = int(matrix[i])
        print(type(m-k))
        print(type(m+k+1))
        print(type(list_i[i]))
        list_i[i] = item[m-k:m+k+1]   
        i = i + 1
    io.savemat('/home/student/yaoyuan/R signal/target', {'data': list_i})


#A00001和B00001一一对应，name为想要名字的部分，例00001,对应A00001.mat和B00001.mat
def search(name):
    for item in os.listdir('/home/student/yaoyuan/R signal/data_Re'):
        item_path = os.path.join('/home/student/yaoyuan/R signal/data_Re', item)
        if os.path.isfile(item_path):
            if name in item:
                return item

#判断B系列合适的R波点,matrix为B系列产生的矩阵，k为想要的大小，点(原数据中的位置)存入list_r
def predict(matrix,k):
    i = 0
    tag = 0 
    matrix = np.squeeze(matrix)
    l = matrix.size
    list_r=[]
    while i < l:
        m = matrix[i]
        if m < 9000 - k + 1: ## smaller than 
            if m < k:
                i = i + 1
                continue
            elif m > k:
                if tag == 0:
                    list_r.append(m)
                    tag = tag + 1
                    i = i + 1
                    continue
                else:
                    if (m - list_r[-1]) > 2*k:
                        list_r.append(m)
                    if (m - list_r[-1]) < 2*k:
                        i = i + 1
                        continue
        i = i + 1
    list_r1 = np.transpose(list_r)
    return list_r1
    print(list_r1.size())
    print(list_r)

necessary(matpath_R)
        


                


            



    
    
  
















     

