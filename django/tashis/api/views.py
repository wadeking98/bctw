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

objs = {
    "users":User.objects,
    "species":species.objects,
    "survey_methods":survey_methods.objects,
    "survey_method_types":survey_method_types.objects,
    "incident_observations":incident_observations.objects,
    "observation_types":observation_type.objects,
    "projects":project.objects,
    "questions":survey_questions.objects,
    "question_data":survey_data.objects
}

def get_all(request, obj=""):
    return HttpResponse(serializers.serialize('json', objs[obj].all()), content_type='application/json')

def search(request, obj=""):
    req_dict = dict(request.GET)
    req_dict_clean = {}
    #remove the array wrapper from value
    for key in req_dict:
        req_dict_clean[key] = req_dict[key][0]

    return HttpResponse(serializers.serialize('json', objs[obj].filter(**req_dict_clean)), content_type='application/json')

def signup(request):
    return HttpResponse("hello")

#TODO add api post methods


