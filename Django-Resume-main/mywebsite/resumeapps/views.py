from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def home(request):
	resumeapps= Profile.objects.all()
	return render(request, 'home.html', {'resumeapps':resumeapps})