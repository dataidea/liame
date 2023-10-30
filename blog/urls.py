from . import views
from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path(route='', view=views.blogs, name='blogs'),
    path(route='blogs/', view=views.blogDetails, name='blog_details'),
    path(route='search/', view=views.search, name='search'), 
]