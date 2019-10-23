# coding=UTF-8
from ast import literal_eval

from django.db.models import Q
from django.http import Http404, HttpResponseBadRequest, HttpResponseNotAllowed,  StreamingHttpResponse
import json
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import models, connection
import re
from django.contrib.admin.views.decorators import staff_member_required
import pytz
import datetime
from django.utils.timezone import utc
from .models import User_Template


# Example
'''
Use it when http request has no permission
'''
class HttpResponseUnauthorized(HttpResponse):
    status_code = 401

'''
User Login
'''
def alogin(request):
    if not request.method == 'POST':
        return HttpResponseNotAllowed(['POST',])
    if request.user.is_authenticated():
        return HttpResponse("{'status':'success'}")
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    user = authenticate(username=username,password=pwd)
    if user is not None:
        login(request, user)
        return HttpResponse(json.dumps({"status":"success"}),content_type="application/json")
    else:
        return HttpResponse(json.dumps({"status":"failed"}),content_type="application/json")

'''
User logout
'''
def alogout(request):
    if not request.user.is_authenticated():
        return HttpResponseUnauthorized()
    logout(request)
    return HttpResponse(json.dumps({"status":"success"}),content_type="application/json")

'''
User Registration
'''
def aregist(request):
    if not request.method == 'POST':
        return HttpResponseNotAllowed(['POST',])
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    email = request.POST.get('email')
    errors = {'username':None,'pwd':None,'email':None}
    flag = True
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9@$_]{5,15}$')
    if username is None or len(username)<6 :
        errors['username'] = 'username is too short'
        flag = False
    elif len(User.objects.filter(username=username))>=1:
        errors['username'] = 'username has already existed'
    if pwd is None or not pattern.match(pwd):
        errors['pwd'] = 'password wrong format'
        flag = False
    if email is None or not re.match(
            r'^[_a-z\d\-./]+@[_a-z\d\-]+(\.[_a-z\d\-]+)*(\.(info|biz|com|edu|gov|net|am|bz|cn|cx|hk|jp|tw|vc|vn))$',
            email.lower()):
        errors['email'] = 'wrong email format'
        flag = False
    if flag:
        user = User.objects.create_user(username,email,pwd)
        user.save()
        user_template = User_Template(user=user)
        user_template.save()
        resp = {'status':'success','error':errors}
    else:
        resp = {'status':'failed','error':errors}
    return HttpResponse(json.dumps(resp), content_type='application/json')



'''
Show the HomePage
'''
def index_webpage(request):
    return render_to_response('hello.html')

