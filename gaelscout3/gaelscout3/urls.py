"""gaelscout3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from teamindex import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('<str:match_number>/match/', views.specmatch, name='specmatch'),
    path('divisionindex/', views.divisionindex, name='divisionindex'),
    path('researchview/', views.divisionindex, name='divisionindex'),
    path('rankings/', views.rankings, name='rankings'),
    path('matches/', views.matches, name='matches'),
    path('teamindex/', views.teamindex, name='teamindex'),
    path('sri/', views.sri, name='sri'),
    path('', views.home, name='home'),
    path('<str:team_number>/dashboard/', views.dashboard, name='dashboard'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
