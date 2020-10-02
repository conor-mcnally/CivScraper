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
data = requests.get('https://civilization.fandom.com/wiki/List_of_city-states_in_Civ6')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

#Extract table from html
list_of_cs = soup.find('table', { 'class': 'article-table sortable' })
#Extract each leader row from table
cs = list_of_cs.find_all('tr')
#-----------------------------------------------------------------------------------
#Wonder Name
name = []
cs.pop(0)
for tr in cs:
	for td in tr:
		name.append(tr.find_all('a')[1])

#Strip html tags
name = strip_html(name)
#Remove duplicates
name = list(dict.fromkeys(name))

#------------------------------------------------------------------------------------
# Wonder Icon
cs_icon = []
for tr in cs:
	for td in tr.find_all("a")[0]:
		for image in td:
			cs_icon.append(image.get('src'))

cs_icon.insert(0, 'https://vignette.wikia.nocookie.net/civilization/images/7/78/Akkad_%28Civ6%29.png/revision/latest/scale-to-width-down/32?cb=20190419023616')

#------------------------------------------------------------------------------------

#Suzerian Bonus
cs_bonus = []
for td in cs:
	cs_bonus.append(td.find_all('td'))

cs_bonus = [i[-1] if len(i) > 2 else i[0] for i in cs_bonus]

#Strip html tags
cs_bonus = strip_html(cs_bonus)
#------------------------------------------------------------------------------------
#Combine Lists
@dataclass
class CityState:
	cs_icon : str
	cs_bonus : str

combined3 = {
	key : CityState(cs_icon, cs_bonus)
	for (key, cs_icon, cs_bonus) in zip (name, cs_icon, cs_bonus)
}

# # #Show results - Testing only
user_input = input("Enter cs name: ")
print("\nSuz Bonus: \n", combined3[user_input].cs_bonus)
