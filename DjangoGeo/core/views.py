from django.shortcuts import render
from .utils import get_geo, get_all_provinces
import folium

# Create your views here.

def index (request):
    template_name = "core/main.html"
    context = {}
    ip = "193.194.88.26"
    #
    map = folium.Map(width = 800, height = 500, location = [35.6976541, -0.6337376], zoom_start = 8)
    # all provinces
    provinces = get_all_provinces()

    for province in provinces:
        for data in province['data'] : 
            folium.Marker([province['latitude'], province['longitude']], tooltip = "click here for more", popup = "nom de wilaya {} confirmed is {}:".format(province['name'], data["confirmed"]), icon = folium.Icon(color= 'purple')).add_to(map) 
        print(data["confirmed"])  
        print("\n")
        print("*******")
    map = map._repr_html_() 
    context["maps"] = map
    return render(request, template_name, context)
