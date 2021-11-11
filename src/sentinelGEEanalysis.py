""" The visualization of sentinel2 using google earth engine
 to display NDVI map for the area of interest. """

#We import the necessary packages
import geemap
import ee
#from config import args
def sentinel_data():
    # We define our inputs
    start_date= str(input('Enter_start_date_yy-mm-dd'))
    end_date=str(input('Enter_end_date_yy-mm-dd'))
    longitude= float(input('Enter_longitude'))
    latitude = float(input('Enter_latitude'))
    #Earth engine authentication
    ee.Authenticate()
    ee.Initialize()
    #We generate a map and center it on our lat and lon
    Map = geemap.Map(center=[latitude,longitude], zoom=9)
    #We enter the lat and loin of the point of interest
    point=ee.Geometry.Point(longitude,latitude)
    #Mapoint=ee.Geometry.Point(latitude,longitude)
    #We import dataset from sentinel 2 using earth engine api and we clip our poi, filter by date and sort according to cloud coverage
    data= ee.ImageCollection("COPERNICUS/S2").filterBounds(point);
    image1=ee.Image(data.filterDate(start_date, end_date).sort("CLOUD_COVERAGE_ASSESSMENT").first());
    #From the first data we selects the bands to generate the ndvi
    ndvi=image1.expression("(NIR - RED) / (NIR + RED)",
    {"NIR":image1.select("B8"),
    "RED":image1.select("B4")});
    display={
    "min":0,
    "max":1,
    "palette":[ 'blue', 'yellow', 'green', 'darkgreen','black']}
    #We display the ndvi
    Map.addLayer(ndvi,display);
    #Map
    
    #We now select the bands to compute the true colour map
    image2= ee.ImageCollection("COPERNICUS/S2").filterBounds(point).filterDate('2016-01-01', '2019-04-30').sort('CLOUDY_PIXEL_PERCENTAGE', False).mosaic()
    truecolor= {'Bands':['B8', 'B4', 'B3'], 'min':0, 'max':3000}
    Map.addLayer(image2, truecolor, 'True Color Composite')
    #We display the true color map on the same map with a layer control
    Map.addLayerControl()

    #Map
    return Map

sentinel_data()