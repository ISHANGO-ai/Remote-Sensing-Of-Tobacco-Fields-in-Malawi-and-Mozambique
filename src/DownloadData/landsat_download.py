from config import args
import landsatxplore
from landsatxplore.earthexplorer import EarthExplorer
from landsatxplore.api import API
#import datetime
#import json


def download_Landsat():
    username = input('username:')
    password = input('password:')
    #start_date = input('date_1:') 
    #end_date = input('date_2:') 
    #latitude = input('lat:')
    #longitude = input('lon:')
   # cloud_max = int(input('cloud:')) 
   # product = input('dataset:')
    
 
    api = landsatxplore.api.API(username,password)
 
    scenes = api.search(
        dataset = args.product,
        latitude = args.latitude,
        longitude = args.longitude,
        start_date = args.start_date, # datetime.datetime.strptime(start_date, "%Y-%m-%d"),
        end_date = args.end_date, # datetime.datetime.strptime(end_date, "%Y-%m-%d"),
        max_cloud_cover = args.cloud_max)
 
    print('{} scenes found.'.format(len(scenes)))
    api.logout()
 
    explorer = EarthExplorer(username, password)
 
    for scene in scenes:
 
        
        ID = scene['landsat_scene_id']
        print('Downloading data %s '% ID)
        
        explorer.download(ID, output_dir='./data')
 
    explorer.logout()

download_Landsat()