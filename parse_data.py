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


def parse(tle: list) -> dict:
    line1 = str(tle[0])
    line2 = str(tle[1])
    orb = Orbital("ISS (ZARYA)", line1=line1, line2=line2)
    data_set = orb.get_lonlatalt(datetime.datetime.utcnow())

    coordinates = {
        "Longitude": round(data_set[0], 2),
        "Latitude": round(data_set[1], 2)
    }

    return coordinates
