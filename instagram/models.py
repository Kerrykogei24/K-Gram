from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    image= models.ImageField(upload_to ='image/')
    name= models.CharField(max_length=30)
    caption= models.CharField(max_length= 300)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    def total_likes(self):
        return self.likes.count()


    def update_image(self):
        self._do_update()

    def get_absolute_url(self):
        return reverse('singlepic', kwargs={'pk':self.pk})



    @classmethod
    def all_images(cls):
        timeline_pics = cls.objects.all()
        return timeline_pics

    @classmethod
    def user_pics(cls,user):
        user_pic = cls.objects.filter(user = user)
        return user_pic

    @classmethod
    def search_image(cls,search_term):

        searched_image = cls.objects.filter(name =search_term)
        return searched_image
    @classmethod
    def delete_post(cls, post_id):
        post = cls.objects.filter(pk=post_id)
        post.delete()

    @classmethod
    def get_all_posts(cls):
        return cls.objects.order_by()



    def __str__(self):
        return self.name
    


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='image/')
    bio = models.CharField(max_length=300)
    username = models.CharField(max_length=50,default='Your username')

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def profiles_posts(self):
        return self.image_set.all()



  
    def search_profile(cls, username):

       found_user = User.objects.get(username = username)

       return found_user


    def __str__(self):
        return self.username


class Comments(models.Model):
    pic_id = models.ForeignKey(Image,on_delete=models.CASCADE)
    text = models.CharField(max_length=1500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user


    def save_comments(self):
        self.save()

    
    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(pic_id=id)
        return comments


