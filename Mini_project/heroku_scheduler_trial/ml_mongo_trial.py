def main():
    #!/usr/bin/env python
    # coding: utf-8

    # In[29]:


    import pymongo
    from pymongo import MongoClient


    # In[30]:


    import pandas as pd


    # In[31]:


    #Connecting to the cluster
    cluster =MongoClient("mongodb+srv://project_mongo:sonicdash123@trial.qlxv5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


    # In[32]:


    db=cluster['Demo_DB']     #Specifying which DB
    collection=db['User_project']     #Specifying which collection in the DB


    # In[33]:


    # results=collection.find()


    # In[34]:


    # list(collection.find())


    # In[35]:


    # for i in results:
    #     print(i)


    # In[36]:


    data=pd.DataFrame(list(collection.find()))


    # In[37]:


    # data


    # In[38]:


    data.to_pickle("./dummy.pkl")


    # In[39]:


    unpickled_df = pd.read_pickle("./dummy.pkl")
    print(unpickled_df)


    # In[40]:


    import os
    os.remove("./dummy.pkl")


    # In[ ]:




if(__name__=="__main__"):
    main()