from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
def index(request):
    postblog=Blogpost.objects.all()
    return render(request,'blog/index.html',{'postblog':postblog})
def blogpost(request,id):
    postblog=Blogpost.objects.all()
    postb=Blogpost.objects.filter(post_id=id)
    n=len(postblog)
    pid=int(id)-1
    nid=int(id)+1
    return render(request,'blog/blogpost.html',{'postb':postb[0],'pid':pid,'nid':nid,'n':n})
# Create your views here.
