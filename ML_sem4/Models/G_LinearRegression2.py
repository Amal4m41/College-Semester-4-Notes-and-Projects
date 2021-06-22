import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np 

df=pd.read_csv("datasets\\Grade_Set_1.csv")

model=linear_model.LinearRegression()

X=[df['Hours_Studied']]
y=[df['Test_Grade']]
# z=[df['Test_Grade']+5]
# print(y,z)

model.fit(X,y)
# print(model.predict(X))
plt.scatter(X,y,color='black')
# plt.scatter(X,z,color='blue')
plt.plot(X,model.predict(X),color='blue',linewidth=3)
plt.title('Hours studied vs Test score')
plt.xlabel('Hours studied')
plt.ylabel('Test score')

plt.show()
