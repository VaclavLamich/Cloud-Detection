from resolution import resolution_image
import numpy as np
import pandas as pd



##corect size

max_sirka=0.2
max_delka=0.27

df=pd.read_csv('bboxes.csv')
for i in range(df.shape[0]):
    df.iloc[i,3]=df.iloc[i,1]+max_delka
    df.iloc[i,4]=df.iloc[i,2]+max_sirka
 
## save correct size of bboxes
iss=[19]
for i in iss:
    df.iloc[i,3]=df.iloc[i,1]+(max_delka)
    df.iloc[i,4]=(df.iloc[i,2]+max_sirka)
    df.iloc[i,2]=df.iloc[i,4]-(max_sirka/2)
 
df=np.round(df,2)
df.to_csv('bboxes_cut.csv',index=False)
#checking resolution 
# a=[]
# for i in range(df.shape[0]):
#     bounding_box=[df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4]]
#     i=resolution_image(np.round(bounding_box,2),10)
#     image=i.run()
#     a.append(image)