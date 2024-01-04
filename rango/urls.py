# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:10:29 2024

@author: hank
"""

from django.urls import path
from rango import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    ]