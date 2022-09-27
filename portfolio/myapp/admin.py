from django.contrib import admin
from  .models import blog_post, image_category,Image
# Register your models here.



class BlogpostAdmin(admin.ModelAdmin):
    list_display=["title",'author','post_time']
    list_display_links=["title",'author','post_time']
    prepopulated_fields = {
        'slug': ['title'],
    }

admin.site.register(blog_post, BlogpostAdmin)

class GallerycategoryAdmin(admin.ModelAdmin):
    list_display=["category_name"]
    prepopulated_fields= {
        'category_slug':['category_name']
    }

admin.site.register(image_category, GallerycategoryAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display=["image_name","category_image"]
    prepopulated_fields= {
        'image_slug':['image_name']
    }

admin.site.register(Image,ImageAdmin)