import pandas as pd
from scipy.stats import stats
from scipy.stats import spearmanr
data= pd.read_csv("SuperMarketAnalysis.csv")

# NONPARAMETRİC HYPOTESİS TEST

sp= stats.spearmanr(data["Sales"], data["Unit price"])
print(sp)

stats_of_test, pvalue= stats.spearmanr(data["Sales"], data["Unit price"])

print('correlation coefficient= %.4f, p-value= %.4f' % (stats_of_test, pvalue))


#or kendalltau
stats_of_test, pvalue= stats.kendalltau(data["Sales"], data["Unit price"])

print('correlation coefficient= %.4f, p-value= %.4f' % (stats_of_test, pvalue))

