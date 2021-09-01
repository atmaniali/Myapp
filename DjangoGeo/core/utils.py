# from django.contrib.gis.geoip2 import GeoIP2
import requests

def get_geo(ip) :
    pass
    # g = GeoIP2()
    # cuntry = g.country(ip)
    # city = g.city(ip)
    # lat , longi = g.lat_lon(ip)
    # return cuntry, city, lat, longi

def get_all_provinces():
    provinces = requests.get('https://api.corona-dz.live/province/latest').json()
    data = []
    longitude = []
    latitide = []
    for province in provinces :
        data.append(province['data'])
    #     # longitude.append(province[''])
    #print(type(data))
    return provinces    

get_all_provinces()

#  [{'date': '2021-09-01T00:00:00.000Z', 'provinceId': 1, 'confirmed': 1329, 'recovered': 0, 'deaths': 8, 'newConfirmed': 1, 'newRecovered': 0, 'newDeaths': 0, 'avg7Confirmed': 0.86, 'avg7Recovered': 0, 'avg7Deaths': 0}]