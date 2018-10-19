# -*- coding: utf-8 -*-
# @Author: wengjiacheng
# @Date:   2018-10-18 16:30:54
# @Last Modified by:   wengjiacheng
# @Last Modified time: 2018-10-19 19:06:35
import random
import numpy as np
import matplotlib.pyplot as plt

num=10
p=0.6

ER_matrix=np.zeros([num,num])
matrix_num=np.arange(num)

for i in matrix_num:
	del_list=np.arange(i+1)
	matrix_num_del_i=np.delete(matrix_num,del_list)
	for j in matrix_num_del_i:
		if(p>=random.random()):
			ER_matrix[i][j]=1

ER_matrix+=ER_matrix.T-np.diag(ER_matrix.diagonal())
print(ER_matrix)






