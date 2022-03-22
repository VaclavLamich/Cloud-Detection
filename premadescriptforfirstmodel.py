import numpy 
import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix 
from sklearn.model_selection import train_test_split
from make_cld_mask_single_band import make_cld_mask_single_band
import pickle

###import data

df=pd.read_csv('bboxes_cut.csv')
i=2

string="C:/Users/vacla/Documents/Cloud-Detection/data/"
string=string + df.iloc[i,0] + '_' + 'clouds'
with open(string, "rb") as fp:   # Unpickling
    cld = pickle.load(fp)


string="C:/Users/vacla/Documents/Cloud-Detection/data/"
string=string + df.iloc[i,0] + '_' + 'no_clouds'

###makecld_mask
make_cld_mask=make_cld_mask_single_band(clouds,noclouds)
mask=make_cld_mask.run()

###vectorize data

###split test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#fit model
RndFrst=RandomForestClassifier(n_jobs=2,n_estimators=10)
RndFrst.fit(X_train,y_train) 
#predict
y_pred=RndFrst.predict(X_test)


###metrics
accuracy_score(y_test, y_pred)

confusion_matrix(y_test, y_pred)
