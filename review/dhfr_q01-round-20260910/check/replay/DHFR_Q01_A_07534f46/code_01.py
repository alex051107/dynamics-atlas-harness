import pandas as pd, glob, os, numpy as np
for f in glob.glob('/source/data/*_distances.tsv'):
 d=pd.read_csv(f,sep='\t'); print('\n',os.path.basename(f),d.shape); print(list(d.columns))
 print(d.head(2).to_string(index=False))
