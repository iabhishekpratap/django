from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.recipe_create, name='recipe_create'),
    path('detail/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('edit/<int:id>/', views.recipe_update, name='recipe_update'),
    path('delete/<int:id>/', views.recipe_delete, name='recipe_delete'),
]
