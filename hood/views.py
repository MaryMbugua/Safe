from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def landing(request):
    return render(request,'navbar.html')