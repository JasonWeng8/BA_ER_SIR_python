# -*- coding: utf-8 -*-
# @Author: wengjiacheng
# @Date:   2018-10-18 16:30:54
# @Last Modified by:   JasonWong97
# @Last Modified time: 2018-10-19 22:25:51
# encoding=utf-8
import random
import numpy as np
import matplotlib.pyplot as plt
from ER_wjc import ER_network
class BA_network(ER_network):
	def __init__(self,N,p,N_end,m0,title):
		super(ER_network, self).__init__()
		self.num=N
		self.p=p
		self.N = N_end# 当网络中存在 N 个节点后，停止。
		self.m=m0#从已存在的网络中选择 𝑚个节点
		self.title=title


# m=3#从已存在的网络中选择 𝑚个节点
# num=10#初始时网络有 num 个节点
# N=100# 当网络中存在 N 个节点后，停止。
# p=0.006#每对节点以概率 p 被选择，进行连边，不允许重复连边。
# # 初始化矩阵
# ER_matrix=np.zeros([num,num])
# matrix_num=np.arange(num)

# for i in matrix_num:
# 	# 只对上三角矩阵进行判断概率是否应该连线
# 	del_list=np.arange(i+1)
# 	matrix_num_del_i=np.delete(matrix_num,del_list)
# 	for j in matrix_num_del_i:
# 		if(p>=random.random()):
# 			ER_matrix[i][j]=1


# # 翻转上三角矩阵至下三角，形成对称矩阵
# ER_matrix+=ER_matrix.T-np.diag(ER_matrix.diagonal())
# print(ER_matrix)
# #构建好了网络
	def Create_BA_network(self,ER_matrix):
		while len(ER_matrix)<self.N:
			# 加入一个新节点，即增加一行一列
			old_len=len(ER_matrix)
			temp=np.zeros(old_len)
			column_added=np.column_stack((ER_matrix,temp))
			temp=np.zeros(old_len+1)
			new_matrix=np.row_stack((column_added,temp))

			# 选择与已存在的节点 i 进行连边的概率 𝑝_𝑖 与节点 i 的度成正比
			# pi（list）为每一个节点的度和总的度的比值，
			# 即每个已存在的点与新加入的节点连边的概率
			pi=ER_matrix.sum(axis=1)/ER_matrix.sum()
			pi_len=np.sum(pi!=0)

			# 这里有时候会报错，是因为pi中的非零项的个数小于m，
			# 比如说只有两个数有概率被抽到，没有办法抽取到m个数，所以报错
			# 如何ER_matrix.sum()全为0,则ER_matrix.sum()=nan，pi=nan，
			m=self.m
			if ER_matrix.sum()==0:
				picked_m_list=np.random.choice(old_len,size=m,replace=False)
				
			elif pi_len>=m:#存在被选中的概率的个数大于m
				picked_m_list=np.random.choice(old_len,size=m,replace=False,p=pi)

			else:#存在的概率的个数小于m，所以存在度的点必然被选中，
				# 再从概率为0的节点中 等概率选择m剩下的点
				# 
				# 从range(old_len)中以概率pi选出np.sum(pi!=0)个节点
				# 即存在概率（度）的点必然被选中
				picked_m_list=np.random.choice(old_len,size=np.sum(pi!=0),replace=False,p=pi)
				# 从range(old_len)，这些节点中删除选中的节点，
				# 再从剩下的节点中（概率为0，即度为0）等概率选中m-np.sum(pi!=0)个节点
				already_picked_m_list=np.delete(np.arange(old_len),picked_m_list)
				# print(already_picked_m_list)
				zero_picked_m_list=np.random.choice(already_picked_m_list,size=m-np.sum(pi!=0),replace=False)
				# print(zero_picked_m_list)
				# 合并存在度的节点的列表和从度为0中等概率选出的剩下的点的列表
				picked_m_list=np.hstack((picked_m_list,zero_picked_m_list))
				# print(picked_m_list)
			# print(picked_m_list)
			# 将选中的m个点与新加入的节点相连
			for m in picked_m_list:
				new_matrix[m,-1]=1
				new_matrix[-1,m]=1
			# 将新的网络赋给ER_matrix，从而进行下一个循环
			ER_matrix=new_matrix
		return ER_matrix


	def main(self):
		BA_matrix=self.Create_BA_network(self.Create_ER_network())
		ele_sum=self.element_sum(BA_matrix)
		self.plot_degree_map(ele_sum,self.title)
# print(ER_matrix)
# mat_degree=ER_matrix.sum(axis=1)
# ele_sum=element_sum(mat_degree)
# print(ele_sum)


# mat_degree_percent=[ key for key,value in ele_sum.items() ]
# mat_degree_percent1=[ value for key,value in ele_sum.items() ]
# mat_degree_percent2=np.array(mat_degree_percent1)/sum(mat_degree_percent1)
# print(mat_degree_percent)
# print(mat_degree_percent1)
# print(mat_degree_percent2)

# x = mat_degree_percent
# y = mat_degree_percent2
 
# plt.plot(x, y, marker='o', mec='r', mfc='w',label='Degree map')
# plt.legend()
# plt.xlabel("degree") #X轴标签
# plt.ylabel("P(degree)") #Y轴标签
# plt.title("BA network") #标题
# plt.show()

# # 加入一个新节点，即增加一行一列
# print(len(ER_matrix))
# temp=np.zeros(old_len)
# column_added=np.column_stack((ER_matrix,temp))
# print(column_added)
# print(len(ER_matrix))

# temp=np.zeros(11)
# new_matrix=np.row_stack((column_added,temp))
# print(new_matrix)


# # 选择与已存在的节点 i 进行连边的概率 𝑝_𝑖 与节点 i 的度成正比
# # pi（list）为每一个节点的度和总的度的比值，
# # 即每个已存在的点与新加入的节点连边的概率
# print(ER_matrix.sum())
# print(ER_matrix.sum(axis=1))
# pi=ER_matrix.sum(axis=1)/ER_matrix.sum()


# print(list(pi))
# # 这里有时候会报错，是因为pi中的非零项的个数小于m，
# # 比如说只有两个数有概率被抽到，没有办法抽取到m个数，所以报错
# # 如何ER_matrix.sum()全为0,则ER_matrix.sum()=nan，pi=nan，
# print("pi（list）为每一个节点的度和总的度的比值，")
# print(ER_matrix.sum()==0)
# print(np.sum(pi!=0))
# print(np.sum(pi!=np.nan))
# print(old_len-np.sum(pi==0))
# pi_len=np.sum(pi!=0)


# if ER_matrix.sum()==0:
# 	picked_m_list=np.random.choice(old_len,size=m,replace=False)
# elif pi_len>=m:#存在被选中的概率的个数大于m
# 	picked_m_list=np.random.choice(old_len,size=m,replace=False,p=pi)
# else:#存在的概率的个数小于m，所以存在度的点必然被选中，
# 	# 再从概率为0的节点中 等概率选择m剩下的点
# 	picked_m_list=np.random.choice(old_len,size=np.sum(pi!=0),replace=False,p=pi)
# 	already_picked_m_list=np.delete(np.arange(old_len),picked_m_list)
# 	print(already_picked_m_list)
# 	zero_picked_m_list=np.random.choice(already_picked_m_list,size=m-np.sum(pi!=0),replace=False)
# 	print(zero_picked_m_list)
# 	picked_m_list=np.hstack((picked_m_list,zero_picked_m_list))
# 	print(picked_m_list)
# print(picked_m_list)
# for m in picked_m_list:
# 	new_matrix[m,-1]=1
# 	new_matrix[-1,m]=1

# print(new_matrix)








