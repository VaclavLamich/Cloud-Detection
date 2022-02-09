import numpy as np

from sentinelhub import BBox, bbox_to_dimensions,CRS


class resolution_image:
    def __init__(self,bbox,resolution):
        self.bbox = bbox
        self.resolution = resolution
        self.size=None
        
    def run(self):
        our_bbox = list(np.round(self.bbox,2))
        our_bbox = BBox(bbox=our_bbox, crs=CRS.WGS84)
        self.size = bbox_to_dimensions(our_bbox, resolution=self.resolution)
        return self.size