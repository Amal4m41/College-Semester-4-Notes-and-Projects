# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import requests
from rasa_sdk.events import AllSlotsReset

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ValidateLocationForm(Action):   #form for fetching country name

    def name(self) -> Text:
        return "location_details_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:

        # required_slots=['country','state']
        required_slots=['country']

        
        # while(tracker.slots.get('country') is None):
        #     #If this slot is not filled yet, ask the user to fill this slot next
        #     return [SlotSet("requested_slot",'country')] 

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                #If this slot is not filled yet, ask the user to fill this slot next
                return [SlotSet("requested_slot",slot_name)] 

        return [SlotSet("requested_slot",None)]   #all slots are filled

class ValidateLocationFormIndia(Action):       #form for fetching state name for India

    def name(self) -> Text:
        return "location_details_form_india"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:

        required_slots=['state']

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                #If this slot is not filled yet, ask the user to fill this slot next
                return [SlotSet("requested_slot",slot_name)] 

        return [SlotSet("requested_slot",None)]   #all slots are filled


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_form_submit"
        
    def run(self, dispatcher, tracker: Tracker, domain:"DomainDict",) -> List[Dict[Text,Any]]:
        # dispatcher.utter_message(template="utter_form_return",Country=tracker.get_slot("country"),State=tracker.get_slot("state"))
        msg=''
        country=tracker.get_slot('country')
          #to prevent the program from crashing due to error caused while fetching data from api(eg: api fields not found)
        if(country):  #if a country is present then do these stuffs(cuz India is treated separatley)
            country=country.lower().strip()
            if(country in ['america','united states of america','united states','us','usa']):
                country='USA'
            elif(country in ['united kingdom','uk']):
                country='UK'    
            elif(country in ['united arab emirates','uae']):
                country='UAE'
            else:
                country=country.title()
                country=country.replace(' And ',' and ')
                country=country.replace(' The ',' the ')
                country=country.replace(' Of ',' of ')

            response = requests.get("https://corona.lmao.ninja/v2/countries?yesterday&sort").json()
            for data in response:
                if(data['country']==country):
                    # print('hello  ',country)
                    lst=[(str(info)+' : '+(str(data[info]) if str(data[info])!='' else 'N/A')) for info in ['country','cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered', 'todayRecovered', 'active', 'critical','tests']]
                    msg='\n'.join(lst)    

            if(msg==''):
                msg='Please try again with proper spelling of country [OR] Data you have asked for is not available now'                            

        else: 
            #which means the country is india (country value will be None) 
            state=tracker.get_slot("state").lower().strip()
            state=state.title().replace(' And ',' and ')
            response = requests.get("https://api.covid19india.org/data.json").json()
            for data in response['statewise']:
                if(data['state']==state):
                    # print('hello  ',state)
                    lst=[(str(info)+' : '+(str(data[info]) if str(data[info])!='' else 'N/A')) for info in ['active','confirmed','deaths','recovered','lastupdatedtime','state','statenotes']]
                    msg='\n'.join(lst)


            if(msg==''):
                msg="Please try again with proper spelling for state [OR] Data you have asked for is not available now"        
    
            

        print(msg)    
        dispatcher.utter_message(text="this is the covid report for : \n"+msg)
        return [AllSlotsReset()]




# import requests

# # r=requests.get('https://www.mohfw.gov.in/data/datanew.json')  #for India and Indian states live covid data
# r=requests.get('https://corona.lmao.ninja/v2/jhucsse')   #for worldwide live data on covid
# # print(r.json())
# c=0
# for i in r.json():
#     if('India' == i['country']):
#       print(i['province'])
#       c+=1

# print(c)      
    

class AskForSlotAction(Action):
    def name(self) -> Text:
        return "action_ask_country"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(text="Please enter the country")
        return []