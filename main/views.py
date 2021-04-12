from django.shortcuts import render
from django.views.generic import TemplateView as TemplateView


class Home(TemplateView):
    template_name = 'index.html'
