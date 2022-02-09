## TESTING SCRIPT

from get_image import get_image
from utils import plot_image


##get coordinates here http://bboxfinder.com
## sentinel tiles https://eatlas.org.au/data/uuid/f7468d15-12be-4e3f-a246-b2882a324f59
### https://maps.eatlas.org.au/index.html?intro=false&z=7&ll=146.90137,-19.07287&l0=ea_ref%3AWorld_ESA_Sentinel-2-tiling-grid_Poly,ea_ea-be%3AWorld_Bright-Earth-e-Atlas-basemap,google_HYBRID,google_TERRAIN,google_SATELLITE,google_ROADMAP&v0=,,f,f,f,f&_ga=2.241250753.217313.1644409772-1220123883.1644409772

#a,b,c,d=14.175110,49.824010,14.762878,50.205128
a,b,c,d=14.361499,50.007739,14.605896,50.118817
bounding_box=[a,b,c,d]

### parameters of get_image are 
#(bbox,resolution,start_date,end_date,leastClouds(0=yes,1=no),all_bands(0=yes, 1=no),maxcc=(float 0-1))
start="2021-01-01"
end="2022-01-22"

i=get_image(bounding_box,10,start,end,1,1,0.5)
image=i.run()

# plot function
# factor 1/255 to scale between 0-1
# factor 3.5 to increase brightness

plot_image(image, factor=3.5/255, clip_range=(0,1))

#plot_image(all_bands_response[0][:, :, 12], factor=3.5/1e4, vmax=1)