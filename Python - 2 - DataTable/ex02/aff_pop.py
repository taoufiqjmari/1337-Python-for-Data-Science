from load_csv import load
from matplotlib import pyplot as plt


def convert_to_numeric(value):
    """Convert a represtation to a numeric value"""
    if value.endswith('M'):
        return float(value[:-1]) * 1000000
    elif value.endswith('k'):
        return float(value[:-1]) * 1000
    else:
        return float(value)


def process_country(data, name):
    """Select country and set it right for coming calculations"""
    country = data.loc[data['country'] == name, '1800':'2050']
    for i in range(len(country.iloc[0, :])):
        country.iloc[0, i] = convert_to_numeric(country.iloc[0, i])
    return country


def display():
    """Displays a country population versus another in a chart"""
    try:
        data = load("../population_total.csv")
        morocco = process_country(data, 'Morocco')
        france = process_country(data, 'France')
        # belgium = process_country(data, 'Belgium')

        plt.figure(figsize=(10, 6))
        plt.plot(morocco.columns[:], morocco.iloc[0, :], label='Morocco')
        plt.plot(france.columns[:], france.iloc[0, :], label='France')
        # plt.plot(belgium.columns[:], belgium.iloc[0, :], label='Belgium')

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend()

        years_to_display = morocco.columns[::40]
        plt.xticks(years_to_display)
        plt.yticks([0, 20_000_000, 40_000_000, 60_000_000],
                   ['0', '20M', '40M', '60M'])

        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    display()
