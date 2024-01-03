import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

playerList = pd.read_csv("QBCleanupList.csv")
url = "https://www.pro-football-reference.com"
# f
seasonYear = ['/gamelog/2022/advanced/', '/gamelog/2021/advanced/','/gamelog/2020/advanced/','/gamelog/2019/advanced/']

with open('latestDataPullQB.csv', 'w', newline='') as f:
    scrapedGames = csv.writer(f,delimiter=' ')

    statList = []
    headerCount = 0
    #76
    for x in range(0,1):
        url_extension = playerList['ID'].iloc[x]
        playerName = playerList['Name'].iloc[x]

        for y in seasonYear:
            time.sleep(10)

            r = requests.get(url + url_extension + y)

            soup = BeautifulSoup(r.text,'html.parser')

            season_table = soup.find('table', id="advanced_passing")
            print(season_table)

            statList = []
            headerCount = 0

            print(url + url_extension + y)

            try:
                for headers in season_table.find_all('th'):
                    valueHeader = headers.text
                    if valueHeader == 'Rk':
                        headerCount = 1

                    if headerCount == 1:
                        statList.append(valueHeader)

                scrapedGames.writerow(statList)

                gameArray = []
                breakValue = 0
                #print("made it through first try segment")

                for game in season_table.find_all('tr'):
                    cols = game.find_all('td')
                    statList = [playerName]
                    for col in cols:
                        if 'Upcoming' in col.text:
                            breakValue = 1
                            break
                        else:
                            stat_col = col.text
                            #print(stat_col)
                            statList.append(stat_col)
                        if breakValue == 1:
                            break
                    print(statList)    
                    scrapedGames.writerow(statList)
                    gameArray.append(statList)



            except:
                print("can't write to file")
                continue





