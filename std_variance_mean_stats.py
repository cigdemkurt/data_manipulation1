import pandas as pd

road_file= 'SuperMarketAnalysis.csv'

my_data=pd.read_csv(road_file)

#using fancy index

fancy_index= ['Product line' , 'gross margin percentage', 'gross income', 'Tax 5%']

df=my_data[fancy_index]
# df_sum=df.groupby('Product line').sum()

# print(df.head())
# print(df_sum.head())

#this way for total values

"""""""""
                        gross margin percentage  gross income     Tax 5%
Product line                                                            
Electronic accessories                 4.761905     15.220597  15.220597
Fashion accessories                    4.761905     14.528062  14.528062
Food and beverages                     4.761905     15.365310  15.365310
Health and beauty                      4.761905     15.411572  15.411572
Home and lifestyle                     4.761905     16.030331  16.030331
Sports and travel                      4.761905     15.812630  15.812630

"""""
df_mean=df.groupby('Product line').mean()
print(df_mean)

#it is important that std and mean values are close to each other


df_std=df.groupby('Product line').std()
print(df_std)

""""""" """"                gross margin percentage  gross income     Tax 5%
Product line                                                            
Electronic accessories                      0.0     11.711696  11.711696
Fashion accessories                         0.0     11.598292  11.598292
Food and beverages                          0.0     11.769418  11.769418
Health and beauty                           0.0     11.311372  11.311372
Home and lifestyle                          0.0     12.123841  12.123841
Sports and travel                           0.0     11.827397  11.827397
"""""""""""""""

# it is observed that the data are consistent

df_variance= df.groupby('Product line').var()
print(df_variance)

"""""""""                        gross margin percentage  gross income      Tax 5%
Product line                                                             
Electronic accessories                      0.0    137.163835  137.163835
Fashion accessories                         0.0    134.520375  134.520375
Food and beverages                          0.0    138.519203  138.519203
Health and beauty                           0.0    127.947140  127.947140
Home and lifestyle                          0.0    146.987533  146.987533
Sports and travel                           0.0    139.887309  139.887309

"""""


