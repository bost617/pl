## this script gets the Premier League tables and prints the results
from bs4 import BeautifulSoup
import requests
sky_url = "https://www.skysports.com/premier-league-table"
bbc_url = "https://www.bbc.com/sport/football/tables"
skyweb = requests.get(sky_url)
skyweb_status = skyweb.status_code
if skyweb_status != 200:
    print(" Sky Sports Website Unavailable")
bbcweb = requests.get(bbc_url)
bbcweb_status = bbcweb.status_code
if bbcweb_status != 200:
    print(" BBC Sports Website Unavailable")
    
sky_soup = BeautifulSoup(skyweb.content, 'html.parser')
bbc_soup = BeautifulSoup(bbcweb.content, 'html.parser')

sky_table = sky_soup.find_all('tr', class_ = 'standing-table__row')
row_number = 1
print("\n")
print("__ Sky __ Sports __ Website __")
for each_row in sky_table:
    place = sky_table[row_number].find_all('td')[0].get_text().strip()
    team = sky_table[row_number].find_all('td')[1].get_text().strip()
    games = sky_table[row_number].find_all('td')[2].get_text().strip()
    wins = sky_table[row_number].find_all('td')[3].get_text().strip()
    print(place+". "+team+" has won "+wins+" of "+games+" games")
    row_number = row_number + 1
    if row_number == 5:
        print("------------")
    if row_number == 6:
        print("------------")
    if row_number == 18:
        print("--+ RELEGATION +--")
    if row_number > 20:
        break
print("\n")    
bbc_table = bbc_soup.find_all('tr')
row_number = 1
print("__ BBC __ Sport __ Website __")
for each_row in bbc_table:
    place = bbc_table[row_number].find_all('td')[0].get_text()
    team = bbc_table[row_number].find_all('td')[2].get_text()
    games = (bbc_table[row_number].find_all('td')[3].get_text())
    wins = bbc_table[row_number].find_all('td')[4].get_text()
    draws = bbc_table[row_number].find_all('td')[5].get_text()
    losses = bbc_table[row_number].find_all('td')[6].get_text()
    goals_for = (bbc_table[row_number].find_all('td')[7].get_text())
    goals_against = bbc_table[row_number].find_all('td')[8].get_text()
    goal_different = bbc_table[row_number].find_all('td')[9].get_text()
    points = bbc_table[row_number].find_all('td')[10].get_text()
    avg_goals = round(int(goals_for)/int(games),2)
    avg_goals = str(avg_goals)
    win_percent = round(float(int(wins)/int(games)*100))
    win_percent = str(win_percent)
    print(place+". "+team+" has scored "+avg_goals+" goals/game and won "+win_percent+"% of games")
    row_number = row_number + 1
    if row_number == 5:
        print("------------")
    if row_number == 6:
        print("------------")
    if row_number == 18:
        print("--+ RELEGATION +--")
    if row_number > 20:
        break