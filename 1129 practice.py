import pandas as pd

filename = "./data/1_pima.csv"
column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(filename, names=column_names)
correlations = data.corr(method='pearson')
print(correlations)
correlations = data.corr(method='pearson')
correlations.to_csv("./results/correlation_coefficient.csv")