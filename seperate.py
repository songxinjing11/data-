'''from scipy.io import loadmat
import numpy as np
import os
import scipy.io as io
matpath = '/home/student/yaoyuan/R signal/data'
target = '/home/student/yaoyuan/R signal/data_Re'
def trans(mat_path,target):
    matname_path = os.listdir(mat_path)
    for matname in matname_path:
        if matname.endswith(".mat"):


        
trans(matpath,target)
'''
# -*- coding: UTF-8 -*- 
import os
import shutil
def cp_tree_ext(exts,src,dest):
  """
  Rebuild the director tree like src below dest and copy all files like XXX.exts to dest 
  exts:exetens seperate by blank like "jpg png gif"
  """
  fp={}
  extss=exts.lower().split()
  for dn,dns,fns in os.walk(src):
    for fl in fns:
      if os.path.splitext(fl.lower())[1][1:] in extss:
        if dn not in fp.keys():
          fp[dn]=[]
        fp[dn].append(fl)
  for k,v in fp.items():
      relativepath=k[len(src)+1:]
      newpath=os.path.join(dest,relativepath)
      for f in v:
        oldfile=os.path.join(k,f)
        if not os.path.exists(newpath):
          os.makedirs(newpath)
        shutil.copy(oldfile,newpath)

cp_tree_ext('mat','/home/student/yaoyuan/R signal/data','/home/student/yaoyuan/R signal/data_Re')
