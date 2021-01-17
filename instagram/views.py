from django.shortcuts import render
from .models import Image, Profile,Comments

# Create your views here.
def index(request):
    posts = Image.all_images()
  

    return render(request, 'index.html',{'posts':posts})


def profile(request):

    user_posts = Image.user_pics(request.user)
    return render(request,'profile.html',{'user_posts':user_posts})


def edit_profile(request):

    if request.method=='POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
    return render(request,'update_profile.html',{'form':form})
