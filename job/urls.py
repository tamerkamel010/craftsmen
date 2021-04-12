from django.urls import path 
from . import views 

urlpatterns = [
    path('jobs/', views.JobList.as_view(), name='job_list'),
    path('job/<slug>', views.JobDetail.as_view(), name='job_detail'),
    # apis 
    path('jobs/apis/', views.JobAPi.as_view(), name='job_api'),
    path('categories/apis/', views.CategoryApi.as_view(), name='category_api'),
]
