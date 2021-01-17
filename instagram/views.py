from django.shortcuts import render
from .models import Image, Profile,Comments

# Create your views here.
@login_required(login_url = '/accounts/login/')
def index(request):
    posts = Image.all_images()
  

    return render(request, 'index.html',{'posts':posts})

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
def comment(request,id):

       id =id
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            image = Image.objects.get(id = id)
            comment.ig_pic_id = image
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
    comments = Comments.objects.filter(ig_pic_id = id)
    return render(request,'single_pic.html',{'post':post,"comments":comments})
