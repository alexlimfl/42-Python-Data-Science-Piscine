from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

#   table format:
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
    df_life = load('life_expectancy_years.csv')
    df_inco = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    if df_life is None or df_inco is None:
        return 1
    # print(df_life, "\n\n", df_inco)
    yr = '1900'
    df_life_yr = df_life[['country', yr]]
    df_inco_yr = df_inco[['country', yr]]
    # print(df_life_yr, "\n\n", df_inco_yr)

    merged_df = pd.merge(df_life_yr, df_inco_yr,
                         on='country', suffixes=('_life', '_inco'))
    # print(merged_df)

    plt.scatter(merged_df[yr + '_inco'], merged_df[yr + '_life'], alpha=1)
    plt.title(yr)
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')

    # x-axis
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.savefig('output_ex03.jpeg')
    plt.show()


if __name__ == "__main__":
    main()
