# coding= UTF-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL

# Example
class User_Template(models.Model):
    '''
    User model packaging
    '''
    user = models.OneToOneField(User,on_delete=None)
    head_img = models.ImageField(upload_to='',default='',height_field='head_height',
                                 width_field='head_width')
    head_height = models.PositiveIntegerField(default=200)
    head_width = models.PositiveIntegerField(default=200)
    email = models.CharField
    conf = models.CharField(max_length=2300, null=False, default='{}')

    def __unicode__(self):
        return unicode_literals(self.user)

class App_Version(models.Model):
    '''
    Application Version
    '''
    version = models.CharField(max_length=15, null=False, primary_key=True)
    time = models.DateTimeField(null=False)
    size = models.CharField(null=False, max_length=7)
    description = models.CharField(null=False, max_length=150)

    class Meta:
        db_table = 'app_version'