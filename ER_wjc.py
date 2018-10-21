# -*- coding: utf-8 -*-
# @Author: wengjiacheng
# @Date:   2018-10-18 16:30:54
# @Last Modified by:   JasonWong97
# @Last Modified time: 2018-10-21 19:38:01
import random
import numpy as np
import matplotlib.pyplot as plt
class ER_network:
	def __init__(self, N,p,title):
		self.num=N#初始时网络有 N 个节点
		self.p=p#每对节点以概率 p 被选择，进行连边，不允许重复连边。
		self.title=title

	def Create_ER_network(self):
		# 初始化矩阵	
		ER_matrix=np.zeros([self.num,self.num])
		matrix_num=np.arange(self.num)

		for i in matrix_num:
			# 只对上三角矩阵进行判断概率是否应该连线
			del_list=np.arange(i+1)
			matrix_num_del_i=np.delete(matrix_num,del_list)
			for j in matrix_num_del_i:
				if(self.p>=random.random()):
					ER_matrix[i][j]=1

		# 翻转上三角矩阵至下三角，形成对称矩阵
		ER_matrix+=ER_matrix.T-np.diag(ER_matrix.diagonal())
		return ER_matrix
		# print(ER_matrix)


	def element_sum(self,mat):
	# 统计数组中所有元素出现的次数 ,返回字典形式
		y = mat.sum(axis=1)
		y = np.array(y)
		key = np.unique(y)
		result = {}
		for k in key:
		    mask = (y == k)
		    y_new = y[mask]
		    v = y_new.size
		    result[k] = v
		return result
		
	def plot_degree_map(self,ele_sum,title):
		mat_degree_percent=[ key for key,value in ele_sum.items() ]
		mat_degree_percent1=[ value for key,value in ele_sum.items() ]
		mat_degree_percent2=\
			np.array(mat_degree_percent1)/sum(mat_degree_percent1)

		x = mat_degree_percent
		y = mat_degree_percent2
		 
		plt.plot(x, y, marker='o', mec='r', mfc='w',label='Degree map')
		plt.legend()
		plt.xlabel("degree") #X轴标签
		plt.ylabel("P(degree)") #Y轴标签
		plt.title(title) #标题
		plt.show()

	def main(self):
		ER_matrix=self.Create_ER_network()
		ele_sum=self.element_sum(ER_matrix)
		self.plot_degree_map(ele_sum,self.title)




