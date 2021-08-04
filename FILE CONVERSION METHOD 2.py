import pandas as pd

tsv_file='DRC_full.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
df=csv_table.to_csv('DRC_full CSV1.csv',index=False)
print(df)
