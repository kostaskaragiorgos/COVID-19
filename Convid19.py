import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('23_3/covid_19_clean_complete.csv')
print(df.dtypes)
print("Number of Deaths:",df['Deaths'].sum())
print("Number of Confirmed:", df['Confirmed'].sum())
print("Number of Recovered:", df['Recovered'].sum())
data = [df['Deaths'].sum(), df['Confirmed'].sum(), df['Recovered'].sum()]
plt.bar(np.arange(3), data)
plt.xticks(np.arange(3), ('Deaths', 'Confirmed', 'Recovered'))
plt.show()