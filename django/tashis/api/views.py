from django.shortcuts import render
from .models import *
from .tests import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
def test(request):
    return HttpResponse(mainTest())

def get_all(request, obj=""):
    objs = {
        "users":lambda : HttpResponse(serializers.serialize('json', app_user.objects.all()), content_type='application/json'),
        "species":lambda : HttpResponse(serializers.serialize('json', species.objects.all()), content_type='application/json'),
        "survey_methods":lambda : HttpResponse(serializers.serialize('json', survey_methods.objects.all()), content_type='application/json')
    }
    return objs[obj]()


