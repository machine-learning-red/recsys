import pandas as pd
from apriori_python import apriori

url = "./datasets/dataset_apriori.csv"
df = pd.read_csv(filepath_or_buffer=url, sep=',', header=None, names=['col1', 'col2', 'col3'])

print(df.head())
# maybe turn this into a matrix manually with a loop loading with csv reader?

freqItemSet, rules = apriori(df, minSup=0.11, minConf=0.5)
print("ITEMSETS FRECUENTES:")
print(freqItemSet)
print("REGLAS DE ASOCIACION:")
print(rules)