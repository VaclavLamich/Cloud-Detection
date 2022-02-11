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
i=0
k=2
stop=0
save_data_noC=[]
while stop==0 & i<9:
    print(i)
    bounding_box=[df.iloc[k,1],df.iloc[k,2],df.iloc[k,3],df.iloc[k,4]]
    start=dates[i]
    end=dates[i+1]
    noclouds=get_data(bounding_box,resolution,start,end,0,all_bands,0.05)
    (noclouds_image,clm)=noclouds.run()
    if noclouds_image[0][0][0]==0:
        i=i+1
    else:
        save_data_noC.append([noclouds_image,start,end,"noclouds"])
        stop=1
        
stop=0
i=0
save_data_C=[]
while stop==0 and i<9:
    print(i)
    bounding_box=[df.iloc[k,1],df.iloc[k,2],df.iloc[k,3],df.iloc[k,4]]
    start=dates[i]
    end=dates[i+1]
    
    clouds=get_data(bounding_box,resolution,start,end,1,all_bands,0.5)
    (clouds_image,clmask)=clouds.run()
    
    prst=(np.sum(clmask))/(clmask.shape[0]*clmask.shape[1])
    if clouds_image[0][0][0]==0:
        i=i+1
    elif prst<0.2:
        i=i+1
    elif prst>0.6:
        i=i+1
    else:
        save_data_C.append([clouds_image,start,end,"clouds"])
        stop=1

rgb=noclouds_image[:,:,1:4]
rgb=rgb[:,:,::-1]

rgb2=clouds_image[:,:,1:4]
rgb2=rgb2[:,:,::-1]


plot_image(rgb, factor=3.5/1e4, vmax=1)
plot_image(rgb2, factor=3.5/1e4, vmax=1)

# import pickle
# string="C:/Users/vacla/Documents/Cloud-Detection/data/"
# string=string + df.iloc[i,0] + '_' + 'clouds'
# with open(string, "wb") as fp:   #Pickling
#     pickle.dump(save_data_C, fp)

# string="C:/Users/vacla/Documents/Cloud-Detection/data/"
# string=string + df.iloc[i,0] + '_' + 'no_clouds'

# with open(string, "wb") as fp:   #Pickling
#     pickle.dump(save_data_noC, fp)

# # with open("test", "rb") as fp:   # Unpickling
# #     b = pickle.load(fp)

print(datetime.now() - startTime)
