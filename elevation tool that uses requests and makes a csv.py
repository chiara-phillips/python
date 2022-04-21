###########
# Name: Chiara Phillips
# UID: 804562889
# Date: 5/26/2019
############

# Import OGR
from osgeo import ogr
# Import "csv" and "requests"
import csv
import requests

# Identify the location of the shapefile to be used
shp_path = 'folder/tl_2017_06_place.shp'
# Create an OGR Driver instance, with the driver type "ESRI Shapefile"
driver = ogr.GetDriverByName('ESRI Shapefile')
# Open the shapefile using the driver
file = driver.Open(shp_path)
# Get the data layer from the shapefile
layer = file.GetLayer()
# Open a CSV file for writing with the DictWriter class
with open('week8_test.csv', 'w') as f:
    # Set up CSV columns, including location's name, centroid latitude and longitude, and elevation (in feet)
    fieldnames = ['name', 'latitude', 'longitude', 'elevation']
    # Create a DictWriter object instance, and write a row of headers
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
# Begin iterating over features in the layer
    for feature in layer:
        # Get geometry of the feature
        geom = feature.GetGeometryRef()
        # Find the point centroid of the feature
        centroid = geom.Centroid()
        lat = centroid.GetY()
        long = centroid.GetX()
        r = requests.get('https://apps.gis.ucla.edu/elevation/api/v1/lookup?locations=%s,%s'%(lat, long))
        d = r.json()
        ele_m = d["results"][0]['elevation']
        # Convert elevation from meters to feet
        elevation_ft = ele_m * 3.28
        writer.writerow({'name': feature.GetField('NAME'), 'latitude': centroid.GetY(), 'longitude': centroid.GetX(),
                         'elevation': elevation_ft})
        # Print output to the console for status purposes, showing at least city name and elevation
        print(feature.GetField('NAME'), elevation_ft)