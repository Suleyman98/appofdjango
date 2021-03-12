from django.shortcuts import render,redirect
from posts.models import BlogPost,TechPost
# Create your views here.
def index(request):
	posts=BlogPost.objects.all()
	posts1=TechPost.objects.all()
	return render(request,'index.html',{'posts':posts,'posts1':posts1})
def about(request):
	posts=BlogPost.objects.all()
	return render(request,'about.html',{'posts':posts})
def services(request):
	posts=BlogPost.objects.all()
	posts1=posts[0:4]
	if len(posts)>4:
		posts2=posts[4:]
	return render(request,'services.html',{'posts1':posts1,'posts2':posts2})
 
 