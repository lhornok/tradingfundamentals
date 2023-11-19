import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

# Fonction pour obtenir le fuseau horaire à partir des coordonnées géographiques
def get_timezone_from_coords(latitude, longitude):
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=latitude, lng=longitude)
    if timezone_str:
        timezone = pytz.timezone(timezone_str)
        return timezone
    else:
        return None


# Fonction pour obtenir le fuseau horaire à partir du nom de la ville
city_name='Washington, DC'
geolocator = Nominatim(user_agent="app")
place_details = geolocator.geocode(city_name)
print (place_details)
print ((place_details[1][0], place_details[1][1]))
timezone = get_timezone_from_coords(place_details[1][0], place_details[1][1])
print (timezone)