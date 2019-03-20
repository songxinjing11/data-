import numpy as np
import scipy.io as io
import os
def npy_mat(npy_path,mat_path):
    npyname_path = os.listdir(npy_path)
    for npyname in npyname_path:
        name = npyname[:-4]
        
        npyname = os.path.join(npy_path,npyname)
        
        name = name[46:]
        mat_name = name+'.mat'
        mat_name = os.path.join(mat_path,mat_name)
        npy = np.load(npyname)
        io.savemat(mat_name,{'data': npy})
npy_mat(r'/home/student/yaoyuan/R signal/Data_300Hz_npy',r'/home/student/yaoyuan/R signal/Data_300Hz_mat')
