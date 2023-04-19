import os
import pandas as pd

root_path = os.getcwd()

data_1 = pd.read_csv(root_path + '/learning/data.csv')
data_2 = pd.read_csv(root_path + '/learning/Resume.csv')
data_3 = pd.read_json(root_path + '/learning/data_3.json')

print(data_1.head())

print(data_2.head())

print(data_3.head())