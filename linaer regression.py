import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
df=pd.read_csv('homeprices.csv')
df
%matplotlib inline
plt.xlabel('area(sqr ft)')
plt.ylabel('price usd')
plt.scatter(df.area,df.price,color='red',marker='+')
reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
reg.coef_
reg.intercept_
d=pd.read_csv('areas.csv')
d
