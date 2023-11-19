import pytz

# Obtenir la liste des fuseaux horaires disponibles
timezones = pytz.all_timezones

# Afficher la liste des fuseaux horaires
for tz in timezones:
    print(tz)
