""""  The Structure Insensitive Pigment Index is good for analysis of vegetation with the variable canopy structure. 
It estimates the ratio of carotenoids to chlorophyll"""
#

# we collect te coordinates of our AOI the start and the end date of times serisies selected

import glob
import numpy as np
# from osgeo import gdal # If GDAL doesn't recognize jp2 format, check version</pre>
from glob import glob
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio as rio
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import plotly.graph_objects as go
from math import*
#from config import args

np.seterr(divide='ignore', invalid='ignore')
# Set input directory
input_dir = input('Enter path')
S_sentinel_bands = glob(input_dir + '/*B?*.jp2')

S_sentinel_bands.sort()

l = []

for i in S_sentinel_bands:
    #

    # we collect te coordinates of our AOI the start and the end date of times serisies selected
    with rio.open(i, 'r') as f:
        l.append(f.read(1))

arr_st = np.stack(l)


def sipi_sentinel(band):

    sipi = (band[3]-band[1]) / (band[3] -band[2])

    return sipi


SIPI = sipi_sentinel(arr_st)

ep.plot_bands(SIPI, cmap="RdYlGn", cols=1, vmin=-1, vmax=1,
              figsize=(10, 14), title='Sentinel2A - SIPI')

plt.show()