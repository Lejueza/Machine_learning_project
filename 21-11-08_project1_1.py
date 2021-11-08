"""
title : 21-11-08_project1_0.py
authors : BOUCHARD Ignace ; LEJUEZ Anthony ;
date : 08/11/2021
"""

"""
Importations
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from random import random, seed

import sklearn as skl

"""
Franke's function
"""

def franke_fct(x,y) :
	
	terme_1 = (3/4)*np.exp(-((9*x - 2)**2)/4 -((9*y - 2)**2)/4)
	terme_2 = (3/4)*np.exp(-((9*x +1)**2)/49 -((9*y + 1))/10)
	terme_3 = (1/2)*np.exp(-((9*x -7)**2)/4 -((9*y - 3))/4)
	terme_4 = (1/5)*np.exp(-((9*x -4)**2) -((9*y - 7)**2))
	
	f = terme_1 + terme_2 + terme_3 - terme_4
	
	return f

"""
tests
"""
x,y = 0.5,0.5
test = franke_fct(x,y)
print(test)