from load_csv import load
import matplotlib.pyplot as plt

data = load("../life_expectancy_years.csv")

morocco = data[data['country'] == 'Morocco']

plt.figure(figsize=(10, 6))
plt.plot(morocco.columns[1:], morocco.iloc[0, 1:])
years_to_display = morocco.columns[1::40]
plt.xticks(years_to_display)

plt.title("Morocco Life expectancy projections")
plt.xlabel("Year")
plt.ylabel("Life expectancy")

plt.show()
