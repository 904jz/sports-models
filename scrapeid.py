import requests
from bs4 import BeautifulSoup
import csv

# url = "https://www.pro-football-reference.com/years/2022/passing.htm"
url = "https://www.pro-football-reference.com/years/2022/rushing.htm"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')

players = soup.find('table',id='rushing')

phead = players.find('thead')
# print(phead.text)

data = players.find('tbody')
rows = data.find_all('tr')
# for row in rows[:50]:
    # print(row)
with open('playerData.txt',"w", newline='') as f:
    
    f.write(str(players))


    

# print(players)
