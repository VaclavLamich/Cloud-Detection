import numpy as np
from make_cld_mask_single_band import make_cld_mask_single_band
from load_data import load_data
from sklearn import preprocessing

class transform_data:
    def __init__(self,indexes,bands):
        self.indexes = indexes
        self.bands=bands
        self.X=None
        self.y=None
        
    def run(self):
        cld_pics=[]
        masks=[]
        for k in self.indexes:
            
            load=load_data()
            (cld,nocld)=load.run(k)
            cld_pics.append(cld)
            
            make_cld_mask=make_cld_mask_single_band(cld,nocld,1)
            mask=make_cld_mask.run()
            mc=mask
            mc[mc<900]=0
            mc[mc>=900]=1
            masks.append(mc)

        X=np.empty(0)
        y=np.empty(0)
        for i in range(len(cld_pics)):
            clds=np.reshape(cld_pics[i][:,:,self.bands],(cld_pics[i].shape[0]*cld_pics[i].shape[1]))
            X=np.concatenate((X,clds))
            msks=np.reshape(masks[i][:,:],(masks[i].shape[0]*masks[i].shape[1]))
            y=np.concatenate((y,msks))
            
        self.X=preprocessing.scale(X)
        self.y=y
        return(self.X,self.y)
        