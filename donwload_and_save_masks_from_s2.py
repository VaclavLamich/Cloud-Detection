import numpy as np
import pandas as pd
from utils import plot_image
from check_inds import check_inds
from load_data import load_data

from load_data2 import load_data2
from load_data_summer import load_data_summer
import pickle
from datetime import datetime
from s2cloudless import S2PixelCloudDetector
from sklearn import preprocessing
from plotting_utils import plot_image, plot_probabilities
from s2cloud import s2cloud


startTime = datetime.now()
indexes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
inds=check_inds(indexes)
a=inds.run()

df=pd.read_csv('bboxes_cut.csv')
resolution=10
masks_from_s2cloud=[]
true_color_images_s2=[]
for k in a[1]:

    load=load_data_summer()
    (cld,nocld)=load.run(k)
    start=cld[0][1]
    end=cld[0][2]
    bounding_box=[df.iloc[k,1],df.iloc[k,2],df.iloc[k,3],df.iloc[k,4]]

    s2=s2cloud(bounding_box,resolution,start,end)

    (true_color_image,cloud_mask)=s2.run()
    masks_from_s2cloud.append(cloud_mask)    
    true_color_images_s2.append(true_color_image)    
    plot_image(mask=cloud_mask)
    plot_image(image=true_color_image, mask=cloud_mask)
    print(datetime.now() - startTime)




string="C:/Users/vacla/Documents/data for Cloud-Detection/"
string=string +'cloud_masks_summer'
with open(string, "wb") as fp:   #Pickling
    pickle.dump(masks_from_s2cloud, fp)

string="C:/Users/vacla/Documents/data for Cloud-Detection/"
string=string +'true_color_images_s2_summer'
with open(string, "wb") as fp:   #Pickling
    pickle.dump(true_color_images_s2, fp)
