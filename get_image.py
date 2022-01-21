from sentinelhub import SHConfig
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt

from sentinelhub import MimeType, CRS, BBox, SentinelHubRequest, SentinelHubDownloadClient, \
    DataCollection, bbox_to_dimensions, DownloadRequest




#CLIENT_ID='39d016f7-af27-47d4-851c-2d7e7789f52d'
#CLIENT_SECRET='.z~uuD8vM[;.GO&)EjHDLC>()T1RR<vnhE[]F!tE'
CLIENT_ID=os.environ.get('SENTINEL_ID')
CLIENT_SECRET=os.environ.get('SENTINEL_SECRET')
config=SHConfig()

if CLIENT_ID and CLIENT_SECRET:
    config.sh_client_id= CLIENT_ID
    config.sh_client_secret = CLIENT_SECRET


class get_image:
    def __init__(self,bbox,resolution,start_date,end_date,clouds):
        self.bbox = bbox
        self.start_date = start_date
        self.end_date = end_date
        self.resolution = resolution
        self.clouds = clouds
        self.image=None
        
    def run(self):
        our_bbox = list(np.round(self.bbox,2))
        our_bbox = BBox(bbox=our_bbox, crs=CRS.WGS84)
        our_size = bbox_to_dimensions(our_bbox, resolution=self.resolution)
        time_int=(self.start_date,self.end_date)
        evalscript_true_color = """
            //VERSION=3
        
            function setup() {
                return {
                    input: [{
                        bands: ["B02", "B03", "B04"]
                    }],
                    output: {
                        bands: 3
                    }
                };
            }
        
            function evaluatePixel(sample) {
                return [sample.B04, sample.B03, sample.B02];
            }
        """
        if self.clouds == 0:
            request_true_color = SentinelHubRequest(
                evalscript=evalscript_true_color,
                input_data=[
                    SentinelHubRequest.input_data(
                        data_collection=DataCollection.SENTINEL2_L1C,
                        time_interval=time_int,
                        mosaicking_order='leastCC'
                    )
                ],
                responses=[
                    SentinelHubRequest.output_response('default', MimeType.PNG)
                ],
                bbox=our_bbox,
                size=our_size,
                config=config
            )
        else:
            request_true_color = SentinelHubRequest(
                evalscript=evalscript_true_color,
                input_data=[
                    SentinelHubRequest.input_data(
                        data_collection=DataCollection.SENTINEL2_L1C,
                        time_interval=time_int,
                    )
                ],
                responses=[
                    SentinelHubRequest.output_response('default', MimeType.PNG)
                ],
                bbox=our_bbox,
                size=our_size,
                config=config
            )
        
        self.image=request_true_color.get_data()[0]
        return self.image