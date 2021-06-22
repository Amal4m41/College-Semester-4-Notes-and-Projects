import pandas as pd, numpy as np, matplotlib.pyplot as plt 

data={
    'Gender':['F','M','N'],
    'EmpId':['E01','E02','E03'],
    'Age':[25,27,25]
}

#columns parameter can be used to filter/order the columns
df=pd.DataFrame(data,columns=['EmpId','Gender','Age'],index=[4,5,6])
print(df)
