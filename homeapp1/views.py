from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeApp1Views(TemplateView):
    template_name = 'base.html'

#class HomeApp2Views(TemplateView):
 #    template_name = 'locatsion.html'

#class WorkdayViews(TemplateView):
 #   template_name = 'Workday.html'



