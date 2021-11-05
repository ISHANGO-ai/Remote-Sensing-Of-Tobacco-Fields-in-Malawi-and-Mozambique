"""" NDVI measures the difference between visible and near-infrared (NIR) light reflectance from vegetation to create
 a snapshot of photosynthetic vigor  """


import glob
import numpy as np
#from osgeo import gdal # If GDAL doesn't recognize jp2 format, check version</pre>
from glob import glob
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio as rio
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import plotly.graph_objects as go
from .config import args

np.seterr(divide='ignore', invalid='ignore')
# Set input directory
input_dir = input('Enter path+/*B?*.jp2')
S_sentinel_bands = glob(input_dir)

S_sentinel_bands.sort()

l = []

for i in S_sentinel_bands:

    with rio.open(i, 'r') as f:
        l.append(f.read(1))

arr_st = np.stack(l)
def ndvi_sentinel(arr_st):

    ndvi = (arr_st[3] - arr_st[2])/(arr_st[3]+arr_st[2])
    
    return ndvi


NDVI =ndvi_sentinel(arr_st)

ep.plot_bands(NDVI, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14),title = 'Sentinel2A - Normalized Difference Vegetation Index (NDVI)') 

plt.show()
