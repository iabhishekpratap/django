from django.urls import path
# import path, a function used to make URLs.

from . import views
# views = file that has page functions

app_name = 'html_temp' 

urlpatterns = [
    path('', views.home, name='home'),
]