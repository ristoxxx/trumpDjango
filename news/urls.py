'''
File: urls.py
Created Date: Monday March 3rd 2025 04:16:59
Author: ristoxxx@github.com
-----
Last Modified: Thursday March 6th 2025 11:32:22
Modified By: ristoxxx@github.com
-----
Copyright (c) 2025 ristoxxx@github.com
'''

from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store_news, name='store_news'),
    path('read/', views.read_news, name='read_news'),
]