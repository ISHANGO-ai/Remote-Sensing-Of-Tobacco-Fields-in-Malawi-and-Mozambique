""" Add all configuratins
add all arguments """
import argparse



args = argparse.Namespace(
    
    # started date
    start_date = 'start_date',
    # ended date
    end_date = 'end_date',
    # name of the plateform
    platformname = 'Sentinel-2',
    # The level of the processing
    processinglevel = 'Level-2A',
    # set the interval of cloud cover
    #orbit direction
    orbitdirection = 'DESCENDING',
    cloudcoverpercentage = (0,100),
    # set the threshold of cloud cover
    threshold_cloudcover = 10,
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
    geojson_file = "tete.geojson",
    #name of product of landsat data
    product = 'landsat_tm_c1' ,


)