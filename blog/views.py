import requests
import markdown
from . models import Blog
from django.db.models import Q
from . models import BlogComment
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.


def blogs(request):
    # Fetch Blogs
    blogs = Blog.objects.all()

    # Sort
    sorted_blogs = sorted(blogs, key=lambda k: k.popularity, reverse=True)

    # pagination
    paginator = Paginator(sorted_blogs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'blogs': page_obj}
    template_name = 'blog/blogs.html'
    return render(request=request, template_name=template_name, context=context)


def blogDetails(request):
    # Fetch Blog Details
    try:
        blog = Blog.objects.get(slug=request.GET.get('slug'))
        related = Blog.objects.filter(category=blog.category).order_by('-pk')
    except Blog.DoesNotExist:
        context = {'state': 'danger', 'message': 'Blog not found'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)
    # Fetch Blog Comments
    comments = BlogComment.objects.filter(blog=blog)

    
    context = {
        'blog': blog, 
        'details': markdown.markdown(blog.content_markdown), 
        'comments': comments,
        'related': related[:4]
        }
    return render(request, 'blog/blog_details.html', context=context)


# Comments
@login_required(login_url='accounts:signin')
def comment(request):

    if request.user.is_anonymous:
        user = User.objects.get(id=12)
    else:
        user = request.user

    try:
        comment = BlogComment(
            comment = request.POST.get(key='comment'),
            blog = Blog.objects.get(slug=request.POST.get(key='slug')),
            user = user
        )

        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        context = {'message': 'An error occured while trying to add your comment', 'state':  'danger'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)
    

def search(request):
    query = request.POST.get(key='query')
    blogs = Blog.objects.filter(
        Q(title__icontains=query) |
        Q(content_markdown__icontains=query)|
        Q(category_id=query)
    )

     # Sort
    sorted_blogs = sorted(blogs, key=lambda k: k.popularity, reverse=True)

     # pagination
    # paginator = Paginator(sorted_blogs, 4)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {'blogs': sorted_blogs}
    template_name = 'blog/blogs.html'
    return render(request=request, template_name=template_name, context=context)