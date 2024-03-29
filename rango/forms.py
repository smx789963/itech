# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 00:18:14 2024

@author: hank
"""

from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,
                           help_text="Please enter your category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)
    
    class Meta:
        model = Category
        fields = ('name',)
    
class PageCategory(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the title of page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the url of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    
    class Meta:
        model = Page
        exclude = ('category',)
        
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('https://'):
            url = f"http://{url}"
            cleaned_data['url'] = url
            
        return cleaned_data