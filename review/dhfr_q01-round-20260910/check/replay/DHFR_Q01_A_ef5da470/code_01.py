import pandas as pd,glob,os
for f in glob.glob('/source/data/*distances.tsv'):
 d=pd.read_csv(f,sep='\t'); print(os.path.basename(f),d.shape,list(d.columns))
 print(d.head(2).to_string(index=False))