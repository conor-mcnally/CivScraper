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
#print("Ability Title: \n", ability_title[1], "\nAgenda Title: \n", agenda_title[1])
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
#print("\nAbility Text: \n", ability_text[1], "\nAgenda Text: \n", agenda_text[1])
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

#print("Leader Name: \n", name[1], "\n")

#------------------------------------------------------------------------------------
# Leader Icon
#YESSSS ALL LEADER ICONS - YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#YOU DA MAN
leader_icon = []
for tr in leader:
	for td in tr.find_all("a")[0]:
		for image in td:
			leader_icon.append(image.get('src'))
print(leader_icon[0])

#------------------------------------------------------------------------------------
#Combine Lists
@dataclass
class Leader:
	ability_title : str
	ability_text : str
	agenda_title : str
	agenda_text : str

combined = {
	key : Leader(ability_title, ability_text, agenda_title, agenda_text)
	for (key, ability_title, ability_text, agenda_title, agenda_text) in zip (name, ability_title, ability_text, agenda_title, agenda_text)
}

#Discord Help Attempt - dict comprehension
#combined = {key : rest for (key, *rest) in zip(name, ability_title, ability_text, agenda_title, agenda_text)}

#Show results
# user_input = input("Enter leader name: ")
# print("\nAbility Title: \n", combined[user_input].ability_title)
# print("\nAbility Text: \n", combined[user_input].ability_text)
# print("\nAgenda Title: \n", combined[user_input].agenda_title)
# print("\nAgenda Text: \n", combined[user_input].agenda_text)

#------------------------------------------------------------------------------------
#Final - Have Seperate lists to be used in embed
