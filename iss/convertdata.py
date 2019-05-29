from pyorbital.orbital import Orbital
import datetime

def parse(tle_list):
    line1 = str(tle_list[0])
    line2 = str(tle_list[1])
    orb = Orbital("ISS (ZARYA)", line1=line1, line2=line2)
    data_set = orb.get_lonlatalt(datetime.datetime.utcnow())
    
    data = {
        "Longitude": round(data_set[0], 3),
        "Latitude": round(data_set[1], 3)
    }
    
    return data