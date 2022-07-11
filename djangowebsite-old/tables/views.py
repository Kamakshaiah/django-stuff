# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return render(response, 'tables/home.html')

def about(response):
    return render(response, 'tables/about.html')
