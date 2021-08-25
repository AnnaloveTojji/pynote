#import the python request library to query a website
import requests

#specify the url we want to scrape from
Link = "https://en.wikipedia.org/wiki/Forbes_list_of_Indian_billionaires"

#convert the web page to text
Link_text = requests.get(Link).text
print(Link_text)

#import BautifulSoup library to pull data out of HTML and XML files
from bs4 import BeautifulSoup

#to convert Link_text into a BeautifulSoup Object
soup = BeautifulSoup(Link_text, 'lxml')
print(soup)

#To take a look at the title of the web page
print(soup.title)

#Only the string not the tags
print(soup.title.string)

#First <a></a> tag
soup.a
#all the <a> </a> tags
soup.find_all('a')
#Fetch all the table tags
all_table = soup.find_all('table')
print(all_table)

#fetch all the table tags with class name="wikitable sortable"
our_table = soup.find('table', class_= 'wikitable sortable')
print(our_table)

#In the table that we will fetch find the <a> </a>tags  
table_links = our_table.find_all('a')
print(table_links)

#put the title into a list 
billionaires = []
for links in table_links:
    billionaires.append(links.get('title'))
print(billionaires)

#Convert the list into a dataframe 
import pandas as pd
df = pd.DataFrame(billionaires)
print(df)