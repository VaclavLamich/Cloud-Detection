from resolution import resolution_image
import numpy as np
import pandas as pd

a,b,c,d=14,50,14.34,50.22
bounding_box=[a,b,c,d]
max_sirka=0.2
max_delka=0.3
i=resolution_image(bounding_box,10)
image=i.run()
print(image)

df=pd.read_csv('bboxes.csv')
