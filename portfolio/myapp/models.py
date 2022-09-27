from audioop import reverse
from email.policy import default
from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse

# Create your models here.
class blog_post(models.Model):
    title = models.CharField(max_length= 250)
    slug = models.SlugField(unique = True)
    image = ResizedImageField(size =[500,500],crop =['middle','center',], upload_to="static/image")
    # image=models.ImageField(upload_to="static/image")
    content = models.TextField(max_length=5000)
    author = models.CharField(max_length=50)
    post_time = models.DateTimeField(auto_now = True )


    def __str__(self):
        return f" {self.title} { self.author} { self.post_time}"

class image_category(models.Model):

    category_name= models.CharField(max_length=200)
    category_slug = models.SlugField(unique=True)


    def get_url(self):
        return reverse('image_by_category', args=[self.category_slug])
    
    def __str__(self):
        return f"{self.category_name} {self.category_slug}"

class Image(models.Model):
    image = ResizedImageField(size=[1000,1000],crop =['middle','center'], upload_to="static/image")
    image_name = models.CharField(max_length=200)
    image_slug = models.SlugField(unique=True)
    category_image = models.ForeignKey(image_category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.image_name} {self.image_slug} {self.category_image} "