from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Userm,Neighborhood,Business,Post
from .forms import NewProfileForm,PostForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def landing(request):
    current_user = request.user
    profile = Userm.get_user()
    posts = Post.get_post()
    return render(request,'index.html',{"posts":posts})
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Userm.get_user()
    return render(request,'profile.html',{"profile":profile})
@login_required(login_url='/accounts/login/')
def edit(request):
    current_user = request.user
    profile=Userm.get_user()

    if request.method == 'POST':
        form = NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = NewProfileForm()

    return render(request,'edit.html',{"form":form})
@login_required(login_url='/accounts/login/')
def biz(request):
    current_user = request.user
    biz = Business.get_business()
    return render(request,'biz.html',{"biz":biz})
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'biz' in request.GET and request.GET["biz"]:
        search_term = request.GET.get("biz")
        searched_biz = Business.find_business(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"biz":searched_biz})

    else:
        message = 'You havent searched for any term'
        return render(request,'search.html',{"message",message})
@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    userm = Userm.get_user()
    for user in userm:
        if user.user.id == current_user.id:
            if request.method == 'POST':
                post_form = PostForm(request.POST,request.FILES)
                if post_form.is_valid():
                    post = post_form.save(commit=False)
                    post.author = user
                    post.save()
                    return redirect(landing)
            else:
                post_form = PostForm()
            return render(request,'post.html',{"post_form":post_form})
        

