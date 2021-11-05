"""the visible atmospheric resistant index(VARI) is designed to emphasize vegetetation in the visible portion
 of the spectrum  while mitigating illimunatio differences and atmspheric effects"""

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

def vari_sentinel (arr_st):

    vari = (arr_st[1] - arr_st[2])/(arr_st[1]+ arr_st[2] - arr_st[0])

    return vari
VARI = vari_sentinel(arr_st)
ep.plot_bands(VARI, cmap="RdYlGn", cols=2, vmin=-1, vmax=1, figsize= (10,14),title= 'VARI')
plt.show()