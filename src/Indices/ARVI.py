"""" the Atmospherically Resistant Vegetation Index is the first vegetation index, which is notrelatively prone
 to atmospheric factors (such as aerosol) """
#

# we collect te coordinates of our AOI the start and the end date of times serisies selected

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
def arvi_sentinel(band):


    arvi = ((band[3] - (2*band[2])+band[0]))/((band[3]+(2*band[2])+band[0]))
    
    return arvi


ARVI =arvi_sentinel(arr_st)

ep.plot_bands(ARVI, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14),title = 'Sentinel2A - ARVI') 

plt.show()
