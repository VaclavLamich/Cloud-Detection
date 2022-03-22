import numpy as np
import pandas as pd
from utils import plot_image
from check_inds import check_inds
from load_data import load_data

from load_data2 import load_data2
import pickle
from datetime import datetime
from s2cloudless import S2PixelCloudDetector
from sklearn import preprocessing
from plotting_utils import plot_image, plot_probabilities
from s2cloud import s2cloud


indexes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]

inds=check_inds(indexes)
a=inds.run()



cld_pics=[]
no_cld_pics=[]
masks=[]
date_diff=[]
# for k in a[0]:
#     load=load_data2()
#     (cld,nocld)=load.run(k)
    
#     d1 = datetime.strptime(cld[0][2], '%Y-%m-%d')
#     d2= datetime.strptime(nocld[0][2], '%Y-%m-%d')
#     d=np.abs(d1-d2)
#     date_diff.append(d.days)
#     cld_pics.append(cld[0][0])
#     no_cld_pics.append(nocld[0][0])
# # for i in range(len(cld_pics)):
#     cld=cld_pics[i]
#     no_cld=no_cld_pics[i]
#     sub=no_cld[:,:,2]-cld[:,:,2]
    
    # rgb=no_cld[:,:,1:4]
    # rgb=rgb[:,:,::-1]
    
    # rgb2=cld[:,:,1:4]
    # rgb2=rgb2[:,:,::-1]
    
    
    # plot_image(rgb, factor=3.5/1e4, vmax=1)
    # plot_image(rgb2, factor=3.5/1e4, vmax=1)

    # #plot_image(cld[:,:,1],factor=3/1e4, vmax=1)
    # plot_image(sub, factor=3/1e4, vmax=1)


startTime = datetime.now()
df=pd.read_csv('bboxes_cut.csv')
resolution=10
k=list(a[0])[0]
load=load_data2()
(cld,nocld)=load.run(k)
start=cld[0][1]
end=cld[0][2]
bounding_box=[df.iloc[k,1],df.iloc[k,2],df.iloc[k,3],df.iloc[k,4]]

s2=s2cloud(bounding_box,resolution,start,end)

(true_color_image,cloud_mask)=s2.run()

plot_image(mask=cloud_mask)
plot_image(image=true_color_image, mask=cloud_mask)
print(datetime.now() - startTime)
#PLOT ALL BANDS AND THEIR SUBTRACTIONS
# sub_save=[]
# m=0
# for i in range(13):
#     cld=cld_pics[m]
#     no_cld=no_cld_pics[m]
#     sub=cld[:,:,i]-no_cld[:,:,i]
#     sub_save.append(sub)
#     plot_image(no_cld[:,:,i])
#     plot_image(cld[:,:,i])
#     plot_image(sub)
# rgb=no_cld[:,:,1:4]
# rgb=rgb[:,:,::-1]

# rgb2=cld[:,:,1:4]
# rgb2=rgb2[:,:,::-1]


# plot_image(rgb)
# plot_image(rgb2)







##
# b2a=c[:,:,1]
# b2=noc[:,:,1]
# b2a_v=np.reshape(b2a,(1,b2a.shape[0]*b2a.shape[1]),order='F')
# b2_v=np.reshape(b2,(1,b2.shape[0]*b2.shape[1]),order='F')
# suma1=0
# suma2=0
# for i in range(len(b2a_v[0])):
#     suma1=suma1+b2a_v[0][i]*b2_v[0][i]
# for i in range(len(b2a_v[0])):
#     suma2=suma2+b2_v[0][i]*b2_v[0][i]
# k2=0
# k2=suma1/suma2
# k2

# B2a=np.abs(b2a-k2*b2)
# plot_image(B2a, factor=3.5/1e4, vmax=1)