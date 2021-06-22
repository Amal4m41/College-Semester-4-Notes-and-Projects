#!/usr/bin/env python
# coding: utf-8

# # Topic : Letter Recognition Classification using SVM

# ## Data Set Information:
# 
# The objective is to identify each of a large number of black-and-white rectangular pixel displays as one of the 26 capital letters in the English alphabet. The character images were based on 20 different fonts and each letter within these 20 fonts was randomly distorted to produce a file of 20,000 unique stimuli. Each stimulus was converted into 16 primitive numerical attributes (statistical moments and edge counts) which were then scaled to fit into a range of integer values from 0 through 15.
# 
# 
# **Attribute Information**
# 
# 1. Capital letter (26 values from A to Z)
# 2. x-box horizontal position of box (integer)
# 3. y-box vertical position of box (integer)
# 4. width width of box (integer)
# 5. high height of box (integer)
# 6. onpix total # on pixels (integer)
# 7. x-bar mean x of on pixels in box (integer)
# 8. y-bar mean y of on pixels in box (integer)
# 9. x2bar mean x variance (integer)
# 10. y2bar mean y variance (integer)
# 11. xybar mean x y correlation (integer)
# 12. x2ybr mean of x * x * y (integer)
# 13. xy2br mean of x * y * y (integer)
# 14. x-ege mean edge count left to right (integer)
# 15. xegvy correlation of x-ege with y (integer)
# 16. y-ege mean edge count bottom to top (integer)
# 17. yegvx correlation of y-ege with x (integer)
# 
# 

# In[1]:


#Importing the necessary libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


# In[2]:


#Load the dataset
df = pd.read_csv('.\\letter-recognition.data',header=None)
df.head()


# In[3]:


print("Dataset size : ",df.shape)  #20,000 records and (16 features+target value) i.e 20,000 x 17


# In[4]:


df.describe()


# In[5]:


#To check the datatype of the features and if there's any null values for the features.
df.info()  


# In[6]:


df[0].value_counts()     #Dataset is not that biased(i.e we have approx equal frequency of data w.r.t the target values)


# In[7]:


plt.figure(figsize = (18,18))

#Checking the relationship trend between the feature values w.r.t their correlation
sn.heatmap(df.corr(),annot=True,cmap='RdYlGn')


# In[8]:


#Just verifying the null values.(a different way to check if there's any null value for the feature)
df.isna().sum()  


# ### Preparing the dataset for train and test

# In[9]:



#Splitting the dataset(taking 20% of the data as test data)
from sklearn.model_selection import train_test_split
train_X,test_X,train_y,test_y=train_test_split(df.iloc[:,1:],df.iloc[:,0],test_size=0.2,random_state=5)

print('Train dataset size = ',train_X.shape)
print('Test dataset size = ',test_X.shape)


# In[10]:


print("Train Features :\n",train_X.head())
print("Train target values :\n",train_y.head())


# ### Creating the SVM model
# 
# * A hyperplane is a plane in nD that tries to separate out different classification groups.
# * Support vector machine draws a hyper plane in nD space such that it maximizes margin between classification groups

# In[11]:


#import the svm model
from sklearn.svm import SVC
model=SVC(kernel='linear')

#train the model with the train dataset
model.fit(train_X,train_y)

#predict the target values using the test dataset feature values
predicted=model.predict(test_X)

#check the accuracy
print("Accuracy :",model.score(test_X,test_y))


# In[12]:


#Creating a dataframe of true and predicted target values for the test dataset 

result=test_X
result['True letter']=test_y
result['Predicted letter']=predicted
result.head()


# In[13]:


#Printing the details of misclassified data

result[result['Predicted letter'] !=result['True letter']].head(15)


# ### Plotting confusion matrix

# In[14]:


#Getting the list of target values to plot confusion matrix
letter_target_values=df[0].unique()
print(letter_target_values)


# In[15]:


#Let's see the confussion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(test_y,predicted)
# print(cm)


# In[16]:


#printing the confusion matrix after converting it into dataframe(to know the classes)
cmDF=pd.DataFrame(cm,columns=letter_target_values,index=letter_target_values)  
# print(cmDF)


# In[17]:


#Gives a visual representation of the confusion matrix
plt.figure(figsize = (26,26))
sn.heatmap(cmDF,annot=True,cmap='RdYlGn')   
plt.xlabel('Predicted lablel/class')
plt.ylabel('True label/class')
plt.show()


# In[ ]:





# # THE END
