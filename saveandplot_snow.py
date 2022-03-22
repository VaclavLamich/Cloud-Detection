import numpy as np
import pandas as pd
from get_data import get_data
from utils import plot_image
from datetime import datetime

startTime = datetime.now()

df=pd.read_csv('bbox_snow2.csv')
dates=[["2022-01-29","2022-02-01","2022-02-08","2022-02-10"],
       ["2022-01-29","2022-02-01","2022-02-08","2022-02-10"],
       ["2022-01-17","2022-01-19","2022-03-03","2022-03-05"],
       ["2022-01-17","2022-01-19","2022-03-03","2022-03-05"]]

resolution=10
all_bands=0
i=0

stop=0
save_data_noC=[]
indexes=[0,1,2]
for k in indexes:
    
    print(k)
    save_data_noC=[]
    
    bounding_box=[df.iloc[k,1],df.iloc[k,2],df.iloc[k,3],df.iloc[k,4]]
    start=dates[k][2]
    end=dates[k][3]
    noclouds=get_data(bounding_box,resolution,start,end,1,all_bands,0.95)
    (noclouds_image,clm)=noclouds.run()
    save_data_noC.append([noclouds_image,start,end,"noclouds"])
    
    save_data_C=[]
    start=dates[k][0]
    end=dates[k][1]
    
    clouds=get_data(bounding_box,resolution,start,end,1,all_bands,0.95)
    (clouds_image,clmask)=clouds.run()
        
    rgb=noclouds_image[:,:,1:4]
    rgb=rgb[:,:,::-1]
    
    rgb2=clouds_image[:,:,1:4]
    rgb2=rgb2[:,:,::-1]
    
    
    plot_image(rgb, factor=3.5/1e4, vmax=1)
    plot_image(rgb2, factor=3.5/1e4, vmax=1)


    
    import pickle
    string="C:/Users/vacla/Documents/data for Cloud-Detection/"
    string=string + df.iloc[k,0] + '_' + 'clouds_snow'
    with open(string, "wb") as fp:   #Pickling
        pickle.dump(save_data_C, fp)
    
    string="C:/Users/vacla/Documents/data for Cloud-Detection/"
    string=string + df.iloc[k,0] + '_' + 'no_clouds_snow'
    
    with open(string, "wb") as fp:   #Pickling
        pickle.dump(save_data_noC, fp)
    
    # with open("test", "rb") as fp:   # Unpickling
    #     b = pickle.load(fp)

print(datetime.now() - startTime)
