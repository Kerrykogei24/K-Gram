from django.db import models

# Create your models here.

class Image(models.Model):
    image= models.ImageField('image')
    name= models.CharField(max_length=30)
    caption= models.TextField()
    comments = models.CharField(max_length=30,blank=True)
    likes=models.ManyToManyField(User, related_name='blog_posts')
    pub_date=models.DateTimeField(auto_now_add=True)

