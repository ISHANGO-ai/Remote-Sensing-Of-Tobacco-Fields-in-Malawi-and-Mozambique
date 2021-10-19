#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import datetime
import gc
import glob
import geopandas
import random
from sentinelsat import SentinelAPI, geojson_to_wkt, read_geojson

class sentinel1_download_preprocess():
    def __init__(self,username,password,date_1,date_2,query_style,footprint,lat,lon,download):
        self.username = username
        self.password = password
        self.date_start = datetime.datetime.strptime(date_1, "%Y/%m/%d")
        self.date_end = datetime.datetime.strptime(date_2, "%Y/%m/%d")
        self.query_style = query_style
        self.footprint = geojson_to_wkt(read_geojson(footprint))
        self.lat = lat
        self.lon = lon
        self.download = download # you want to download, the default is False, but if you want to continue to download preocess is "True"
            # configurations
        self.api = SentinelAPI(username, password, 'https://scihub.copernicus.eu/dhus')
        self.platformname ='Sentinel-2'# sentinel1-1,sentine-2,sentinel-3,sentinel-5P
        self.orbitdirection = 'DESCENDING'  # ASCENDING, DESCENDING
        self.processinglevel = 'Level-2A'#L-2A,L-1C
        self.cloudcoverpercentage = (0,30)# better high %
        
    @classmethod
    def parameters(cls):#fucntions of input required parameters
        username = input(' Enter username:')
        password = input('Enter password:')
        date_1 = input('Startdate yyyy/mm/dd:') #start_date
        date_2 = input('Enddate yyyy/mm/dd:') #end_date
        query_style = input('query_style:') #footprint or coordinates
        
        lat = None
        lon = None
        footprint = None
        if query_style == 'coordinate':
            lat = input('latitude:')
            lon = input('longitude:')
        elif query_style == 'footprint':
            footprint = input('"Enter path_geoson_file:') #path where geojson file is stored,
        else:
            assert "Define query attribute"          

        download = input('download:') #True or False
            
        return cls(username, password, date_1, date_2, query_style, footprint, lat, lon, download)


    def sentinel1_download(self):
        global download_candidate
        if self.query_style == 'coordinate': #coordinates
            download_candidate = self.api.query('POINT({0} {1})'.format(self.lon, self.lat),
                                                date=(self.date_start, self.date_end),
                                                platformname=self.platformname,
                                                orbitdirection=self.orbitdirection,
                                                processinglevel=self.processinglevel,
                                                cloudcoverpercentage=self.cloudcoverpercentage)
        elif self.query_style == 'footprint': # geojson file
            download_candidate = self.api.query(self.footprint,
                                                 date=(self.date_start, self.date_end),
                                                platformname=self.platformname,
                                                orbitdirection=self.orbitdirection,
                                                processinglevel=self.processinglevel,
                                                cloudcoverpercentage=self.cloudcoverpercentage)


            
            dataproduct = self.api.to_geodataframe(download_candidate) #to put into dataframe
            d = []
            for i in range(len(dataproduct.uuid)):
                product_id = self.api.get_product_odata(dataproduct['uuid'][i])
               # print(f"show this {product_id}")
                for j in product_id.keys():
                    if (j == 'Online' and product_id[j] == True):#check id which is online
                        d.append(dataproduct['uuid'][i])
            if len(d)==0:
                print('No data available online')

            print(f"products available online = {len(d)}")
            #data = self.api.download(random.choice(d)) #randomly download
           
        else:
            print("Define query attribute")
                                   
                            
sentinel1_download_preprocess.parameters().sentinel1_download()                        


# In[ ]:




