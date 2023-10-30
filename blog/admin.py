from django.contrib import admin
from .models import (BlogPage, Blog, BlogCategory, Author)

# Register your models here.
admin.site.register(model_or_iterable=(BlogPage, Blog, BlogCategory, Author))