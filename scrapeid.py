import requests
from bs4 import BeautifulSoup

url = "https://www.pro-football-reference.com/years/2022/passing.htm"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')

players = soup.find('table',id='passing')

print(players)
