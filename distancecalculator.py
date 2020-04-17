import math
def calc_dis(lat1, lon1,lat2,lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h= math.sin((lat2 - lat1)/2) ** 2 + \
        math.cos(lat1)* \
        math.cos(lat2)* \
        math.sin((lon2-lon1) / 2) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

print(calc_dis(55.378052, -3.435973,48.856613, 2.352222))