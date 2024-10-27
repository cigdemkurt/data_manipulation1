# covariance is a measure of the variability of the relationship between two variables.
# if two variables are increasing or reducing simultaneously covariance is positive, otherwise covariance is negative

# correlation is a statistical technique that expresses the relationship between two variables, whether the relationship is significant, the severity and direction of the relationship
#if the correlation between the two values is close to 1, there is a positive correlation as one increases the other increases
# if the correlation between two values is close to -1, there is a negative correlation as one increases, the other reduces
# if the correlation between the two values is close to 0, there is no significant relationship.

import pandas as pd


data = pd.read_csv('SuperMarketAnalysis.csv')


covariance = data[['Unit price', 'Sales']].cov().iloc[0,1]

#print(f"Unit price  Sales : {covariance}")
# Unit price  Sales : 4130.035141976606

# the covariance value is positive, its mean that as the unit price increases, sales also increase

correlation= data['Unit price'].corr(data['Sales'])
print(f"Between unit price and sales values correlation: {correlation}")

# Between unit price and sales values correlation: 0.6339620885890688
# the correlation value is close to 1, so there is a positive correlation










