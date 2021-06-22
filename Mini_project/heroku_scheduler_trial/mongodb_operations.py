import pymongo
from pymongo import MongoClient

cluster=MongoClient('mongodb+srv://project_mongo:sonicdash123@trial.qlxv5.mongodb.net/<dbname>?retryWrites=true&w=majority')  #Connecting the cluster
db=cluster['Demo_DB']     #Specifying which DB
collection=db['User_project']     #Specifying which collection in the DB


def insert_many_record(): #To insert many record at once
#   post1={'_id':110,'name':'Ronaldo','team':'Juventus'}
  post2={'name':'Neymar','team':'PSG'}
#   collection.insert_many([post1,post2])      #passing a list of posts/records
  collection.insert_many([post2])      #passing a list of posts/records



insert_many_record()