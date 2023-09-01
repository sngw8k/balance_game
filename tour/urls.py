from django.urls import path
from . import views

app_name = 'tour'

urlpatterns = [
    path('', views.index, name='index'),

    path('advice/', views.advice, name='advice'),
    
]