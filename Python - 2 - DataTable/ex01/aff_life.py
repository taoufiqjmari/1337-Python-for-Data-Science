from load_csv import load
from matplotlib import pyplot as plt


def display():
    """Displays the country information of a campus in a chart"""
    try:
        data = load("../life_expectancy_years.csv")
        morocco = data[data['country'] == 'Morocco']

        plt.figure(figsize=(10, 6))
        plt.plot(morocco.columns[1:], morocco.iloc[0, 1:])
        plt.xticks(morocco.columns[1::40])

        plt.title("Morocco Life expectancy projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")

        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    display()
