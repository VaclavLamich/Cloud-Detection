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
from transform_data import transform_data

startTime = datetime.now()

indexes=[0,2,9,10,19,23] #ok mask
#indexes=[0,1,2,8,9,10,12,19,22,23]
transform=transform_data(indexes,1)

(X,y)=transform.run()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

X_train=np.reshape(X_train,(X_train.shape[0],1))
X_test=np.reshape(X_test,(X_test.shape[0],1))
y_train=np.reshape(y_train,(y_train.shape[0],1))
y_test=np.reshape(y_test,(y_test.shape[0],1))
#fit model
RndFrst=RandomForestClassifier(n_jobs=2,n_estimators=10)
RndFrst.fit(X_train,y_train) 
#predict
y_pred=RndFrst.predict(X_test)


###metrics
acc=accuracy_score(y_test, y_pred)

con=confusion_matrix(y_test, y_pred)

###validation
load=load_data()
(X_val,y_val)=load.load_validation(1)
y_pred_val=RndFrst.predict(X_val)

acc1=accuracy_score(y_val, y_pred_val)

con1=confusion_matrix(y_val, y_pred_val)

print(acc)
print(acc1)
print(con)
print(con1)
print(datetime.now() - startTime)
