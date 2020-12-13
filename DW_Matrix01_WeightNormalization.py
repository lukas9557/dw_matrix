#Exercise regarding to DataWorkshop Matrix.
#conversion of weights in different measures to grams.
import pandas as pd

col4 = ['3.0 lbs', '9 g', '1.45 lbs', '0.45 lbs', '1.0 lbs', '0.23 lbs', '5.0 lbs', '5.5 lbs', '7.45 lbs', '4.0 lbs', '2.7969 lbs', '3.9 lbs', '4.6 pounds', '2.1 lbs', '1.1057 lbs', '15.0 lbs', '2.4 ounces', '454 g', '0.105 lbs', '9.1 ounces', '4.8 lbs', '6.1 lbs', '6.5 lbs', '1.1041 lbs', '1.3 Kg', '91 g', '20.0 lbs', '6.0 lbs', '386 g', '0.81 lbs', '4.5 lbs', '0.5 ounces', '2.0 lbs', '3.1? lbs', '5.9 lbs', '6.15 lbs', '1 pounds', '1.95 lbs', '2.15 lbs', '2 pounds', '2.1 pounds', '14 Kg', '0.4788 lbs', '10.0 lbs', '0.38 lbs', '2.5 lbs', '68.912 lbs', '45 g', '13.09 lbs', '2.5 pounds', '0.21 lbs', '16.75 lbs', '6.3 lbs', '272 g', '1.8 Kg', '2.8 pounds', '0.1 lbs', '5.05 lbs', '0.28 lbs', '76.08 lbs', '0.15 lbs', '200 g', '7.8 pounds', '399 g', '4.95 lbs', '64.144 lbs', '24 pounds', '73.696 lbs', '1.6 lbs', '6.6 ounces', '5 g', '1.2 Kg', '862 g', '3.05 lb', '8.6 ounces', '3.6 lbs', '71.296 lbs', '5.2 pounds', '3.44 lbs', '0.3 ounces', '1.4 Kg']
col3 = list()
col1 = list()
for i in range(len(col4)):
    col3.append(i)

col1 = col4.copy()
data = {"ID": col3, "Weight_before": col4}
df = pd.DataFrame(data, columns=["ID","Letters","Weight_before"])

for i in range(len(col1)):
    col1[i] = col1[i].replace("?","") #there was a single value with "?", so I removed it
    space_position = col1[i].find(" ") #find space in each weight from column 1
    value = col1[i][:space_position]
    measure = col1[i][space_position+1:]

    if measure in["lbs", "lb", "pounds"]:
        value = round(float(value) * 453.59237,1)
        col1[i] = str(value) + " gram"
    elif measure == "ounces":
        value = round(float(value) * 28.3495231,1)
        col1[i] = str(value) + " gram"
    elif measure == "Kg":
        value = round(float(value) * 1000,1)
        col1[i] = str(value) + " gram"
    elif measure == "g":
        value = round(float(value), 1)
        col1[i] = str(value) + " gram"

df['Weight_after'] = col1
print(df)

writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
writer.save()
