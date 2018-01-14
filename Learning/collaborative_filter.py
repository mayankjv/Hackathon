import pandas as pd
import sys
import numpy as np
from measures import measures


def recommend(ind,row):
    print(data[ind][0])
    for i in range(1, row):
        if (int(data[ind][i]) >= 3 and int(data[1][i] == 0)):
            print(data[0][i])
data = pd.read_csv('train.csv')
#print(data)
data = data.replace(np.nan, 0)
try:
    col = len(data[0])
    row = len(list(data))
    k=measures()
    dis=k.pearsonCorrelation(data,1)
    print(dis)

except KeyError:
    print("keyError")
