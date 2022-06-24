from geoip import open_database
with open_database('data/GeoLite2-City.mmdb') as db:
    match = db.lookup_mine()
    print ('My IP info:', match)
