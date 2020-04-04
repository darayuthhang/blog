from django.shortcuts import render
from django.template.context import RequestContext
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")



def project(request):
	return render(request, "project.html")


def contact(request):
	return render(request, "contact.html")