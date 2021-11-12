"""  The NDWI results from the following equation: Index = (NIR - MIR) / (NIR + MIR) using Sentinel-2 Band 8 (NIR) and Band 12 (MIR). 
The NDWI is a vegetation index sensitive to the water content of vegetation and is complementary to the NDVI. 
High NDWI values show a high water content of the vegetation. """

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
#from .config import args

np.seterr(divide='ignore', invalid='ignore')
# Set input directory
input_dir = input('Enter path')
S_sentinel_bands = glob(input_dir +'/*B?*.jp2' )

S_sentinel_bands.sort()

l = []

for i in S_sentinel_bands:

    with rio.open(i, 'r') as f:
        l.append(f.read(1))

arr_st = np.stack(l)

def ndwi_sentinel (arr_st):

    ndwi = (arr_st[1] - arr_st[3])/(arr_st[1]+ arr_st[3])

    return ndwi
NDWI = ndwi_sentinel(arr_st)
ep.plot_bands(NDWI, cmap="RdYlGn", cols=2, vmin=-1, vmax=1, figsize= (10,14),title= 'NDWI')
plt.show()