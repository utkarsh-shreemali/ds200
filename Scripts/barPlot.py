import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("riceProduction.csv")
df2=df[['State','Production of Rice - Average Production (2010-11 to 2014-15)']]
l=list(df['State'])
l=l[:-1]
#print(len(l))
m=list(df['Production of Rice - Average Production (2010-11 to 2014-15)'])
m=m[:-1]
m=[int(i) for i in m]
n=[i for i in range(1,len(m)+1)]
#print(n)

plt.bar(n,m,align="center")

#specify labels on xticks
plt.xticks(n,l,rotation='vertical')

plt.xlabel("States")
plt.ylabel("Average Production of Rice (2010-11 to 2014-15)")

plt.legend()
plt.show()

