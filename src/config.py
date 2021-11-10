""" Add all configuratins
add all arguments """
import argparse



args = argparse.Namespace(
    
    # started date
    start_date = '19950101',
    # ended date
    end_date = '19951001',
    # name of the plateform
    platformname = 'Sentinel-2',
    # The level of the processing
    processinglevel = 'Level-2A',
    # set the interval of cloud cover
    #orbit direction
    orbitdirection = 'DESCENDING',
    cloudcoverpercentage = (0,100),
    # set the threshold of cloud cover
    cloud_max = 30,
    # latitude of tete in mozambique
    # latitude = -16.1328104, 
    latitude = -16.1328104,
    # longitude  of tete in mozambique 
    #longitude = 35.529562,
    longitude = 33.6063855,
    # your username
    username = "username",
    # your password
    password = "password",
    # geojson file
    footprint= "/home/jannette/Videos/Remote-Sensing-Of-Tobacco-Fields-in-Malawi-and-Mozambique/data/tete.geojson",
    #name of product of landsat data
    product = 'landsat_tm_c1' ,
    query_style = ' footprint',#geojson file, coordinates


)