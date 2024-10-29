# Hypothesis

import pandas as pd

data=pd.read_csv("SuperMarketAnalysis.csv")

corr_pearson= data["Sales"].corr(data["Unit price"])

print(f'correlation coefficient: ', corr_pearson)
# correlation coefficient:  0.6339620885890689
#this corr for pearson, it can calculate when the normality assumption is satisfied

corr_spearman= data["Sales"].corr(data["Unit price"], method = 'spearman')
print(f'correlation coefficient with spearman: ', corr_spearman)

#ccorrelation coefficient with spearman:  0.6300541064753133

# there is a positive and medium strength ( about 0.63) realitionship between variables

#TEST OF CORRELATİON SİGNİFİCANCE

from scipy.stats.stats import pearsonr

stats_of_test, pvalue= pearsonr(data["Unit price"], data["Sales"])

print('Stats of Value = %.4f, p-value = %.4f' % (stats_of_test, pvalue))

# Stats of Value = 0.6340, p-value = 0.0000
""""""" p value= 0.0000, H0 hypothesis rejected, there is a significiant relationship between variables.