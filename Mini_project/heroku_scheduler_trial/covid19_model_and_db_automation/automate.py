import schedule
import time
from webscrape_and_mongodb import update_data_India,update_data_world
import wordwide_covid_model,india_covid_model

def job():
    print("I'm on")
    #first fetch the data and update the db
    update_data_world()
    update_data_India()

    #then train the model and get the results
    wordwide_covid_model.main()
    india_covid_model.main()

schedule.every().day.at("20:49").do(job)  #when the time in 24 hour format matches with the system time it does the specified job.

while(1):
    schedule.run_pending()
    time.sleep(1)
