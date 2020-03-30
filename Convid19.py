import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('23_3/covid_19_clean_complete.csv')
print(len(df))
print(df.dtypes)
df['Country/Region']= df['Country/Region'].astype("string")
df = df.drop_duplicates(subset='Country/Region', keep='last')
print(len(df))
print("Number of Deaths:",df['Deaths'].sum())
print("Number of Confirmed:", df['Confirmed'].sum())
print("Number of Recovered:", df['Recovered'].sum())
"""
data = [df['Deaths'].sum(), df['Confirmed'].sum(), df['Recovered'].sum()]
plt.bar(np.arange(3), data)
plt.xticks(np.arange(3), ('Deaths', 'Confirmed', 'Recovered'))
plt.show()
print(df[df['Country/Region']=="Greece"]['Confirmed'].sum())
print(df[df['Country/Region']=="Greece"]['Deaths'].sum())
print(df[df['Country/Region']=="Greece"]['Recovered'].sum())
"""


print(df.loc[(df['Country/Region']=="Greece") &(df['Date']=='3/22/20')])

import datetime
day = datetime.date(2020,3,20).strftime('%x')
print(day.year)
month = datetime.date(2020,3,20).month
day = datetime.date(2020,3,20).day

print(df.loc[(df['Country/Region']=="Greece") &(df['Date']==str(str(month)+'/'+str(day)+'/'+str(year)))])
