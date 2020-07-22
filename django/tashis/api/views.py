from django.shortcuts import render
import json
from .models import *
from .tests import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
# Create your views here.
def test(request):
    print(request.session.items())
    return HttpResponse(request.user.is_authenticated)

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

@csrf_exempt
def signup(request):

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        keys = ['fname', 'lname', 'email', 'password']
        for key in keys:
            if data.get(key, None) is None:
                return HttpResponse(status=405)
        
        try:
            user = User.objects.create_user(username=data['email'],
                email=data['email'],
                first_name=data['fname'],
                last_name=data['lname'],
                password=data['password'])
            login(request, user)
        except:
            return HttpResponse(status=405)
        return HttpResponse(status=200)
    return HttpResponse(status=405)

@csrf_exempt
def signin(request):
    resp=None
    if request.method == 'POST':
        data=json.loads(request.body.decode('utf-8'))
        keys = ['email', 'password']
        for key in keys:
            if data.get(key, None) is None:
                return HttpResponse(status=405)
        
        user = authenticate(username=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            resp = HttpResponse(status=200)
            resp.set_signed_cookie('auth', True)
        else:
            resp = HttpResponse(status=401)
    else:
        resp = HttpResponse(status=405)
    
    return resp


@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse(status=200)
        



