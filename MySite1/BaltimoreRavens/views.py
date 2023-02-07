from django.shortcuts import render
from django.http import  HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

def index(request):
    return render(request, "BaltimoreRavens/index.html")