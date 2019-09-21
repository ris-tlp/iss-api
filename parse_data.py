import urllib
import datetime
from bs4 import BeautifulSoup
from pyorbital.orbital import Orbital


def scrape() -> list:
    page = urllib.request.urlopen(
        "http://celestrak.com/NORAD/elements/stations.txt")

    data = str(page.read())
    html_list = data.split("\\n")
    tle = []
    tle.append(html_list[1].split("\\r")[0])
    tle.append(html_list[2].split("\\r")[0])

    return tle


def parse(tle_list) -> dict:
    line1 = str(tle_list[0])
    line2 = str(tle_list[1])
    orb = Orbital("ISS (ZARYA)", line1=line1, line2=line2)
    data_set = orb.get_lonlatalt(datetime.datetime.utcnow())

    data = {
        "Longitude": round(data_set[0], 3),
        "Latitude": round(data_set[1], 3)
    }

    return data
