from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


plt.figure(figsize=(10, 6))
plt.title("Population Projections")
plt.xlabel("Year")
plt.ylabel("Population")

data = load("../population_total.csv")
morocco = data[data['country'] == 'Morocco']
morocco = morocco.loc[:, '1800':'2050']
france = data[data['country'] == 'France']
france = france.loc[:, '1800':'2050']

plt.plot(morocco.columns[:], morocco.iloc[0, :], label='Morocco')
plt.plot(france.columns[:], france.iloc[0, :], label='France')
plt.legend()

years_to_display = morocco.columns[::40]
plt.xticks(years_to_display)

plt.show()
