# Django Rapid Development Template

> 2019-10-22

[中文说明](readme_cn.md)

## Project Introduction

This project is a Django rapid development template, which contains modules such as web page routing, request processing, database operation, periodic tasks, and provides code examples such as user registration, login, logout and email sending.<br>
* project structure
    * project_template : django configuration
    * TestModel : project main app
    * utils: utility classes
* Project Environment
    python3 \ mysql 
    Installation project dependency
    ```
    pip install -r requirements.txt
    ```
    If the installation fails in the middle of the process, you can install it manually. The version does not have to be consistent.<br>

****

## Function Introduction
### Web Page & Routing
HTML, CSS, JS and other files in project are stored in `TestModel/templates` <br>
`project_template/urls.py` is used to represent the view information. <br>
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello$', views.index_webpage),
    url(r'^login$', views.alogin),
    url(r'^logout$', views.alogout),
    url(r'^register$', views.aregist)
]
```
`TestModel/views.py` is used to write the specific contents of views. In the example, it has provided the relevant codes for users to login, logout, registration and visit web pages. <br>
After running Django server, you can access `TestModel/templates/hello.html` by visiting http://127.0.0.1:8000/hello . Successful opening means successful deployment. <br>

### Reuqest Processing
`TestModel/views.py` can be used to write the details of the server interface.<br>
```python
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
```
`request.method` can be used to decide POST or GET. <br>
The return value of the function is response. We take JSON for example.<br>

### Database Operations
In this template, MYSQL is selected as the database.<br>
You can modify `project_template/db.cfg` to change the database settings to your own configuration.<br>

`TestModel/models.py` is used to write the table structure of the database.<br>
```python
class User_Template(models.Model):
    user = models.OneToOneField(User,on_delete=None)
    head_img = models.ImageField(upload_to='',default='',height_field='head_height',
                                 width_field='head_width')
    head_height = models.PositiveIntegerField(default=200)
    head_width = models.PositiveIntegerField(default=200)
    email = models.CharField
    conf = models.CharField(max_length=2300, null=False, default='{}')
```
After writing the properties of various entity classes, enter the following command to convert the entity class in `models.py` to the table structure in the database.<br>
```
python manage.py makemigrations
python manage.py migrate
```
Log in to the database, and `show tables` to see that the tables have been built.<br>

### Timing Task
The timing task in this template use the Celery.<br>
`TestModel/tasks.py` is used to write various timing tasks. This template provides the timing task of sending email as an example.<br>
When writing a timing function, `@shared_task` must be marked above the function.<br>
Then create superuser
```
python manage.py createsuperuser
```
Aftere creation, start the Django server, access http://127.0.0.1:8000/admin in the browser, and log in with the user you just created.<br>
- Click Periodic Tasks to add the scheduled tasks that have been written
- Click Crontabs \ Intervals to set the time of the scheduled tasks

### Send E-Mail
An example of sending email has been provided in `TestModel/tasks.py`.<br>
In `project_template/settings.py` , you need to modify the configuration according to your own mailbox. <br>
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''
```


****

|Author|RongRongJi|
|---|---
|Contact|[homepage](https://github.com/RongRongJi)