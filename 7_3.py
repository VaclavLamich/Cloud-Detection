import numpy as np
import pandas as pd
from utils import plot_image
import pickle
from make_cld_mask_single_band import make_cld_mask_single_band
from load_data import load_data
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from datetime import datetime

startTime = datetime.now()



indexes=[0,1,2,8,9,10,12,19,22,23]
#for k in indexes:
load=load_data(23)
(cld,nocld)=load.run()
make_cld_mask=make_cld_mask_single_band(cld,nocld,1)
mask=make_cld_mask.run()

plot_image(mask, factor=3.5/1e4, vmax=1)
mc=mask
mc[mc<900]=0
mc[mc>=900]=1
plot_image(mc)

X=np.reshape(cld[:,:,1],(cld.shape[0]*cld.shape[1],1))
y=np.reshape(mc,(mc.shape[0]*mc.shape[1],1))
X=preprocessing.scale(X)

###split test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#fit model
RndFrst=RandomForestClassifier(n_jobs=2,n_estimators=100)
RndFrst.fit(X_train,y_train) 
#predict
y_pred=RndFrst.predict(X_test)


###metrics
acc=accuracy_score(y_test, y_pred)

con=confusion_matrix(y_test, y_pred)

###validation
(X_val,y_val)=load.load_validation(1)
y_pred_val=RndFrst.predict(X_val)

acc1=accuracy_score(y_val, y_pred_val)

con1=confusion_matrix(y_val, y_pred_val)

print(acc)
print(acc1)
print(con)
print(con1)
print(datetime.now() - startTime)
