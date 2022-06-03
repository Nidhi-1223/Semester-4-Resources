# importing libraries
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv('/home/hp1/Documents/College/Semester 4/Data Mining And Business Visualization/dataset-main/Market_Basket_Optimisation.csv')

transacts = []
for i in range(0,7501):
    transacts.append([str(Data.values[i,j]) for j in range(0,20)])