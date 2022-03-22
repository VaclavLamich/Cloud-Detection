import numpy as np
import pandas as pd
import pickle
import h5py
from sklearn import preprocessing
class check_inds:
    def __init__(self,index):
        self.index = index
        good_inds=None
        
    def run(self):
        df=pd.read_csv('bboxes_cut.csv')
        df1=pd.read_csv('bbox_snow2.csv')
        
        not_in_directory=[]
        not_in_directory_snow=[]
        not_in_directory_summer=[]
        
        for i in self.index:
            try:
                string="C:/Users/vacla/Documents/data for Cloud-Detection/"
                string=string + df.iloc[i,0] + '_' + 'clouds'
                with open(string, "rb") as fp:   # Unpickling
                    g=1+1
                    
                string="C:/Users/vacla/Documents/data for Cloud-Detection/"
                string=string + df.iloc[i,0] + '_' + 'no_clouds'
            
                with open(string, "rb") as fp:   # Unpickling
                    g=1+1
            except:
                not_in_directory.append(i)
            try:
                string="C:/Users/vacla/Documents/data for Cloud-Detection/"
                string=string + df1.iloc[i,0] + '_' + 'clouds'+'_snow'
                with open(string, "rb") as fp:   # Unpickling
                    g=1+1
                    
                string="C:/Users/vacla/Documents/data for Cloud-Detection/"
                string=string + df1.iloc[i,0] + '_' + 'no_clouds'+'_snow'
            
                with open(string, "rb") as fp:   # Unpickling
                    g=1+1
            except:
                not_in_directory_snow.append(i)
            try:
                string="C:/Users/vacla/Documents/data for Cloud-Detection/"
                string=string + df.iloc[i,0] + '_' + 'clouds'+'_summer'
                with open(string, "rb") as fp:   # Unpickling
                    g=1+1
                    
                string="C:/Users/vacla/Documents/data for Cloud-Detection/"
                string=string + df.iloc[i,0] + '_' + 'no_clouds'+'_summer'
            
                with open(string, "rb") as fp:   # Unpickling
                    g=1+1
            except:
                not_in_directory_summer.append(i)
                
        a=set(self.index)-set(not_in_directory)
        b=set(self.index)-set(not_in_directory_snow)
        c=set(self.index)-set(not_in_directory_summer)
        good_inds=(a,b,c)
        return good_inds