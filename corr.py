from pandas import read_csv
import os
import matplotlib.pyplot as plt
import numpy as np
from pandas import set_option
from sklearn.preprocessing import Normalizer



os.chdir(".//Data")
data = read_csv('THU_U_day.txt')



# set_option('display.width', 2231)
# set_option('precision', 3) #POSITION
# correlation = data.corr(method= 'pearson')
print(data)
