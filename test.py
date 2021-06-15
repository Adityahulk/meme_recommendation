import pandas as pd
import numpy as np
import Embeddings as embed 
df = pd.read_excel('memes.xlsx')
print(df.loc[0]['Table 2'])
image_id = "image"

for i in np.arange(0,len(df)):
    embed.gen_embed(df.loc[i]['Table 2'],image_id+str(i+100))
