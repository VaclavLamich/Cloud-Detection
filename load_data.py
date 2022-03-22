import numpy as np
import pandas as pd
import pickle
import h5py
from sklearn import preprocessing
class load_data:
    def __init__(self):
        self.clouds=None
        self.noclouds=None
        
    def run(self,index):
        self.index = index
        df=pd.read_csv('bboxes_cut.csv')
        string="C:/Users/vacla/Documents/data for Cloud-Detection/"
        string=string + df.iloc[self.index,0] + '_' + 'clouds'
        with open(string, "rb") as fp:   # Unpickling
            cld = pickle.load(fp)
            
        string="C:/Users/vacla/Documents/data for Cloud-Detection/"
        string=string + df.iloc[self.index,0] + '_' + 'no_clouds'
    
        with open(string, "rb") as fp:   # Unpickling
            nocld = pickle.load(fp)

        self.clouds=np.array(cld[0][0])
        self.noclouds=np.array(nocld[0][0])
        return (self.clouds,self.noclouds)
    
    def load_validation(self,bands):
        self.bands=bands
        self.X_val=None
        self.y_val=None

        with h5py.File('C:/Users/vacla/Documents/data for Cloud-Detection/20160914_s2_manual_classification_data.h5','r') as hdf:
            ls=list(hdf.keys())
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
        
        c=np.reshape(classes,(classes.shape[0],1))
        if type(self.bands)==int:
            b=np.reshape(spectra[:,self.bands],(spectra.shape[0],1))
            Pixels=np.concatenate((b,c),axis=1)
        else:
            Pixels=np.concatenate((spectra[:,self.bands],c),axis=1)
        
        #Ger=np.where((country==b'Germany')|(country==b'France')|(country==b'Greece')|(country==b'Georgia')|(country==b'Iceland')|(country==b'Spain')|(country==b'UK'))
        #Ger=np.where((country==b'Germany')|(country==b'France')|(country==b'Georgia')|(country==b'UK'))
        Ger=np.where((country==b'Germany'))
        Ger=np.array(Ger)
        Ger=Pixels[np.array(Ger)]
        Ger=Ger[0,:,:]
        a=np.where(Ger[:,1]==20)
        b=np.where(Ger[:,1]==60)
        a=np.concatenate([a[0],b[0]])
        Ger=np.delete(Ger, a,0)
        Ger[Ger==40]=1
        Ger[Ger==50]=1
        Ger[Ger==10]=0
        #Ger[Ger==20]=0
        Ger[Ger==30]=0
        #Ger[Ger==60]=0
        self.y_val=Ger[:,-1]
        self.X_val=preprocessing.scale(Ger[:,:-1])
        return (self.X_val,self.y_val)
