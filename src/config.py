""" Add all configuratins
add all arguments """
import argparse



args = argparse.Namespace(
    
    # started date
    start_date = '2018/08/25',
    # ended date
    end_date = '2020/08/25',
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
    # latitude of mozambique
    # latitude = -18.665695, 
    latitude = -18.665695,
    # longitude  of mozambique 
    #longitude = 35.529562,
    longitude = 35.529562,
    # your username
    username = "username",
    # your password
    password = "password",
    # geojson file
    geojson_file = "tete.geojson",
    #name of product of landsat data
    product = 'landsat_tm_c1' ,


)