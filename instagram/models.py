from django.db import models

# Create your models here.

class Image(models.Model):
    image= models.ImageField('image')
        author= models.ForeignKey(Profile, on_delete=models.CASCADE)
    name= models.CharField(max_length=30)
    caption= models.TextField()
    comments = models.CharField(max_length=30,blank=True)
    likes=models.ManyToManyField(User, related_name='blog_posts')
    pub_date=models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self._do_update()
    
    def __str__(self):
        return self.name
    


class Profile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio= models.CharField(max_length=100)
    prof_pic= models.ImageField('image')
    following= models.ManyToManyField(User, related_name='follower', blank=True)
    created=models.DateTimeField(auto_now_add=True)

