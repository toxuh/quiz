from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('answer/', views.answer, name='index'),
    path('regenerate/', views.regenerate, name='index'),
]