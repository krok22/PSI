import numpy as np
import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from subprocess import check_output

df_2017 = pd.read_csv('./input/2017.csv')
df_2017.head()

# sprawdenie korelacji pomiedzy happiness score i GDP (produkt krajowy brutto)
happiness_score = df_2017['Happiness.Score']
Economy_GDP = df_2017['Economy..GDP.per.Capita.']

# tworzenie wykresu happiness score(PKB)
plt.scatter(happiness_score,Economy_GDP)
plt.title('Korelacja pomiedzy Happiness Score i PKB')
plt.xlabel('Happiness Score')
plt.ylabel('Produkt Krajowy Brutto')
plt.show()
print('Korelacja pomiedzy Szczęście a PKB:',happiness_score.corr(Economy_GDP))


# sprawdenie korelacji pomiedzy happiness score i niski przedział ufności
LowerConfidenceInterval = df_2017['Whisker.low']

# tworzenie wykresu Szczęście(Niski przedział ufności)
plt.scatter(happiness_score,LowerConfidenceInterval)
plt.title('Korelacja pomiedzy Happiness Score i Lower Confidence Interval')
plt.xlabel('Szczęście')
plt.ylabel('Niski przedział ufności')
plt.show()
print('Korelacja pomiedzy Szczęście a Niski przedział ufności:',happiness_score.corr(LowerConfidenceInterval))

# sprawdenie korelacji pomiedzy Szczęście i wysoki przedział ufności
HighConfidenceInterval = df_2017['Whisker.high']

# tworzenie wykresu Szczęście(Wysoki przedział ufności)
plt.scatter(happiness_score,HighConfidenceInterval)
plt.title('Korelacja pomiedzy Szczęście i Wysoki przedział ufności')
plt.xlabel('Szczęsice')
plt.ylabel('Wysoki przedział ufności')
plt.show()
print('Korelacja pomiedzy Szczęście a Wysoki przedział ufności:',happiness_score.corr(HighConfidenceInterval))

# sprawdenie korelacji pomiedzy happiness score a czynnik rodzinny
Family = df_2017['Family']

# tworzenie wykresu Szczęście(Rodzina)
plt.scatter(happiness_score,Family)
plt.title('Korelacja pomiedzy Happiness Score i Family')
plt.xlabel('Szczęście')
plt.ylabel('Rodzina')
plt.show()
print('Korelacja pomiedzy Szczęście a Rodzina:',happiness_score.corr(Family))

# sprawdenie korelacji pomiedzy wolnoscia a oczekiwana dalsza długośia trwania życia
freedom = df_2017['Freedom']
Life_expectacny = df_2017['Health..Life.Expectancy.']
# tworzenie wykresu Szczęście(Oczekiwana dalsza długośia trwania życia)
plt.scatter(happiness_score,Life_expectacny)
plt.xlabel('Szczęście')
plt.ylabel('Oczekiwana dalsza długośia trwania życia')
plt.show()
print('Korelacja pomiedzy Szczęście a Oczekiwana dalsza długościa trwania życia:',happiness_score.corr(Life_expectacny))


# sprawdenie korelacji pomiedzy Szczęśćie(korupcja)
corruption_data = df_2017['Trust..Government.Corruption.']
# rysowanie wykresy v0.1
plt.scatter(happiness_score,corruption_data)
plt.ylabel('Korupcja')
plt.xlabel('szczęśćie')
plt.show()
print('Korelacja pomiedzy Szczęśćie a Korupcja:',happiness_score.corr(corruption_data))


# sprawdenie korelacji pomiedzy Szczęście(Wolność)
Freedom = df_2017['Freedom']
# rysowanie wykresy v0.1
plt.scatter(happiness_score,Freedom)
plt.ylabel('Freedom')
plt.ylabel('Happiness Score')
plt.show()
print('Korelacja pomiedzy Szczęście a Wolność:',happiness_score.corr(Freedom))


# sprawdenie korelacji pomiedzy Dystopia Residual a Happiness Score
DystopiaResidual = df_2017['Dystopia.Residual']

# rysowanie wykresy v0.1
plt.scatter(happiness_score,DystopiaResidual)
plt.ylabel('Dystopia Residual')
plt.xlabel('Happiness Score')
plt.show()
print('Korelacja pomiedzy Szczęście a Dystopia Residual:',happiness_score.corr(DystopiaResidual))

# sprawdenie korelacji pomiedzy Szczęście(Hojność)
Generosity = df_2017['Generosity']
# rysowanie wykresy v0.1
plt.scatter(Generosity,happiness_score)
plt.xlabel('Hojność')
plt.ylabel('Happiness Score')
plt.show()
print('Korelacja pomiedzy Szczęście a Hojność:',corruption_data.corr(Generosity))

# odczyt z pliku
df_2016 = pd.read_csv('./input/2016.csv')
df_2016.head()

features = ['Economy (GDP per Capita)','Family','Health (Life Expectancy)','Country']
temp_dataframe = df_2016[features]
temp_dataframe = temp_dataframe.sort_values('Country')

# usuwanie 'Country' z tablicy danych
del temp_dataframe['Country']
X = temp_dataframe
label = 'Happiness Score'
Y = df_2016[label]
regressor = LinearRegression()
model = regressor.fit(X,Y)
del df_2016['Region']
df_2017.columns = df_2016.columns
df_2017
temp_dFrame = df_2017.sort_values('Country')

new_features = ['Economy (GDP per Capita)','Family','Health (Life Expectancy)']
train_x = temp_dFrame[new_features]
train_y = temp_dFrame[label]
prediction = regressor.predict(train_x)

temp_df = pd.DataFrame()
temp_df['Original Happiness Score'] = train_y
temp_df['Predicted Happiness Score'] = prediction

temp_df['Country'] = df_2016['Country']
mean_squared_error_value = sqrt(mean_squared_error(y_true=train_y,y_pred=prediction))
print('błąd: ',mean_squared_error_value)

