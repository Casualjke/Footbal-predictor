import pandas as pd

data = {
    'home',
    'score',
    'away',
    'year'
}

df = pd.DataFrame(data)
# Сохраняем DataFrame в CSV файл
df.to_csv('fifa_champions_league_fixture_data.csv', index=False)