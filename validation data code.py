import h5py 
import pandas as pd
import numpy as np

with h5py.File('C:/Users/vacla/Documents/data for Cloud-Detection/20160914_s2_manual_classification_data.h5','r') as hdf:
    ls=list(hdf.keys())
#    print('List of data',ls)
    data=hdf.get('country')
    data1=hdf.get('classes')
    data2=hdf.get('class_ids')
    data3=hdf.get('class_names')
    data4=hdf.get('spectra')
    data5=hdf.get('band')
    band=np.array(data5)
    country=np.array(data)
    classes=np.array(data1)
    class_ids=np.array(data2)
    class_names=np.array(data3)
    spectra=np.array(data4)
    data5=np.array(data5)
    
#Pixels=np.array([spectra[:,0],spectra[:,1],spectra[:,2],spectra[:,3],spectra[:,7],spectra[:,10],spectra[:,11],spectra[:,12],classes])
Pixels=np.array(spectra[:,1])

Pixels=np.transpose(Pixels)
Ger=np.where((country==b'Germany'))
# #b=np.where((country==b'Germany')|(country==b'France')|(country==b'Greece')|(country==b'Georgia')|(country==b'Iceland')|(country==b'Spain')|(country==b'UK'))
Ger=np.array(Ger)
Ger=Pixels[np.array(Ger)]
Ger=Ger[0,:,:]
Ger[Ger==40]=1
Ger[Ger==50]=1
Ger[Ger==10]=0
Ger[Ger==20]=0
Ger[Ger==30]=0
Ger[Ger==60]=0
# Pixels[Pixels==40]=1
# Pixels[Pixels==50]=1
# Pixels[Pixels==10]=0
# Pixels[Pixels==20]=0
# Pixels[Pixels==30]=0
# Pixels[Pixels==60]=0

y_val_g=Ger[:,8]
# x_val_multi_g=Ger[:,0:8:1]
x_val_b2_g=Ger[:,1]