from django.shortcuts import render
from .models import Image, Profile,Comments

# Create your views here.
def index(request):
    posts = Image.all_images()
  

    return render(request, 'index.html',{'posts':posts})


def profile(request):

    user_posts = Image.user_pics(request.user)
    return render(request,'profile.html',{'user_posts':user_posts})