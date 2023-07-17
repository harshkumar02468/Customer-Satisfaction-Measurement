from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_view, name='home'),
    path('predict/', views.predict , name='predicted'),
    path('sentiment_analysis/', views.sentiment_analysis, name='sentiment_analysis'),
    path('heySweetheart/', views.heySweetheart, name='heySweetheart'),
    
]