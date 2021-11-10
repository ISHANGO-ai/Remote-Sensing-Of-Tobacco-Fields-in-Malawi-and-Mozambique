

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
input_dir = input('Enter path+')
S_sentinel_bands = glob(input_dir + '/*B?*.jp2')

S_sentinel_bands.sort()

l = []

for i in S_sentinel_bands:

    with rio.open(i, 'r') as f:
        l.append(f.read(1))

arr_st = np.stack(l)
#RGB composite image with strech
ep.plot_rgb(arr_st,rgb=(2,1,0),
stretch=True,
str_clip=0.2,
figsize=(10,16))
plt.show()