import matlab.engine
from scipy.io import loadmat
import numpy as np

array_1 = loadmat('/home/student/yaoyuan/R signal/data_Re/A00001.mat')
load = list(array_1.values())[0][0]
m = np.transpose(load)
print(len(m))
