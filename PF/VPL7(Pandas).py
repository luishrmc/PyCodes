import pandas as pd
games = pd.read_csv('games.csv')

def numRows(games):
    return games.index.size

def numColumns(games):
    return games.columns.size
    

def numGoldTotal(games):
    return games['GoldT'].sum()

def numSummerGoldCountry(games,country):
    df0 = games #[df0['Country'] == country] retorna uma lista de booleanos
    return df0[df0['Country'] == country]['GoldS'].iloc[0] #que funciona como um filtro

def getCodeMaxSummerGold(games):
    df0 = games #[df0['GoldS'] == df0['GoldS'] retorna uma lista de booleanos
    return df0[df0['GoldS'] == df0['GoldS'].max()]['Code'].iloc(0) #que funciona como um filtro

def getNthBestSummerCountry(games,n): #ORDENAÇÃO POR CAMADAS!!!!!!!!!!!!!!!!!!!!!!!!
    criteria = ['GoldS','SilverS','BronzeS'] #critério de ordenação
    sortedGames = games.sort_values(by=criteria, ascending = False)
    return sortedGames['Country'].iloc[n]

def numCountriesWithMoreThanNWinterMedals(games,n):
    df0 = games
    return df0[df0['TotalS'] > n].index.size

def numWinterCountries(games):
    df0 = games # [df0['GoldW'] > df0['GoldW'].mean()] retorna uma lista de booleanos
    return df0[df0['GoldW'] > df0['GoldW'].mean()].index.size #que funciona como um filtro

def countGoldsWithLetter(games,c):
    df0 = games #[df0['Country'][0] == c] retorna uma lista de booleanos em que 
    return df0[[df0['Country'][0]] == c]['GoldT'].sum() 

def countHybernalCountries(games):
    df0 = games
    return df0[df0['TotalS'] == df0['TotalW']].index.size + df0[df0['TotalS'] < df0['TotalW']].index.size
