#DataWorkShop - Matrix exercise. Analysis of Men's Shoe Prices, and simple perdiction model
#on the basis of data.world/datafiniti/mens-shoe-prices file named 7004_1.csv.

########### DAY 3 ##########
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def currency_bar_chart(x,y): #it's a function which will print out popularity of currencies
    x = x.to_frame()
    x.columns = ["Count"] #change of column name
    x = x['Count'].to_list() #convert to list

    y = y.tolist() #convert to list
    y = y[:13] #removing a single currency

    y_pos = np.arange(len(y))
    plt.barh(y_pos, x, align='center')
    plt.yticks(y_pos, y)
    plt.title('Common of currencies')
    press_ent = input("Press enter to see bar chart which presents popularity of currencies. ")
    plt.show()

########## IMPORTING DATA ##########
n = list()
for i in range(0, 39): #chose how many columns we want to read
    n.append(i)

data = pd.read_csv("7004_1.csv", skipinitialspace=True, usecols=n) #read only n columns
print(data.columns) #check names of imported columns
data.columns = data.columns.str.replace(".","_") #column's names has dots, we have to replace tem with underscore
print(data.columns) #column names with _ instead of .

########## DATA PREPARATION ##########
print(data.prices_currency.unique())  #check how much different currencies we have
print(data.prices_currency.value_counts()) #check which currency is the most popular
x = data.prices_currency.value_counts()
y = data.prices_currency.unique()
#currency_bar_chart(x,y) #function calling

print(data.prices_currency.value_counts(normalize = True)) #percentage of currencies
#96% of currencies are USD, so we will use only USD to perform next steps
df_usd = data[data.prices_currency == 'USD'].copy() #filter by currency = USD
df_usd['prices_amountMin'] = df_usd['prices_amountMin'].astype(np.float) #change type to float
#press_ent = input("Press enter to see histogram which presents prices in USD. ")
#plt.hist(df_usd.prices_amountMin) #histogram of prices
#plt.show()

filter = np.percentile(df_usd.prices_amountMin, 99) #99% of prices are less or equal to this value
df_usd_filter = df_usd[df_usd.prices_amountMin < filter]
print(df_usd_filter)
#press_ent = input("Press enter to see histogram which presents 99 percentile of prices, divided to 100 bins. ")
#plt.hist(df_usd_filter.prices_amountMin, bins=100)
#plt.show() #this is result of day 3

########## DAY 4 ##########
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score

def run_model(feats):
    x = df_usd[feats].values
    y = df_usd.prices_amountMin.values

    model = DecisionTreeRegressor(max_depth=5)
    scores = cross_val_score(model, x, y, scoring='neg_mean_absolute_error')
    return(("mean(scores): ", np.mean(scores),"std(scores): ", np.std(scores)))

mean_price = np.mean(df_usd.prices_amountMin)
print("Mean price is: ", mean_price)
y_true = df_usd.prices_amountMin
y_perd = df_usd.prices_amountMin.count() * [mean_price]
print(mean_absolute_error(y_true, y_perd))

median_price = np.median(df_usd.prices_amountMin)
print("Median price is: ", median_price)
y_perd = df_usd.prices_amountMin.count() * [median_price]
print(mean_absolute_error(y_true, y_perd))

lg_price = np.expm1(np.mean(np.log1p(df_usd.prices_amountMin)))
print("Log mean price is: ", lg_price)
y_perd = df_usd.prices_amountMin.count() * [lg_price]
print(mean_absolute_error(y_true, y_perd))

df_usd['brandID'] = df_usd.brand.factorize()[0] #assigning ID to each brand
df_usd['manufacturerID'] = df_usd.brand.factorize()[0] #assigning ID to each manufacturer

print(run_model(['brandID', 'manufacturerID']))