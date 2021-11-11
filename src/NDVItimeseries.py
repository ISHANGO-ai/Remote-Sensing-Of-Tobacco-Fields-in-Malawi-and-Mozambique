""" NDVI time series using google earth engine
 using point of interest from land classification map in the model.py for class"""

#from config import args
import ee
import folium
#import geemap
#from folium import plugins
from IPython.display import Image
import geopandas as gpd
#import json
print(folium.__version__)
from ipygee import chart
from ipygee import*
#import math
import pandas as pd
#from tslearn.clustering import TimeSeriesKMeans
#from tslearn.utils import to_time_series_dataset

ee.Initialize()

# we collect te coordinates of our AOI the start and the end date of times series selected
months = ee.List.sequence(1,12)
years = ee.List.sequence(2018, 2019)
POI = ee.Geometry.Point([-122.2769, 37.7435])


# the dataset we use is 8 days ndvi from landsat and we filter with respect to the date and ourAOI
MD_NDVI = ee.ImageCollection('LANDSAT/LC08/C01/T1_8DAY_NDVI').filterDate('2018-1-1','2019-12-31').filterBounds(POI).select('NDVI')
modis_ndvi = MD_NDVI.median().clip(POI)
mean_ndvi = MD_NDVI.mean().clip(POI)


# Let's define a function to return the NDVI monthly medium, generating a time series between January 2018 and Decener 2019
def monthly(collection):
 img_coll = ee.ImageCollection([])
 for y in years.getInfo():
  for m in months.getInfo():
   filtered = collection.filter(ee.Filter.calendarRange(y,y,'year')).filter(ee.Filter.calendarRange(m, m, 'month'))
   filtered = filtered.median()
   img_coll = img_coll.merge(filtered.set('year', y).set('month', m).set('system:time_start',ee.Date.fromYMD(y, m, 1).getInfo()['value']))
 return img_coll
Monthly_MD = monthly(MD_NDVI)


# we use ipygee to generate a chart of the NDVI variation in the analysis period for any point in the AOI(bare land)
Point_1 = ee.Geometry.Point([-122.2776, 37.8181])
MD_ndvi = chart.Image.series(**{'imageCollection': Monthly_MD,
'region': Point_1,
'reducer': ee.Reducer.mean(),
'scale': 250,
'xProperty': 'system:time_start'})
MD_ndvi.renderWidget(width='80%')


# we use ipygee to generate a chart of the NDVI variation in the analysis period for any point in the AOI(vegetation)
Point_1 = ee.Geometry.Point([-122.5118, 37.8438])
MD_ndvi = chart.Image.series(**{'imageCollection': Monthly_MD,
'region': Point_1,
'reducer': ee.Reducer.mean(),
'scale': 500,
'xProperty': 'system:time_start'})
MD_ndvi.renderWidget(width='200%')




# we use ipygee to generate a chart of the NDVI variation in the analysis period for any point in the AOI(water)
Point_1 = ee.Geometry.Point([-122.2769, 37.7435])
MD_ndvi = chart.Image.series(**{'imageCollection': Monthly_MD,
'region': Point_1,
'reducer': ee.Reducer.mean(),
'scale': 250,
'xProperty': 'system:time_start'})
MD_ndvi.renderWidget(width='80%')


