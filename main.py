# -*- coding: utf-8 -*-
# @Author: JasonWong97
# @Date:   2018-10-19 21:37:31
# @Last Modified by:   JasonWong97
# @Last Modified time: 2018-10-19 22:27:20

from ER_wjc import ER_network as ER
from BA_wjc import BA_network as BA

er_network=ER(N=1000,p=0.006,title="ER network")
er_network.main()
# ER_matrix=er_network.Create_ER_network()
# ele_sum=er_network.element_sum(ER_matrix)
# er_network.plot_degree_map(ele_sum,"ER network")

ba_network=BA(N=3,p=0.006,N_end=1000,m0=3,title="BA network")
ba_network.main()
# BA_matrix=ba_network.Create_BA_network(ba_network.Create_ER_network())
# ele_sum=ba_network.element_sum(BA_matrix)
# ba_network.plot_degree_map(ele_sum,"BA network")