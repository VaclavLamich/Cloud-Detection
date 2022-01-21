## TESTING SCRIPT

from get_image import get_image
from utils import plot_image


##get coordinates here http://bboxfinder.com

a,b,c,d=14.175110,49.824010,14.762878,50.205128
bounding_box=[a,b,c,d]

### parameters of get_image are (bbox,resolution,start_date,end_date,leastClouds(0=yes,1=no))
start="2021-01-01"
end="2022-01-22"

i=get_image(bounding_box,60,start,end,0)
image=i.run()

# plot function
# factor 1/255 to scale between 0-1
# factor 3.5 to increase brightness
plot_image(image, factor=3.5/255, clip_range=(0,1))