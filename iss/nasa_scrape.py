import urllib
from bs4 import BeautifulSoup

def scrape():
    page = urllib.request.urlopen(
        "https://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html")

    soup = BeautifulSoup(page, "html.parser")
    html_list = str(soup.pre).split()
    tle_list = []

    for i, value in enumerate(html_list):
        if(value == "SET"):
            tle_list = html_list[i+2:i+20]
            break

    tle_data = " ".join(tle_list)
    return tle_data