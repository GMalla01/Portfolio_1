from django.urls import path

from . import views

urlpatterns = [
   path("", views.home, name="index"),
   path("about/", views.about, name="about"),
   path("service/", views.service, name="service"),
   path("blog/", views.blog, name="blog"),
   path("blog/<str:slug>/", views.blog_detail, name="blog_detail"),
   path("gallery/", views.gallery, name="gallery"),
   path("category/<str:category_slug>/", views.gallery, name="image_by_category"),
   path("contact/", views.contact, name="contact"),
   path("search/", views.search, name="search"),
]