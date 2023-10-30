from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPage(models.Model):
    image = models.ImageField(upload_to = 'blog/images', default='blog.jpg')
    highlight = models.CharField(max_length=122, default='Welcome to our Blog')
    description = models.CharField(max_length=122, default='Welcome to our Blog')

    def __str__(self):
        return self.highlight

class Author(models.Model):
    name = models.CharField(max_length=122, default='dataidea')
    image = models.ImageField(upload_to = 'blog/images', default='profile.jpg')
    email = models.CharField(max_length=122, default='datasideaofficial@gmail.com')
    profile = models.TextField(default='No profile provided')

    def __str__(self):
        return self.name
   
class BlogCategory(models.Model):
    name = models.CharField(max_length=122, default='New category')
    description = models.CharField(max_length=122, default='New category description')
    color = models.CharField(max_length=122, default='purple')

    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    slug = models.CharField(max_length=122, default='New Blog Slug')
    title = models.CharField(max_length=122)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(to=BlogCategory, on_delete=models.CASCADE, default=1)
    brief = models.TextField(default='')
    image = models.ImageField(upload_to = 'blog/images')
    date_featured = models.DateField(auto_now_add=True, null=True, blank=True)
    content_markdown = models.TextField(default='')

    def __str__(self):
        return self.title
