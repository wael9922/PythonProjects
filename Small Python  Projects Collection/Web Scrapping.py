"""
 Web Scrapping For the 100 largest companies by revenue in 2025
 from Wikipedia page
 URL: https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd 
url = r"https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url) #return response object
soup = BeautifulSoup(page.text,'html.parser')

table = soup.find_all('table')[0]
# print(table)
headers = table.find_all('th')
headers_name =[]
for i in headers:
    headers_name.append(i.text.strip())
# print(headers_name)
df = pd.DataFrame(columns=headers_name)
# print(df)
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_raw_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_raw_data
print(df)
df.to_csv(r'D:\scraping output\companies2.csv',index=False)