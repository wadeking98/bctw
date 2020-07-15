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
        "survey_methods":lambda : HttpResponse(serializers.serialize('json', survey_methods.objects.all()), content_type='application/json'),
        "survey_method_types":lambda : HttpResponse(serializers.serialize('json', survey_method_types.objects.all()), content_type='application/json'),
        "incident_observations":lambda : HttpResponse(serializers.serialize('json', incident_observations.objects.all()), content_type='application/json'),
        "observation_types":lambda : HttpResponse(serializers.serialize('json', observation_type.objects.all()), content_type='application/json'),
        "projects":lambda : HttpResponse(serializers.serialize('json', project.objects.all()), content_type='application/json'),
        "questions":lambda : HttpResponse(serializers.serialize('json', survey_questions.objects.all()), content_type='application/json')
    }
    return objs[obj]()

#TODO add api post methods


