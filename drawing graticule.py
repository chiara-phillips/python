###########
# Name: Chiara Phillips
# UID: 804562889
# Date: 5/19/2019
############
# Import OGR
from osgeo import ogr
import numpy as np


# Retrieve and validate graticule interval, min/max lat/long from the user.
print("Enter your desired graticule interval between 1 and 30 degrees, a minimum and maximum latitude value within the "
      "range of -90 to 90 degrees and a minimum and maximum longitude value within the range of -180 to 180 degrees.")
for attempt in range(15):
    user_Graticule = float(input("Type your desired graticule interval here: "))
    if 1 <= user_Graticule <= 30:
        break
    # If the user did not follow instructions, tell them so and make them do it again.
    else:
        print("Graticule angle must be between 1 and 30.")
for attempt in range(15):
    # Store the input min/max latitude as a float variable
    user_min_Latitude = float(input("Type the minimum latitude point here: "))
    user_max_Latitude = float(input("Type the maximum latitude point here: "))
    # Store the input min/max longitude as a float variable
    user_min_Longitude = float(input("Type the minimum longitude point here: "))
    user_max_Longitude = float(input("Type the maximum longitude point here: "))
    if (-90 <= user_min_Latitude <= 90) and (-90 <= user_max_Latitude <= 90) and (user_min_Latitude < user_max_Latitude)\
                and (-180 <= user_min_Longitude <= 180) and (-180 <= user_max_Longitude <= 180) and \
            (user_min_Longitude < user_max_Longitude):
        break
    # If the user did not follow instructions, tell them so and make them do it again.
    else:
        print("Latitude must be between -90 and 90 and Longitude must be between -180 and 180.")

# Create a multi-line geometry object instance to store all lines of latitude and longitude;
multi_line = ogr.Geometry(ogr.wkbMultiLineString)
# Iterate over ranges of latitude and longitude separately, doing the following within the loop:
for lat in np.append(np.arange(user_min_Latitude, user_max_Latitude, user_Graticule), user_max_Latitude):
    #   Create a line string geometry object;
    line1 = ogr.Geometry(ogr.wkbLineString)
    #   Add the end points for the graticule line to the object
    line1.AddPoint(lat, user_max_Longitude)
    line1.AddPoint(lat, user_min_Longitude)
    #   Add the line string object to the multi-line geometry object created before the loop.
    multi_line.AddGeometry(line1)
for lon in np.append(np.arange(user_min_Longitude, user_max_Longitude, user_Graticule), user_max_Longitude):
    #   Create a line string geometry object;
    line2 = ogr.Geometry(ogr.wkbLineString)
    #   Add the end points for the graticule line to the object
    line2.AddPoint(user_max_Latitude, lon)
    line2.AddPoint(user_min_Latitude, lon)
    #   Add the line string object to the multi-line geometry object created before the loop.
    multi_line.AddGeometry(line2)

# Save the output as a text file containing the geometry stored in Well-Known Text (WKT) format, test in Q
with open('graticule_test6.txt', 'w') as f:
    f.write(multi_line.ExportToWkt())
    print(multi_line)
