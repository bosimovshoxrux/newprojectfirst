from django.urls import path
from .views import HomeApp1Views, HomeApp2Views,WorkdayViews

urlpatterns = [
    #path('workday/',WorkdayViews.as_view(), name='workday'),
    #path('locatsion/',HomeApp2Views.as_view(), name='home2'),
    path('', HomeApp1Views.as_view(), name='home'),


]
