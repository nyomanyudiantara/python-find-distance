from geopy.geocoders import Nominatim
from geopy import distance

geocoder = Nominatim(user_agent="I learn Python")
location1 = "Moscow Ring Road"
location2 = "bangalore"

coordinates1 = geocoder.geocode(location1)
coordinates2 = geocoder.geocode(location2)

# print(coordinates1.latitude)

lat1, long1 = (coordinates1.latitude), (coordinates1.longitude)
lat2, long2 = (coordinates2.latitude), (coordinates2.longitude)

place1 = (lat1, long1)
place2 = (lat2, long2)

print(distance.distance(place1, place2))