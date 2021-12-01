import csv
import pandas as pd
from io import StringIO

# url = "https://raw.githubusercontent.com/machine-learning-red/recsys/main/dataset_base.csv"
url = "./datasets/dataset_base.csv"
df = pd.read_csv(url)
print(df.head())

apriori = df.copy()
for column in df:
    if column != "ID_Cliente":
      apriori.loc[(df[column] > 0), column] = column
      apriori.loc[(df[column] == 0), column] = None
print(apriori.head())

DS_APRIORI_FILENAME = './datasets/dataset_apriori.csv'
f = open(DS_APRIORI_FILENAME, 'w') # open the file in the write mode
writer = csv.writer(f) # create the csv writer
csv = StringIO(u""+apriori.to_csv(index=False, header=False))
for row in csv.readlines():
  r = row
  try:
    while r.index(",,"):
      r = r.replace(",,",",")
  except ValueError:
    pass # ignore not finding any more commas
  r = r[:-2] # removes \n and the last comma
  writer.writerow(r.split(",")) # write a row to the csv file
f.close() # close the file