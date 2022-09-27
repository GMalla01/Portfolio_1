from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Image
from .models import blog_post, image_category


# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    allpost=blog_post.objects.order_by('-post_time')
    # print(allpost)
    context={ 'allpost':allpost}
    return render(request,"blog.html",context)

def service(request):
    return render(request,"service.html")

def gallery(request,category_slug=None):
    images=None
    categories=None
    categories=image_category.objects.all()
    if category_slug is not None:
        category=get_object_or_404(image_category, category_slug=category_slug)
        images=Image.objects.filter(category_image=category)
    else:
        images=Image.objects.all()
    
    context={
        'categories':categories,
        "images":images,
    }

    return render(request,"gallery.html",context)

def contact(request):
    return render(request,"contact.html")


def blog_detail(request,slug):
    detail_post=blog_post.objects.filter(slug=slug).first()
    print(type(detail_post))
    print((detail_post))

    context={"detail_post": detail_post}
    return render(request,"blog_details.html", context)