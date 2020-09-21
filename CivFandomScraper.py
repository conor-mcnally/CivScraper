#Finding results from webpage containing a table
import re
import requests
from bs4 import BeautifulSoup
import urllib.request

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

#This works - Finds only p tags in list of leaders
#Retrives Leader ability & leader agenda, need to split by seperate p tags
# p - finds descriptions for abiliy and agenda
# b - names of agendas and abilities
# a - SHOULD find name of leader(td[0]), where td[0] == leader, td[1] == civ, td[2] == ability, td[3] == agenda

#-----------------------------------------------------------------------------------
#LEADER ABILITY/AGENDA TITLE
#Extract leader ability/agenda titles from table
leader_info_titles = []
for td in leader:
	leader_info_titles.append(td.find_all('b'))

#Save all agenda/ability titles to lists
leader_info_titles.pop(0) #First entry is empty, remove
ability_title = [i[0] for i in leader_info_titles] #Seperate ability to seperate list
agenda_title = [i[1] for i in leader_info_titles]  #Seperate agenda to seperate list

#Strip html tags
ability_title = strip_html(ability_title)
agenda_title = strip_html(agenda_title)

#Show results
print("Ability Title: \n", ability_title[1], "\nAgenda Title: \n", agenda_title[1])
#------------------------------------------------------------------------------------
#LEADER ABILITY/AGENDA TEXT
#Extract leader ability/agenda text from table
leader_info_text = []
for td in leader:
	leader_info_text.append(td.find_all('p'))

#Save all agenda/ability text to lists
leader_info_text.pop(0) #First entry is empty, remove
ability_text = [i[0] for i in leader_info_text] #Seperate ability to seperate list
agenda_text = [i[1] for i in leader_info_text]  #Seperate agenda to seperate list

#Strip html tags
ability_text = strip_html(ability_text)
agenda_text = strip_html(agenda_text)

#Show results
print("\nAbility Text: \n", ability_text[1], "\nAgenda Text: \n", agenda_text[1])
#------------------------------------------------------------------------------------
#Leader Name

#------------------------------------------------------------------------------------
#Leader Icon

#------------------------------------------------------------------------------------
#Final step, combine each corresponding element in leader name, leader icon, leader emblem, leader ability/agenda title & leader ability/agenda text

# for tr in list_of_leaders.find_all('tr'):
# 	leader = tr.find_all('td')[1].text.strip()
# 	civilization = tr.find_all('td')[2].text.strip()
# 	leader_ability = tr.find_all('td')[3].text.strip()
# 	leader_agenda = tr.find_all('td')[4].text.strip()
# 	print(leader, civilization, leader_ability, leader_agenda)
