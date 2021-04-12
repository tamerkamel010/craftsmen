from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job, Category
from django.views.generic import ListView, DetailView
from rest_framework import generics 
from .serializers import JobSerializer, CategorySerializer
# Create your views here.

class JobList(ListView):
    template_name = 'jobs-list-layout-1.html'
    context_object_name = 'jobs'
    model = Job 

class JobDetail(DetailView):
    model = Job 
    template_name = 'single-job-page.html' 
    def get_context_data(self, **kwargs):
        context = super(JobDetail, self).get_context_data(**kwargs)
        context['similar_jobs'] = Job.objects.filter(category = self.object.category).exclude(slug = self.kwargs['slug'])[:4]
        return context

# apis 
class JobAPi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class CategoryApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer