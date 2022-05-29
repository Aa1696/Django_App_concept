from django.shortcuts import render

# Create your views here.
from blog.models import Blog


def allblog(request):
    blog_object=Blog.objects
    return render(request,'blog/allblog.html',{'blogs':blog_object})
