from django.test import TestCase
from django.shortcuts import render
import json
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework import status

def testUser():
    #create new user and assert that it is in the database
    User.objects.create_user(username="test@test.com",
                email="test@test.com",
                first_name="test",
                last_name="test",
                password="test")
    u = User.objects.get(username="test@test.com")

    #assert user is queryable
    assert(u is not None)

    #assert user is authenticatable
    assert(authenticate(username="test@test.com", password="test") is not None)

# Create your tests here.
def mainTest():
    testUser()
    return "hello from test"