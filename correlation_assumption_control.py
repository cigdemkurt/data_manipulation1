from scipy.stats import shapiro
import pandas as pd

data = pd.read_csv('SuperMarketAnalysis.csv')

stat_of_test, pvalue=shapiro(data["Sales"])
print('Stat of test = %.4f, p-value= %.4f' % (stat_of_test, pvalue))

stat_of_test, pvalue=shapiro(data["Unit price"])
print('Stat of test = %.4f, p-value= %.4f' % (stat_of_test, pvalue))

"""Stat of test = 0.9088, p-value=0.0000
Stat of test = 0.9519, p-value=0.0000"""

"""p-values are 0.000, they refuses the H0 hypothesis. It means there is a significant difference between the sample distribution and the normal distribution
so, should do correlation coefficient hypothesis testing"""

#between two values, there is a significant realitionship
#the shapiro() function checks whether the given data corresponds to the normal distribution by applying the Shapiro-Wilk test.
