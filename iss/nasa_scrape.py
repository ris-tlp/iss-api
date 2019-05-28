import urllib
from bs4 import BeautifulSoup

def scrape():
    page = urllib.request.urlopen(
        "http://celestrak.com/NORAD/elements/stations.txt")

    data = str(page.read())
    html_list = data.split("\\n")
    tle_list = []
    tle_list.append(html_list[1].split("\\r")[0])
    tle_list.append(html_list[2].split("\\r")[0])
        
    return tle_list