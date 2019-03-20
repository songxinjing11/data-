# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:51:21 2019

@author: Administrator
"""
import numpy as np
import scipy.io as io
#加载.npy文件：
numpy_file = np.load('G:/AF_TF/Record_Label.npy')
io.savemat('Record.mat',{'data':numpy_file})

numpy_file = np.load('G:/AF_TF/Label.npy')
io.savemat('Label.mat',{'data':numpy_file})

numpy_file = np.load('G:/AF_TF/DataSet_250Hz/A0001.npy')
io.savemat('A1.mat',{'data':numpy_file})

numpy_file = np.load('G:/AF_TF/Data_300Hz_npy/A00014.npy')
io.savemat('AA1.mat',{'data':numpy_file})