from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    # return HttpResponse("hello world")
    return render_to_response('homepage.html')


def radial(request):
    # return HttpResponse("hello world")
    return render_to_response('radial_tree.html')


def hori(request):
    # return HttpResponse("hello world")
    return render_to_response('hori_tree.html')
