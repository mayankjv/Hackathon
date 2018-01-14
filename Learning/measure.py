import numpy as np
import pandas as pd
import import sys
from multimethod import multimethod

class measure:

    def __init__(self):
        self.p=10

    def getRow(self,data):
        return len(list(data))

    def getColoumn(self,data):
        return len(data[0])

    @multimethod(object,pandas.core.frame.DataFrame,int)
    def pearsonCorrelation(self,data,user):
        row = self.getRow(data)
        col = self.getColoumn(data)
        val=-1
        for j in range(2,col):
            p1 = 0
            count = 0
            p2 = 0
            p3 = 0
            p5 = 0
            p6 = 0
            for i in range(1,row):
                if j==user:
                    continue
                if (int(data[user][i]) == 0 or int(data[j][i]) == 0):
                    continue
                p1=p1+int(data[user][i])*int(data[j][i])
                count=count+1
                p2=int(p2+int(data[user][i]))
                p3=int(p3+int(data[j][i]))
                p5 = int(p5 + int(data[user][i]) * int(data[user][i]))
                p6 = int(p6 + int(data[j][i]) * int(data[j][i]))
            if count>0:
                p4=p2*p3/count
                p1=p1-p4
                p2=p2*p2/count
                p3=p3*p3/count
                k1=np.sqrt(p5-p2)
                k2=np.sqrt(p6-p3)
                r=p1/(k1*k2)
                if r>val:
                    val=r
                    indexSimilar=j
                print(r, j)
        return indexSimilar

    @multimethod(object,pandas.core.frame.DataFrame,int,int)
    def pearsonCorrelation(self,data,user1,user2):
        row = self.getRow(data)
        p1 = 0
        count = 0
        p2 = 0
        p3 = 0
        p5 = 0
        p6 = 0
        for i in range(1,row):
            if (int(data[user1][i]) == 0 or int(data[user2][i]) == 0):
                continue
            p1=p1+int(data[user1][i])*int(data[user2][i])
            count=count+1
            p2=int(p2+int(data[user1][i]))
            p3=int(p3+int(data[user2][i]))
            p5 = int(p5 + int(data[user1][i]) * int(data[user1][i]))
            p6 = int(p6 + int(data[user2][i]) * int(data[user2][i]))
        if count>0:
            p4=p2*p3/count
            p1=p1-p4
            p2=p2*p2/count
            p3=p3*p3/count
            k1=np.sqrt(p5-p2)
            k2=np.sqrt(p6-p3)
            r=p1/(k1*k2)
        return  r

        return indexSimilar






