# from pyorbital import tlefile
import ephem
import datetime

def parse(tle_list):
    line1 = tle_list[0]
    line2 = tle_list[1]
    print(line1)
    print(line2)

    iss = ephem.readtle("ISS", str(line1), str(line2))
    now = datetime.datetime.utcnow()
    iss.compute(now)
    lon = iss.sublong()
    return lon
    # return line1, line2