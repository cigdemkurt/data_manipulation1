import pandas as pd

road_file= 'SuperMarketAnalysis.csv'

my_data=pd.read_csv(road_file)

# print(my_data)
#print(my_data.head())

# to make transactions by handling certain columns
# first, the numerical values
unitPrice= my_data['Unit price']
quantity = my_data['Quantity']

# view column data
# print(unitPrice)
# print(quantity)

# quantity_price_df = my_data[['Unit price' , 'Quantity' ]]
# print(quality_price_df.head())

#add a categorical column

df= my_data[['Unit price', 'Quantity', 'Product line']]
# print(df.head())

#using groupby and finding statistical values
#df["Unit price"].mean()
""""aggregate_statistic_values= df.groupby("Product line")["Quantity"].describe()
print(aggregate_statistic_values)"""""


stats = df.groupby('Product line').agg({
    'Unit price': ['mean', 'sum', 'min', 'max'],
    'Quantity': ['mean', 'sum', 'min', 'max']
})

# print(stats)

#for 'Health and beauty' and 'Electronic accessories' categories, their sum values are 8337.88 and 9103.77 but their mean values are 54.854474 and  53.551588 so i think more products may have been sold in the Electronic accessories category. i should check their sum Quantity values

ea_data= my_data[my_data['Product line']== 'Electronic accessories']
sumPrice_ea=ea_data['Unit price'].sum()
sumQuantity_ea=ea_data['Quantity'].sum()

Hb_data= my_data[my_data['Product line']== 'Health and beauty']
sumQuantity_Hb= Hb_data['Quantity'].sum()

"""print (sumQuantity_ea)
print (sumQuantity_Hb)"""

"""971
854"""
#this is the result of my suspect

#wanna find the category with the most sales

TotalSales= my_data.groupby('Product line')['Sales'].sum()

theMostSales= TotalSales.idxmax()

# print(f'Product line has the most sales: {theMostSales}')

#Food and beverages

# find average selling time

Food_Beverages= my_data[my_data['Product line']== 'Food and beverages']

average_sale= Food_Beverages.groupby('Time')['Sales'].mean()

theMostAverageTime= average_sale.idxmax()
# print(average_sale)
#print(f'the average time with the most sales: {theMostAverageTime}')

#the average time with the most sales: 8:23:00 PM
# find the city with the most shoppers at 8:23:00 PM

time_8_23_pm= Food_Beverages[Food_Beverages['Time']== '8:23:00 PM']

the_city_sumsale= my_data.groupby('City')['Sales'].sum()
#print(the_city_sumsale)

the_city_mostsale= the_city_sumsale.idxmax()



# print(f'the city with the most shoppers at 8:23:00 PM: {the_city_mostsale}')

# the city with the most shoppers at 8:23:00 PM: Naypyitaw

#find which gender had the most sale at 8:23:00 pm

which_gender= my_data.groupby('Gender')['Sales'].sum()
print(which_gender)

the_mostSale_fromGender= which_gender.idxmax()
print(f'the gender that shops the most at 8:23:00 PM: {the_mostSale_fromGender}')

# the gender that shops the most at 8:23:00 PM: Female

