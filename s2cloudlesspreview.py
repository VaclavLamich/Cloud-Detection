
from s2cloudless import S2PixelCloudDetector
from plotting_utils import plot_image, plot_probabilities
#  needed bands ["B01", "B02", "B04", "B05", "B08", "B8A", "B09", "B10", "B11", "B12", "dataMask"], units: "reflectance"
      

###an specify the following arguments in the initialization of a S2PixelCloudDetector:

   # threshold - cloud probability threshold value. All pixels with cloud probability above threshold value are masked as cloudy pixels. Default is 0.4.
    #average_over - Size of the disk in pixels for performing convolution (averaging probability over pixels). For this resolution 4 is appropriate.
   # dilation_size - Size of the disk in pixels for performing dilation. For this resolution 2 is appropriate.
    #all_bands - Flag specifying that input images will consists of all 13 Sentinel-2 bands. It has to be set to True if we would download all bands. If you define a layer that would return only 10 bands, then this parameter should be set to False.

cloud_detector = S2PixelCloudDetector(
threshold=0.4,
average_over=4,
dilation_size=2,
all_bands=False
)

cloud_prob = cloud_detector.get_cloud_probability_maps(bands)
cloud_mask = cloud_detector.get_cloud_masks(bands)

plot_probabilities(true_color_image, cloud_prob)
plot_image(mask=cloud_mask)
plot_image(image=true_color_image, mask=cloud_mask)
