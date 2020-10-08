import re
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

#regex expression for html tags
clean = re.compile('<.*?>')

#Function to strip html tags from text
def strip_html(list):
	newList = []
	for i in list:
		no_tags = clean.sub('', str(i))
		newList.append(no_tags)
	return newList

# get the data
data = requests.get('https://civilization.fandom.com/wiki/List_of_pantheons_in_Civ6')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

#Extract table from html
list_of_pantheon = soup.find('table', { 'class': 'article-table sortable' })
#Extract each leader row from table
pantheon = list_of_pantheon.find_all('tr')[1:]
header = list_of_pantheon.find_all('tr')[0]
#----------------------------------------------------------------------------------------
#Name
name = []
for tr in pantheon:
	name.append(tr.find_all('a')[1])

#Strip html tags
name = strip_html(name)
#----------------------------------------------------------------------------------------
#Description
description = []
for tr in pantheon:
    description.append(tr.find_all('td'))

description = strip_html(description)
#----------------------------------------------------------------------------------------
#Icon
icon = []
for tr in pantheon:
    for td in tr.find_all("a")[0]:
        for image in td:
            icon.append(image.get("src"))
#----------------------------------------------------------------------------------------
@dataclass
class Pantheon:
    description : str
    icon : str

combined5 = {
    key : Pantheon(description, icon)
    for (key, description, icon) in zip(name, description, icon)
}

print(combined5.description)
