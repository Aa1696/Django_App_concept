
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Job

def home(request):
    job_app_data=Job.objects
    return render(request,'jobs/home.html',{'jobs':job_app_data})
