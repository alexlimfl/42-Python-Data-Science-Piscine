from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def convert_to_numeric(v):
    """converts str, 'k' and 'M' to numbers"""
    if v.endswith('k'):
        return int(float(v[:-1]) * 1e3)
    elif v.endswith('M'):
        return int(float(v[:-1]) * 1e6)
    elif v.endswith('B'):
        return int(float(v[:-1]) * 1e9)
    else:
        return int(float(v))

# table format:
#   get specific column in series:
#       df['column A','column B']
#   get specific column in dataframe:
#       df[['column A','column B']]
#   get specific row:
#       df[start:end]
#   get rows and columns simultaneously:
#       df.loc[rows, columns]
#   get rows based on condition:
#       df[condition]


def main():
    csv = load('population_total.csv')
    if csv is None:
        return 1
    # print(csv)

    #   csv[csv['column title'] == 'keyword in the column']
    csv.iloc[:, 1:] = csv.iloc[:, 1:].map(convert_to_numeric)
    country1 = csv[csv['country'] == 'France']
    country2 = csv[csv['country'] == 'Malaysia']
    year = csv.columns[1:].astype(int).values
    year_2050 = year[year <= 2050]
    col_2050yr = len(year_2050) + 1
    plt.plot(year_2050, country1.values[0][1:col_2050yr], label='France')
    plt.plot(year_2050, country2.values[0][1:col_2050yr], label='Malaysia')
    plt.title('Population Projection')

    # x-axis
    x_ticks = np.arange(min(year_2050), max(year_2050), 40)
    plt.xticks(x_ticks)
    plt.xlabel('Year')

    # y-axis
    max_popu = max(max(country1.values[0][1:col_2050yr]),
                   max(country2.values[0][1:col_2050yr]))
    min_popu = min(min(country1.values[0][1:col_2050yr]),
                   min(country2.values[0][1:col_2050yr]))
    plt.ylabel('Population')
    y_ticks = np.arange(min_popu, max_popu, 20 * 1e6)
    y_tick_labels = [f'{int(val/1e6)}M' for val in y_ticks]
    plt.yticks(y_ticks, y_tick_labels)
    plt.legend(loc='lower right')
    plt.savefig('output_ex02.jpeg')
    plt.show()


if __name__ == "__main__":
    main()
