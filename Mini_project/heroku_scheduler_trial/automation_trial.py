import schedule
import time
from ml_mongo_trial import main

def do_nothing():
    print("this is automation trial")
    main()

schedule.every(10).seconds.do(do_nothing)

while(1):
    schedule.run_pending()
    time.sleep(1)
