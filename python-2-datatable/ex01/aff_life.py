from load_csv import load
# import matplotlib
# matplotlib.use('WXAgg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    csv = load("life_expectancy_years.csv")
    if csv is None:
        return 1
    print(csv)
    # x_data = csv.columns[1:].astype(float).values
    # x_data = csv[1:]
    # row = csv.loc[123].values
    # row = csv.loc[123].values
    # france = 58
    # malaysia = 123
    country = csv[csv['country'] == 'Malaysia']
    year = csv.columns[1:].astype(int).values
    # print(country)
    # print(country.values)
    # print(country.values[0])
    plt.plot(year, country.values[0][1:])
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('Malaysia Life Expectancy Projection')
    x_ticks = np.arange(min(year), max(year), 40)
    plt.xticks(x_ticks)
    plt.savefig('output_ex01.jpeg')
    plt.show()


if __name__ == "__main__":
    main()
