from bs4 import BeautifulSoup
import requests
import pandas as pd 

years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]



def get_matches(year):
    year= int(year)
    season =  f"{year}–{year-1999}"
    web =  f'https://en.wikipedia.org/wiki/{season}_UEFA_Champions_League_group_stage'
    response = requests.get(web)
    content = response.text 
    soup = BeautifulSoup(content, 'html.parser')

    matches = soup.find_all('div',class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches: 
        home.append(match.find('th',class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())

    dict_football = {'home':home, 'score':score, 'away':away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = f'{year}-{year+1}'
    return df_football


def get_fixture_matches(year):
    year= int(year)
    season =  f"{year}–{year-1999}"
    web =  f'https://en.wikipedia.org/wiki/{season}_UEFA_Champions_League_league_phase'
    response = requests.get(web)
    content = response.text 
    soup = BeautifulSoup(content, 'html.parser')

    matches = soup.find_all('div',class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches: 
        home.append(match.find('th',class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away.append(match.find('th',class_='faway').get_text())

    dict_football = {'home':home, 'score':score, 'away':away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = f'{year}-{year+1}'
    return df_football

#historical
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa,ignore_index=True)
df_fifa.to_csv('fifa_champions_league_historical_data.csv',index = False,encoding='utf-8-sig')

#fixture
df_fixture = get_fixture_matches(2024)
df_fixture.to_csv('fifa_champions_league_fixture_data.csv',index = False,encoding='utf-8-sig')
