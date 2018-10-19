# -*- coding: utf-8 -*-
# @Author: wengjiacheng
# @Date:   2018-10-18 16:30:54
# @Last Modified by:   JasonWong97
# @Last Modified time: 2018-10-19 21:22:39
import random
import numpy as np
import matplotlib.pyplot as plt

		
num=10#初始时网络有 num 个节点
p=0.6#每对节点以概率 p 被选择，进行连边，不允许重复连边。

# 初始化矩阵
ER_matrix=np.zeros([num,num])
matrix_num=np.arange(num)

for i in matrix_num:
	# 只对上三角矩阵进行判断概率是否应该连线
	del_list=np.arange(i+1)
	matrix_num_del_i=np.delete(matrix_num,del_list)
	for j in matrix_num_del_i:
		if(p>=random.random()):
			ER_matrix[i][j]=1

# 翻转上三角矩阵至下三角，形成对称矩阵
ER_matrix+=ER_matrix.T-np.diag(ER_matrix.diagonal())
print(ER_matrix)






