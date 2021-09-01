from django.shortcuts import render
from .utils import get_geo, get_all_provinces
import folium

# Create your views here.

def index (request):
    template_name = "core/main.html"
    context = {}
    ip = "193.194.88.26"
    country, city, lat , lon = get_geo(ip)
    print(lat,lon)
    print(city)
    # initial folium map
    map = folium.Map(width = 800, height = 500, location = [35.6976541, -0.6337376], zoom_start = 5)
    # all provinces
    provinces = get_all_provinces()

    for province in provinces:
        folium.Marker([35.6976541, -0.6337376], tooltip = "click here for more", popup = "oran", icon = folium.Icon(color= 'purple')).add_to(map) 

    map = map._repr_html_() 
    context["maps"] = map
    return render(request, template_name, context)
