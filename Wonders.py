#Finding results from webpage containing a table
import re
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

#regex expression for html tags
clean = re.compile('<.*?>')

#Function to strip html tags from text
def strip_html(*list):
	newList = []
	for i in list:
		no_tags = clean.sub('', str(i))
		newList.append(no_tags)
	return newList

# get the data
data = requests.get('https://civilization.fandom.com/wiki/List_of_natural_wonders_in_Civ6')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

#Extract table from html
list_of_wonders = soup.find('table', { 'class': 'article-table sortable' })
#Extract each leader row from table
wonder = list_of_wonders.find_all('tr')
#-----------------------------------------------------------------------------------
#Wonder Name
name = []
wonder.pop(0)
for tr in wonder:
	for td in tr:
		name.append(tr.find_all('a')[1])

#Strip html tags
name = strip_html(name)
#Remove duplicates
name = list(dict.fromkeys(name))
#------------------------------------------------------------------------------------
#description/size
wonder_info_text = []
for td in wonder:
	wonder_info_text.append(td.find_all('td'))

description = [i[-2] for i in wonder_info_text]
size = [i[-1] for i in wonder_info_text]

#Strip html tags
description = strip_html(description)
size = strip_html(size)

#------------------------------------------------------------------------------------
# Wonder Icon
wonder_icon = []
for tr in wonder:
	for td in tr.find_all("a")[0]:
		for image in td:
			wonder_icon.append(image.get('src'))

#------------------------------------------------------------------------------------
#Combine Lists
@dataclass
class NaturalWonder:
	description : str
	size : str
	wonder_icon : str

combined2 = {
	key : NaturalWonder(description, size, wonder_icon)
	for (key, description, size, wonder_icon) in zip (name, description, size, wonder_icon)
}

# # #Show results - Testing only
# user_input = input("Enter wonder name: ")
# print("\nDescription: \n", combined2[user_input].description)
# print("\nSize: \n", combined2[user_input].size)

#------------------------------------------------------------------------------------
