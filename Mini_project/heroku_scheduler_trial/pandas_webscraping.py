import pandas as pd
import pymongo
from pymongo import MongoClient


cluster =MongoClient("mongodb+srv://project_mongo:sonicdash123@trial.qlxv5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster['WebApp_trial']     #Specifying which DB
collection_worldwide=db['Worldwide_data']     #Specifying which collection in the DB
collection_india=db['India_data']     #Specifying which collection in the DB


#URL to scrap data from
# url='https://www.worldometers.info/coronavirus/'
url='https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen'


dfs=pd.read_html(url)   #extracting the table data from the url
df=dfs[0]  #accessing the first table(the only table as of now)


def data_world():
    world_data=df[df['Location']=="Worldwide"][['Total cases','Deaths']]
    print(world_data)
    row={'Total_cases':int(world_data.iloc[0,0]),'Deaths':int(world_data.iloc[0,1])}
    collection_worldwide.insert_one(row)      #passing a list of posts/records



def data_India():
    india_data=df[df['Location']=="India"][['Total cases','Deaths']]
    print(india_data)
    row={'Total_cases':int(india_data.iloc[0,0]),'Deaths':int(india_data.iloc[0,1])}
    collection_india.insert_one(row)      #passing a list of posts/records
    


if __name__=="__main__":
    data_world()
    data_India()




