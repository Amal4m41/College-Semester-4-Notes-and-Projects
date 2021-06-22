import csv
import datetime,random as r

def create_csv():
    with open(f'DataCollection\\{name}','w',newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Date','Country1','Country2','Country3'])


def add_rows():
    with open(f'DataCollection\\{name}','a',newline='') as file:     #mode is append
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        count=0
        while(count!=5):
            x=datetime.datetime(2020,5,count+1)
            writer.writerow([str(x).split()[0],r.randint(23113,35423),r.randint(254522,334423),r.randint(23113,35423)])
            count+=1


def print_csv():
    with open(f'DataCollection\\{name}') as f:
        data=csv.reader(f)
        for row in data:
            print(row)


name='dummy_file.csv'
# create_csv()
add_rows()
print_csv()
