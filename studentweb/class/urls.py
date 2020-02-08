#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:01:02 2020

@author: Brandon
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "class-home"),
]
