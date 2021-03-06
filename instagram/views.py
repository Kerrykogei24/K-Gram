from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Image,Profile,Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import NewPostForm,SignUpForm,EditProfileForm,CommentForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import (DetailView)

@login_required(login_url = '/accounts/login/')
def index(request):
    posts = Image.all_images()
    return render(request, 'index.html',{'posts':posts})


def signUp(request):    
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['username']
            email = form.cleaned_data['email']
            send=welcome_email(name,email)
            HttpResponseRedirect('timeline')

    else:
        form = SignUpForm()

    return render(request,'registration/registration_form.html',{'form':form})


@login_required(login_url = '/accounts/login/')
def profile(request):

    user_posts = Image.user_pics(request.user)
    return render(request,'profile.html',{'user_posts':user_posts})

@login_required(login_url = '/accounts/login/')
def edit_profile(request):

    if request.method=='POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
    return render(request,'update_profile.html',{'form':form})



@login_required(login_url = '/accounts/login/')
def new_post(request):
    if request.method=='POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('timeline')

    else:
        form = NewPostForm()
        
    return render(request,'new_post.html',{'form':form})


@login_required(login_url = '/accounts/login/')
def comment(request,id):

    id =id
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            image = Image.objects.get(id = id)
            comment.pic_id = image
            comment.save()
            return redirect('timeline')

        else:
            pic_id = id
            messages.info(request,'Make sure you fill all fields correctly')
            return redirect('comment',id=pic_id)
    else:
        id = id
        form =CommentForm()
        return render(request,"comment.html",{'form':form,"id":id})


@login_required(login_url = '/accounts/login/')
def single_pic(request,id):

    post = Image.objects.get(id = id)
    comments = Comments.objects.filter(pic_id = id)
    return render(request,'single_pic.html',{'post':post,"comments":comments})

@login_required(login_url = '/accounts/login/')
def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_pics = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{'message':message,'image':searched_pics})

    else:
        message = "You have not entered anything to search"
        return render(request,'search.html',{"message":message})

@login_required(login_url="/accounts/login/")
def logout_request(request):

    logout(request)
    return redirect('timeline')

class PostDetailView(DetailView):
    model = Image
    template_name= 'single_pic.html'

    def get_context_data(self, *args, **kwargs):
        context=super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(Image, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        context["total_likes"]=total_likes
        return context


def like_image(request, pk):
    post= get_object_or_404(Image, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('singlepic', args=[str(pk)]))


@login_required
def add_like(request, post_id):
    post = Image.objects.filter(pk=post_id).first()
    post.likes += 1
    post.save()
    all_posts = Image.get_all_posts()   
    context = {
        'pic': all_posts,
    }    
    return render(request, 'index.html', context)