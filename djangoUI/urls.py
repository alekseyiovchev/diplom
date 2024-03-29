"""djangoUI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from football.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),
    path('players/', players, name = 'players'),
    path('teams/', teams, name = 'teams'),
    path('teams/manchester_city', manchester_city, name = 'manchester_city'), 
    path('teams/real_madrid', real_madrid, name = 'real_madrid'), 
    path('players/<int:players_id>/', show_player, name='players_post'),
    path('champions_league_2023/', champions_league_2023, name = 'champions_league_2023'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)