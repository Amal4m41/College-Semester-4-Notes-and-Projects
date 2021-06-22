import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv(".\\datasets\\Grade_Set_1.csv")
# print(df.columns)  #Index(['Hours_Studied', 'Test_Grade'], dtype='object')

#Simple scatter plot
df.plot(kind='scatter',x='Hours_Studied',y='Test_Grade',title='Hours Studied vs Test Grade')
plt.show()
