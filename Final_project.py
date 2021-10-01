# import visualization libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# read data
price_rd = pd.read_csv('price_paid_records_small.csv')

# display the first 5 rows in data
print(price_rd.head(5))

# min, max, mean of data
des_data = price_rd.describe()
print('Describe the Price paid ', des_data)

# Count the number of County in Dataframe
cnt_county = pd.value_counts(price_rd['County'])
print('The number of Country in DataFrame', cnt_county)

# create a new column Year from the first 4 characters of the Date of Transfer feature
price_rd['Year'] = price_rd['Date of Transfer'].str[:4]
print(price_rd)

# List the high price above 500000 in Town/City
lst = price_rd[['Price', 'Old/New', 'Town/City']]
hgh_pr = lst[(lst['Price'] >= 500000)]
print(hgh_pr)

# Draw chart about Price
plt.hist(price_rd['Price'])
plt.title('All House Prices Distribution')
plt.xlabel('House Price (£)')
plt.ylabel('Count')
plt.show()

