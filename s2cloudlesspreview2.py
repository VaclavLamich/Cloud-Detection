
import datetime as dt
import os
import matplotlib.pyplot as plt
import numpy as np

from sentinelhub import SHConfig, BBox, CRS, SentinelHubRequest, DataCollection, \
    MimeType, bbox_to_dimensions

from s2cloudless import S2PixelCloudDetector, CloudMaskRequest, get_s2_evalscript

def plot_image(image=None, mask=None, ax=None, factor=3.5/255, clip_range=(0, 1), **kwargs):
    """ Utility function for plotting RGB images and masks.
    """
    if ax is None:
        _, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))

    mask_color = [255, 255, 255, 255] if image is None else [255, 255, 0, 100]

    if image is None:
        if mask is None:
            raise ValueError('image or mask should be given')
        image = np.zeros(mask.shape + (3,), dtype=np.uint8)

    ax.imshow(np.clip(image * factor, *clip_range), **kwargs)

    if mask is not None:
        cloud_image = np.zeros((mask.shape[0], mask.shape[1], 4), dtype=np.uint8)

        cloud_image[mask == 1] = np.asarray(mask_color, dtype=np.uint8)

        ax.imshow(cloud_image)


CLIENT_ID=os.environ.get('SENTINEL_ID')
CLIENT_SECRET=os.environ.get('SENTINEL_SECRET')
config=SHConfig()

if CLIENT_ID and CLIENT_SECRET:
    config.sh_client_id= CLIENT_ID
    config.sh_client_secret = CLIENT_SECRET

bbox = BBox([-90.9217, 14.4191, -90.8187, 14.5520], crs=CRS.WGS84)
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
            time_interval='2017-12-01'
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
            time_interval='2017-12-01'
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
plot_image(mask=cloud_mask)
plot_image(image=true_color_image, mask=cloud_mask)