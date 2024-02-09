from load_csv import load
from matplotlib import pyplot as plt


def display():
    """Displays a scatter chart showing correlation between life span"""
    """and gross domestic product in 1900"""
    try:
        le = load('../life_expectancy_years.csv')
        gdp = load(
            '../income_per_person_gdppercapita_ppp_inflation_adjusted.csv')

        le_1900 = le['1900']
        gdp_1900 = gdp['1900']

        plt.figure(figsize=(10, 6))
        plt.scatter(gdp_1900, le_1900)

        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale('log')
        plt.xticks([300, 1_000, 10_000],
                   ['300', '1k', '10k'])

        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    display()
