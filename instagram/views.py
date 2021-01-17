from django.shortcuts import render
from .models import Image, Profile, Follow, Comment

# Create your views here.
def index(request):
    posts = Image.objects.all()
    comments = Comment.objects.filter(image_id).all()

    return render(request, 'index.html',{'posts':posts,'comments':comments}