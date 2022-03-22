import numpy as np
import pandas as pd
import pickle
import h5py
from sklearn import preprocessing
class load_data2:
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

        self.clouds=np.array(cld)
        self.noclouds=np.array(nocld)
        return (self.clouds,self.noclouds)
