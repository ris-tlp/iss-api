# from pyorbital import tlefile
import ephem
import datetime
from math import degrees

def parse(tle_list):
    line1 = str(tle_list[0])
    line2 = str(tle_list[1])
    iss = ephem.readtle("ISS (ZARYA)", line1, line2)
    iss.compute(datetime.datetime.utcnow())

    data = {
        "Latitude": str(round(degrees(iss.sublat), 4)) + " N",
        "Longitude": str(round(degrees(iss.sublong), 4)) + " E"
    }

    return data