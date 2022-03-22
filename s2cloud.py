
import datetime as dt
import os
import matplotlib.pyplot as plt
import numpy as np

from sentinelhub import SHConfig, BBox, CRS, SentinelHubRequest, DataCollection, \
    MimeType, bbox_to_dimensions

from s2cloudless import S2PixelCloudDetector, CloudMaskRequest, get_s2_evalscript

from plotting_utils import plot_image, plot_probabilities



CLIENT_ID=os.environ.get('SENTINEL_ID')
CLIENT_SECRET=os.environ.get('SENTINEL_SECRET')
config=SHConfig()

if CLIENT_ID and CLIENT_SECRET:
    config.sh_client_id= CLIENT_ID
    config.sh_client_secret = CLIENT_SECRET
    
class s2cloud:
    def __init__(self,bbox,resolution,start_date,end_date):
        self.bbox = bbox
        self.start_date = start_date
        self.end_date = end_date
        self.resolution = resolution
        self.image=None
        self.clm=None
        
    def run(self):
        time_int=(self.start_date,self.end_date)
        a,b,c,d=self.bbox
        bbox=BBox([a,b,c,d], crs=CRS.WGS84)
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
        
        request = SentinelHubRequest(
            evalscript=evalscript_true_color,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L1C,
                    time_interval=time_int
                )
            ],
            responses=[
                SentinelHubRequest.output_response('default', MimeType.PNG)
            ],
            bbox=bbox,
            size=bbox_to_dimensions(bbox, 10),
            config=config
        )
        
        true_color_image = request.get_data()[0]
        
        true_color_image.shape
        
        
        evalscript = get_s2_evalscript(
            all_bands=True,
            reflectance=True
        )
        
        print(evalscript)
        
        request = SentinelHubRequest(
            evalscript=evalscript,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L1C,
                    time_interval=time_int
                )
            ],
            responses=[
                SentinelHubRequest.output_response('default', MimeType.TIFF)
            ],
            bbox=bbox,
            size=bbox_to_dimensions(bbox, 10),
            config=config
        )
        
        data = request.get_data()[0]
        
        bands = data[..., :-1]
        mask = data[..., -1]
        
        cloud_detector = S2PixelCloudDetector(
            threshold=0.4,
            average_over=4,
            dilation_size=2,
            all_bands=True
        )
        cloud_mask = cloud_detector.get_cloud_masks(bands)
        
        return (true_color_image,cloud_mask)