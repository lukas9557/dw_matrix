import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_hdf("train.car_price.h5")
plt.hist(df.price_value, bins=100) #prices histogram
plt.show()

print(df.columns.values)
print(df.price_value.describe()) #the most important statistics of data

def group_and_barplot(feat_groupby, feat_agg = 'price_value', agg_funcs=[np.median, np.mean, np.size], feat_sort='mean', feat_asc=False, top=50):
    print(df
        .groupby(feat_groupby)[feat_agg]
        .agg(agg_funcs)
        .sort_values(by=feat_sort, ascending=feat_asc)
        .head(top)
        .plot(kind='bar', figsize = (15,5), subplots=True))
    plt.show()

group_and_barplot('param_year', feat_sort='mean')