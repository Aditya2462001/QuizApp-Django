from django.conf import urls
from django.urls import path
from . import views

urlpatterns = [
    path('',views.subject,name="home"),
    path('questions/<str:pk>',views.questions,name='question'),
    path ('ans/',views.result , name="answers"),
    path ('about/',views.about , name="about"),
]