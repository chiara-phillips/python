###########
# Name: Chiara Phillips
# UID: 804562889
# Date: 4/28/2019
############

# Import haversine, csv, and pandas modules
from haversine import haversine
import csv
import pandas as pd

# Instruct the user to input a latitude and longitude point.
print("Enter latitude and longitude coordinates for a point on Earth's surface. Latitude values should be within the "
      "range of -90 to 90 and the longitude values should be within the range of -180 to 180.")
# Make sure that the point has a latitude between -90 and 90 and a Longitude between -180 and 180 with a loop.
for attempt in range(15):
    # Store the input latitude as a float variable
    user_Latitude = float(input("Type the latitude point here: "))
    # Store the input longitude as a float variable
    user_Longitude = float(input("Type the longitude point here: "))
    # If the user followed the instructions, break and move on with the script.
    if (-90 <= user_Latitude <= 90) and (-180 <= user_Longitude <= 180):
        break
    # If the user did not follow instructions, tell them so and make them do it again.
    else:
        print("Latitude must be between -90 and 90 and Longitude must be between -180 and 180.")

# Define the user input numbers as a tuple.
user_Point = (user_Latitude, user_Longitude)
# Open the airport csv
with open('airports.csv') as data:
    # Use the DictReader object with the CSV data
    reader = csv.DictReader(data)
    # Create 3 empty lists
    list1, list2, list3 = [], [], []
    for row in reader:
        # Define the airport point with the variables from the CSV data as floats
        airport_Point = float(row["latitude_deg"]), float(row["longitude_deg"])
        # Add the "name" category to list one. Make it only show 26 characters to make sure name, code, and distance
        # can all be displayed in the final print statement
        list1.append(row["name"][:26])
        # Add the IATA Code into the second empty list.
        list2.append(row["iata_code"])
        # Use the haversine module and function to calculate the distances between the input point and the CSV data
        list3.append(haversine(user_Point, airport_Point))
# Use pandas to make a dataframe with the three lists
df = pd.DataFrame({"Airport_Name": list1, "IATA_Code": list2, "Distance_KM": list3})
# Sort the lists by distance
df_sorted = df.sort_values(by="Distance_KM")
# Let the user see the final table
print(df_sorted)
