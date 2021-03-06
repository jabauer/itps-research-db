"""itps_research URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory import views as inventory_views
from places import views as place_views

urlpatterns = [

    path('', inventory_views.index, name='index'),
    path('data/locations.geojson', place_views.make_locations_geojson, name='locations_geojson'),
    path('data/items-by-status.json', inventory_views.make_items_by_status_json, name="items_by_status"),
    # path('data/credits-by-user.json', inventory_views.make_credits_by_user_json, name="credits_by_user"),

    # Enables the entire admin
    path('admin/', admin.site.urls),
]
