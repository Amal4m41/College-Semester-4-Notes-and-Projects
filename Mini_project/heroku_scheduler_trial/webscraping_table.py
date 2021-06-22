from bs4 import BeautifulSoup
import requests,pandas as pd

url='https://www.worldometers.info/coronavirus/'
r=requests.get(url)
# print(r.status_code)  #200 therefore success

# print(r.text)  #contents of the response in unicode

# soup=BeautifulSoup(r.text,'html.parser')
soup=BeautifulSoup(r.text,'lxml')

# print(soup)
table=soup.find('table',id='main_table_countries_today')
# table=soup.find_all('table    ')
# table=soup.find('tbody',class_='total_row_body body_world')
# print(table)

# df=pd.DataFrame(table)
# print(df)


# </tbody>
# <tbody class="total_row_body body_world">
# <tr class="total_row">
# <td></td>
# <td><strong>Total:</strong></td>
# <td>123,903,665</td>
# <td style="background-color:#FFEEAA; color:#000;">+52,380</td>
# <td>2,728,644</td>
# <td style="background-color:red; color:#fff">+1,126</td>
# <td>99,821,265</td>
# <td style="background-color:#c8e6c9; color:#000">+33,930</td>
# <td>21,353,756</td>
# <td>90,199</td>
# <td>15,895.7</td>
# <td>350.1</td>
# <td></td>
# <td></td>





# table_rows=table.find_all('tr')
# for i  in table_rows:
#     td=i.find_all('td')
#     [print(i.text) for i in td]
#     print('---------------------------------------------')
# # print(type(table_rows))






df = pd.read_html(str(table))

print(table)