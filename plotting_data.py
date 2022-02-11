import numpy as np
import pandas as pd
from get_image import get_image
from utils import plot_image
from datetime import datetime

startTime = datetime.now()

df=pd.read_csv('bboxes_cut.csv')

### parameters of get_image are 
#(bbox,resolution,start_date,end_date,leastClouds(0=yes,1=no),all_bands(0=yes, 1=no),maxcc=(float 0-1))

start="2021-01-11"
end="2021-01-20"
leastClouds=0
all_bands=1
resolution=10
max_cc=0.05

# for i in range(df.shape[0]):
#     bounding_box=[df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4]]
#     i=get_image(bounding_box,resolution,start,end,leastClouds,all_bands,max_cc)
#     image=i.run()
#     plot_image(image, factor=3.5/255, clip_range=(0,1))
#isss=[0,1,2,3,4,5,6,9,10,11,12,14,15,16,17,18,20,22,23,24,25,27,28,29,30,31]
#isss=[0,1,3,5,6,9,11,12,14,15,16,17,18,20,22,23,24,25,27,28,29,30,31]
iss=[7]#,26]
for i in iss:
    bounding_box=[df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4]]
    i=get_image(bounding_box,resolution,start,end,leastClouds,all_bands,max_cc)
    image=i.run()
    plot_image(image, factor=3.5/255, clip_range=(0,1))


print(datetime.now() - startTime)
