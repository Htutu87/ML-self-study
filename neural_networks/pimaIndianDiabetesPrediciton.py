# The Pima Indian Diabetes Prediciton
# Description: Based on a dataset of 8 different health features of the Pima Indian population individuals, this code aims to predict if new inputs of Pima Indians Health data indicates that they have diabetes, withou explicitly knowing the answer.
# Author: Artur Amaral
# Initial Date: 20/03/2021 

import os
import numpy as np

#-------------------------------------------
# Loading the text database and converting it into 
# a numpy matrix
#-------------------------------------------

os.chdir('../data')
pimaCSV = np.loadtxt('diabetes.csv',delimiter=',')
np.shape(pimaCSV)
print(np.matrix(pimaCSV))
