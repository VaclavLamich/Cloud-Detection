from sentinelhub import SHConfig
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt

from sentinelhub import MimeType, CRS, BBox, SentinelHubRequest, SentinelHubDownloadClient, \
    DataCollection, bbox_to_dimensions, DownloadRequest



CLIENT_ID=os.environ.get('SENTINEL_ID')
CLIENT_SECRET=os.environ.get('SENTINEL_SECRET')
config=SHConfig()

if CLIENT_ID and CLIENT_SECRET:
    config.sh_client_id= CLIENT_ID
    config.sh_client_secret = CLIENT_SECRET


class get_image:
    def __init__(self,bbox,resolution,start_date,end_date,clouds,bands,maxcc):
        self.bbox = bbox
        self.start_date = start_date
        self.end_date = end_date
        self.resolution = resolution
        self.clouds = clouds
        self.bands = bands
        self.maxcc=maxcc
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
        evalscript_all_bands = """
            //VERSION=3
            function setup() {
                return {
                    input: [{
                        bands: ["B01","B02","B03","B04","B05","B06","B07","B08","B8A","B09","B10","B11","B12"],
                        units: "DN"
                    }],
                    output: {
                        bands: 13,
                        sampleType: "INT16"
                    }
                };
            }
        
            function evaluatePixel(sample) {
                return [sample.B01, 
                        sample.B02, 
                        sample.B03, 
                        sample.B04, 
                        sample.B05, 
                        sample.B06, 
                        sample.B07, 
                        sample.B08, 
                        sample.B8A, 
                        sample.B09, 
                        sample.B10, 
                        sample.B11, 
                        sample.B12];
            }
        """
        if self.clouds == 0:
            if self.bands ==0:                
                request_true_color = SentinelHubRequest(
                    evalscript=evalscript_all_bands,
                    input_data=[
                        SentinelHubRequest.input_data(
                            data_collection=DataCollection.SENTINEL2_L1C,
                            time_interval=time_int,
                            maxcc=self.maxcc,
                            mosaicking_order='leastCC'
                        )
                    ],
                    responses=[
                        SentinelHubRequest.output_response('default', MimeType.TIFF)
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
                            maxcc=self.maxcc,
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
            if self.bands ==0:                
                request_true_color = SentinelHubRequest(
                    evalscript=evalscript_all_bands,
                    input_data=[
                        SentinelHubRequest.input_data(
                            data_collection=DataCollection.SENTINEL2_L1C,
                            time_interval=time_int,
                            maxcc=self.maxcc
                        )
                    ],
                    responses=[
                        SentinelHubRequest.output_response('default', MimeType.TIFF)
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
                            maxcc=self.maxcc
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