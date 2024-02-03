# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 01:33:52 2024

@author: hank
"""

from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    return{'categories':Category.objects.all(),
           'current_category':current_category}