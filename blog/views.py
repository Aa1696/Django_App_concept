from django.shortcuts import render,get_object_or_404

# Create your views here.
from blog.models import Blog


def allblog(request):
    blog_object=Blog.objects
    return render(request,'blog/allblog.html',{'blogs':blog_object})

def detail(request,blog_id):
    blog_detail_id=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog_detail_id})
