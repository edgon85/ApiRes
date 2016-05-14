from django.shortcuts import render
from .models import CourseApp
from .forms import CourseAppForms
from rest_framework import viewsets
from .serializers import CourseAppSerializer

# Create your views here.

def home(request):
	title = "my title"
	form = CourseAppForms(request.POST or None)
	context = {
		"title": title,
		"form":form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print (instance.name)
		print (instance.id)

	
	return render(request, "home.html", context)

class CourseAppViewSet(viewsets.ModelViewSet):
	queryset = CourseApp.objects.all()
	serializer_class = CourseAppSerializer 
