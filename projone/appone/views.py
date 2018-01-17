# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from appone.models import ArhProj

# Create your views here.
def index(request):
    """Home page"""
    return render(request,'appone/index.html')


def about(request):
    return render (request,"appone/about.html")

def proj(request):
    proj_list = ArhProj.objects.all().order_by("budget")
    proj_dict = {"kp":proj_list}
    return render(request,"appone/proj.html",context = proj_dict)

def flat(request):
    proj_list = ArhProj.objects.all().get(name="Apartment")
    proj_dict = {"kp": proj_list}
    return render (request,'appone/flat.html',context = proj_dict)

def mansion(request):
    proj_list = ArhProj.objects.all().get(name="Mansion")
    proj_dict = {"kp": proj_list}
    return render (request,'appone/mansion.html',context = proj_dict)


def house(request):
    proj_list = ArhProj.objects.all().get(name="Home")
    proj_dict = {"kp": proj_list}
    return render (request,'appone/house.html',context = proj_dict)