import matplotlib.pyplot as plt 
import pandas as pd
'''
spatial_data = open('tripFile.txt', 'r').readlines()

print(type(spatial_data))

spatial_data = [line.split(',') for line in spatial_data]
'''
spatial_data = pd.read_csv('tripFile.txt', header=None)
print(spatial_data.head())


