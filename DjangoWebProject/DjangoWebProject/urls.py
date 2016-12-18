"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms

import app.views
from app import views



# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
   url(r'^$', views.index, name='index'),
    url(r'^list/', views.list, name='list'),
    url(r'^add/', views.add, name='add'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
