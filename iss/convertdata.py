from pyorbital import tlefile

def parse(tle_list):
    line1 = " ".join(tle_list[:9]).strip()
    line2 = " ".join(tle_list[9:]).strip()
    tle =  tlefile.read("ISS", line1=line1, line2=line2)
    return tle.inclination

    # return line1, line2