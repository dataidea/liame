import markdown
from . models import Blog
from . models import BlogPage
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from index.models import (CompanyInfo,Contact)


# Create your views here.
def blogs(request):
    companyinfo = CompanyInfo.objects.all()[0]
    contacts = Contact.objects.all()
    # Fetch Blogs
    blogs = Blog.objects.all().order_by('-pk')
    blog_set = BlogPage.objects.all()[0]

    # pagination
    paginator = Paginator(blogs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs': page_obj,
        'companyinfo': companyinfo,
        'contacts':contacts
        }
    template_name = 'blog/blog-home.html'
    return render(request=request, template_name=template_name, context=context)


def blogDetails(request):
    companyinfo = CompanyInfo.objects.all()[0]
    contacts = Contact.objects.all()
    # Fetch Blog Details
    try:
        blog = Blog.objects.get(slug=request.GET.get('slug'))
        related = Blog.objects.filter(category=blog.category).order_by('-pk')
    except Blog.DoesNotExist:
        context = {'state': 'danger', 'message': 'Blog not found'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)

    
    context = {
        'blog': blog, 
        'details': markdown.markdown(blog.content_markdown), 
        'related': related[:4],
        'companyinfo':companyinfo,
        'contacts':contacts
        }
    return render(request, 'blog/blog-single.html', context=context)

def search(request):
    query = request.POST.get(key='query')
    blogs = Blog.objects.filter(
        Q(title__icontains=query) |
        Q(content_markdown__icontains=query)
    )
    blog_set = BlogPage.objects.all()[0]

    # pagination
    paginator = Paginator(blogs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'blogs': page_obj, 'blog_set': blog_set}
    template_name = 'blog/blog-home.html'
    return render(request=request, template_name=template_name, context=context)
