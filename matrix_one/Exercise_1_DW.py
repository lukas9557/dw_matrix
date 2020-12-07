#DataWorkShop - Matrix exercise. Analysis of Men's Shoe Prices on the basis of
#data.worlddatafiniti/mens-shoe-prices file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("7004_1.xlsx")
#print(data.shape) #18,378 rows
#print(data.sample(n=5))
df_usd = data[data.currency == 'USD' ].copy() #filter - most of currencies are USD, so we will use ony USD
#print(df_usd.shape) #17,286 rows
df_usd.price = df_usd.price.astype(np.float)
#print(df_usd.price.hist())
print(plt.hist(df_usd.price))
plt.show()


filter_max = np.percentile(df_usd.price, 99)
print(filter_max)
df_usd_filter = df_usd[ df_usd['price'] < filter_max]

print(plt.hist(df_usd_filter.price, bins=100))
plt.show()