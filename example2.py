import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://civilization.fandom.com/wiki/Leaders_(Civ6)')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

list_of_leaders = soup.find("table", {"class": "wikitable sortable"})

tbody = list_of_leaders.find('tbody')

for tr in tbody.find_all('tr'):
	name = tr.find_all('td').find_all('a')
print(name)
