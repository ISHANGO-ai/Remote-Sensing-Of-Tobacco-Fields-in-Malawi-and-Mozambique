import matplotlib
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


ep.plot_bands(arr_st, 
              cmap = 'gist_earth', 
              figsize = (20, 12), 
              cols = 8, 
              cbar = False)
plt.show()