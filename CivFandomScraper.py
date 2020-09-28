#Finding results from webpage containing a table
import re
import requests
from bs4 import BeautifulSoup

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
data = requests.get('https://civilization.fandom.com/wiki/Leaders_(Civ6)')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

#Extract table from html
list_of_leaders = soup.find('table', { 'class': 'wikitable sortable' })
#Extract each leader row from table
leader = list_of_leaders.find_all('tr')
#Remove first row containing table headings
leader.pop(0)

#-----------------------------------------------------------------------------------
#leader ability/agenda titles
leader_info_titles = []
for td in leader:
	leader_info_titles.append(td.find_all('b'))

#Save all agenda/ability titles to lists
ability_title = [i[0] for i in leader_info_titles] #Seperate ability to seperate list
agenda_title = [i[1] for i in leader_info_titles]  #Seperate agenda to seperate list

#Strip html tags
ability_title = strip_html(ability_title)
agenda_title = strip_html(agenda_title)

#Show results
print("Ability Title: \n", ability_title[1], "\nAgenda Title: \n", agenda_title[1])
#------------------------------------------------------------------------------------
#leader ability/agenda text
leader_info_text = []
for td in leader:
	leader_info_text.append(td.find_all('p'))

#Save all agenda/ability text to lists
ability_text = [i[0] for i in leader_info_text] #Seperate ability to seperate list
agenda_text = [i[1] for i in leader_info_text]  #Seperate agenda to seperate list

#Strip html tags
ability_text = strip_html(ability_text)
agenda_text = strip_html(agenda_text)

#Show results
print("\nAbility Text: \n", ability_text[1], "\nAgenda Text: \n", agenda_text[1])
#------------------------------------------------------------------------------------
#Leader Name
name = []
for tr in leader:
	for td in tr:
		name.append(tr.find_all('a')[1])

#Strip html tags
name = strip_html(name)

#Remove duplicates
name = list(dict.fromkeys(name))

print("Leader Name: \n", name[0:10])

#------------------------------------------------------------------------------------
#Leader Icon
# leader_icon = []
# for tr in leader:
# 	for image in tr:
# 		leader_icon.append(image.find_all('img')['src'])
# print(len(leader_icon))

#------------------------------------------------------------------------------------
#Combine Agenda/Ability titles and text
agenda_dict = dict(zip(agenda_title, agenda_text))
#print(agenda_dict)

ability_dict = dict(zip(ability_title, ability_text))
#print(ability_dict)

#------------------------------------------------------------------------------------
#Final - Have Seperate lists to be used in embed
