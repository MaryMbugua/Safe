from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Userm,Neighborhood,Business
from .forms import NewProfileForm,NeighbourhoodForm,BusinessForm
# Create your views here.

def landing(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')

def edit(request):
    current_user = request.user
    profile=Userm.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = NewProfileForm()
    return render(request,'edit.html',{"form":form})