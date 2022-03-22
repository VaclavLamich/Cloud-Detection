import numpy as np
import pandas as pd

class make_cld_mask_single_band:
    def __init__(self,clouds,no_clouds,band):
        self.clouds = clouds
        self.no_clouds = no_clouds
        self.band=band
        self.cld_mask=None
        
    def run(self):
        
        b2a=self.clouds[:,:,self.band]
        b2=self.no_clouds[:,:,self.band]
        b2a_v=np.reshape(b2a,(1,b2a.shape[0]*b2a.shape[1]),order='F')
        b2_v=np.reshape(b2,(1,b2.shape[0]*b2.shape[1]),order='F')
        suma1=0
        suma2=0
        for i in range(len(b2a_v[0])):
            suma1=suma1+b2a_v[0][i]*b2_v[0][i]
        for i in range(len(b2a_v[0])):
            suma2=suma2+b2_v[0][i]*b2_v[0][i]
        k2=0
        k2=suma1/suma2
        k2
        
        self.cld_mask=np.abs(b2a-k2*b2)
        return self.cld_mask