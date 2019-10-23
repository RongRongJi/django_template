# coding=UTF-8
import configparser
import datetime
import json

import math

import requests
from celery import shared_task
from django.db import models
from .models import User_Template
from django.core.mail import send_mail
import pytz
import time
import string

tz = pytz.timezone('Asia/Shanghai')

'''
An example of scheduled tasks: Send a scheduled E-mail
'''
@shared_task
def sendmail():
    '''
    Send a scheduled E-mail
    :return:
    '''
    # get all the users
    users = User_Template.objects.all()

    # input sender's e-mail address
    from_email = ''

    # send mail
    send_mail(u'email_title'+datetime.datetime.now(tz).strftime('(%Y-%m-%d %H:%M:$S)'),
              u'email_content',from_email,[user.user.email for user in users], fail_silently=True)
