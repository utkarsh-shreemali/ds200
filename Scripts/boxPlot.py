import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("riceProduction.csv")
pl=df[['State','Production of Rice - Average Production (2010-11 to 2014-15)']]

'''
l=list(df['State'])
l=l[:-1]
#print(len(l))
m=list(df['Production of Rice - Average Production (2010-11 to 2014-15)'])
m=m[:-1]
k=[]

n=[i for i in range(0,len(m))]
#print(n)
k.append(m)
k.append(l)
'''

pl.boxplot()
plt.ylim(0, 15000)



plt.legend()
plt.show()

