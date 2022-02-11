import numpy as np
import pandas as pd
from get_data import get_data
from utils import plot_image
from datetime import datetime

startTime = datetime.now()

df=pd.read_csv('bboxes_cut.csv')
dates=["2021-11-01","2021-11-11","2021-11-21","2021-12-01","2021-12-11","2021-12-21",
       "2021-12-31","2022-01-11","2022-01-21","2022-01-31","2022-02-10"]

resolution=10
all_bands=0
clouds=[0,1]
max_cc=[0.05,0.5]
i=1
stop=0

k=0
bounding_box=[df.iloc[k,1],df.iloc[k,2],df.iloc[k,3],df.iloc[k,4]]
start=dates[i]
end=dates[i+1]
noclouds=get_data(bounding_box,resolution,start,end,1,all_bands,0.55)
(noclouds_image,clm)=noclouds.run()
rgb=noclouds_image[:,:,1:4]
rgb=rgb[:,:,::-1]

plot_image(rgb, factor=3.5/1e4, vmax=1)

print(datetime.now() - startTime)