import pandas as pd
from apriori_python import apriori

url = "./datasets/dataset_apriori.csv"
df = pd.read_csv(filepath_or_buffer=url, names=range(100), dtype=str)

print(df.head())
# maybe turn this into a matrix manually with a loop loading with csv reader?

freqItemSet, rules = apriori(df, minSup=0.5, minConf=0.5)
print("ITEMSETS FRECUENTES:")
print(freqItemSet)
print("REGLAS DE ASOCIACION:")
print(rules)