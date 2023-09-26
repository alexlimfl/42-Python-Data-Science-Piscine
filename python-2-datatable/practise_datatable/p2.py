import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}

df = pd.DataFrame(data)

# Using single brackets returns a Series
series_result = df['A']

# Using double brackets returns a DataFrame
dataframe_result = df[['A']]

print(series_result)  # <class 'pandas.core.series.Series'>
print(type(series_result))  # <class 'pandas.core.series.Series'>
print(dataframe_result)  # <class 'pandas.core.frame.DataFrame'>
print(type(dataframe_result))  # <class 'pandas.core.frame.DataFrame'>
