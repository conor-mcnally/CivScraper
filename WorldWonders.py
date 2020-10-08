#Finding results from webpage containing a table
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
data = requests.get('https://civilization.fandom.com/wiki/List_of_wonders_in_Civ6')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

#Extract table from html
list_of_world_wonders = soup.find('table', { 'class': 'article-table sortable' })
#Extract each leader row from table
wonder = list_of_world_wonders.find_all('tr')[1:]
header = list_of_world_wonders.find_all('tr')[0]
#-----------------------------------------------------------------------------------
#Wonder Name
name = []
for tr in wonder:
	name.append(tr.find_all('a')[1])

#Strip html tags
name = strip_html(name)
#------------------------------------------------------------------------------------
# Wonder Icon
world_wonder_icon = []
for tr in wonder:
	for td in tr.find_all("a")[0]:
		for image in td:
			world_wonder_icon.append(image.get('src'))

#------------------------------------------------------------------------------------
era = []
requirements = []
production = []
bonus = []
placement = []
for tr in wonder:
    era.append(tr.find_all('td')[1])
    requirements.append(tr.find_all('td')[2])
    production.append(tr.find_all('td')[3])
    bonus.append(tr.find_all('td')[4])
    placement.append(tr.find_all('td')[5])

# era = list(dict.fromkeys(era))
era = strip_html(era)
requirements = strip_html(requirements)
production = strip_html(production)
bonus = strip_html(bonus)
placement = strip_html(placement)


#------------------------------------------------------------------------------------
@dataclass
class WorldWonder:
	era : str
	requirements : str
	production : str
	bonus: str
	placement : str
	world_wonder_icon : str

combined4 = {
	key : WorldWonder(era, requirements, production, bonus, placement, world_wonder_icon)
	for (key, era, requirements, production, bonus, placement, world_wonder_icon) in zip (name, era, requirements, production, bonus, placement, world_wonder_icon)
}

print(requirements, end = " ")
