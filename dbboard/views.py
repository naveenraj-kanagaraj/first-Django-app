# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import devboard
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
	return render(request,'home.html')


