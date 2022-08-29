from django.urls import path
from . import views
from dotaApi.views import PlayerView
urlpatterns = [
    path('', views.index, name='index'),
    path('set_api_data/', PlayerView.set_api_data),
    ]