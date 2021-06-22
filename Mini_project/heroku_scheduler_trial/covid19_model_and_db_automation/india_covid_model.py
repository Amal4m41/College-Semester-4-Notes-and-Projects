def main():
    #!/usr/bin/env python
    # coding: utf-8

    # In[2]:


    import pymongo
    from pymongo import MongoClient
    from bson.objectid import ObjectId


    # In[3]:


    import pandas as pd


    # In[4]:


    #Connecting to the cluster
    cluster =MongoClient("mongodb+srv://project_mongo:sonicdash123@trial.qlxv5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


    # In[5]:


    db=cluster['WebApp_trial']     #Specifying which DB
    collection_india=db['India_data']     #Specifying which collection in the DB


    # In[6]:


    data=pd.DataFrame(list(collection_india.find()))


    # In[7]:


    data


    # In[9]:


    #coverting the object id to date object
    date_lst=[ObjectId(i).generation_time.date() for i in data['_id']]


    # In[11]:


    date_df=pd.DataFrame(date_lst,columns=['Date'])


    # In[12]:


    date_df


    # In[13]:


    new_df=pd.merge(date_df,data,left_index=True,right_index=True).drop(['_id'],axis=1)


    # In[14]:


    new_df


    # In[15]:


    print(new_df)


    # In[ ]:



if __name__=="__main__":
    main()

