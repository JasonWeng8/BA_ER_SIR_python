# -*- coding: utf-8 -*-
# @Author: JasonWong97
# @Date:   2018-10-19 21:37:31
# @Last Modified by:   JasonWong97
# @Last Modified time: 2018-10-21 20:45:30

from ER_wjc import ER_network as ER
from BA_wjc import BA_network as BA
from SIR_wjc import SIR_model as SIR

er_network=ER(N=1000,p=0.006,title="ER network")
er_network.main()

ba_network=BA(N=3,p=0.006,N_end=1000,m0=3,title="BA network")
ba_network.main()

sir_model_er=SIR(beta=0.15,miu=0.1,t=100,
	network="ER_network",method="max_node")
sir_model_er.main()

sir_model_ba=SIR(beta=0.15,miu=0.1,t=100,
	network="BA_network",method="max_node")
sir_model_ba.main()

sir_model_er=SIR(beta=0.15,miu=0.1,t=100,
	network="ER_network",method="random_node")
sir_model_er.main()

sir_model_ba=SIR(beta=0.15,miu=0.1,t=100,
	network="BA_network",method="random_node")
sir_model_ba.main()




