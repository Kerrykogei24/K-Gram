from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    image= models.ImageField(upload_to ='image/')
    name= models.CharField(max_length=30)
    caption= models.CharField(max_length= 300)
    likes=models.ManyToManyField(User, related_name='likes', blank=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self._do_update()


    @classmethod
    def all_images(cls):
        timeline_pics = cls.objects.all()
        return timeline_pics

    @classmethod
    def user_pics(cls,user):
        user_pic = cls.objects.filter(user = user)
        return user_pic


    def __str__(self):
        return self.name
    


class Profile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio= models.CharField(max_length=100)
    prof_pic= models.ImageField('image')
    following= models.ManyToManyField(User, related_name='follower', blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def profiles_posts(self):
        return self.image_set.all()

    def save(self):
        super().save()


    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


    def __str__(self):
        return f'{self.user.username} Profile'


class Comment(models.Model):
    user_id= models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    image_id=models.ForeignKey(Image,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id} :{self.comment}'



class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'    

