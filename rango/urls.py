# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:10:29 2024

@author: hank
"""

from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('category/<slug:category_name_slug>/',views.show_category,name='show_category')
    ]