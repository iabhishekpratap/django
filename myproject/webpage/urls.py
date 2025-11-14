from django.urls import path
# import path, a function used to make URLs.

from . import views
# views = file that has page functions



urlpatterns = [
    path('', views.home, name='home'),
]