from django.shortcuts import render
from .models import Destination

def index(request):
    
    dest1=Destination()
    dest1.city_name="Mumbai"
    dest1.country_name="India"
    return render(request,"index.html",{'dest1':dest1})

