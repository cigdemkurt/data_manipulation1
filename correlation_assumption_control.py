from scipy.stats import shapiro
import pandas as pd

data = pd.read_csv('SuperMarketAnalysis.csv')

stat_of_test, pvalue=shapiro(data["Sales"])
print('Stat of test = %.4f, p-value= %.4f' % (stat_of_test, pvalue))

stat_of_test, pvalue=shapiro(data["Unit price"])
print('Stat of test = %.4f, p-value= %.4f' % (stat_of_test, pvalue))

"""Stat of test = 0.9088, p-value=0.0000
Stat of test = 0.9519, p-value=0.0000"""

#p-values are 0.000, they are less than 0.5, it means the result that obtained is statistically significant.


# the shapiro() function checks whether the given data corresponds to the normal distribution by applying the Shapiro-Wilk test.
