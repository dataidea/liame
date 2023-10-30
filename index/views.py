import markdown
from .models import (TermOfService, PrivacyPolicy, Feedback)
from django.shortcuts import (render, redirect, get_object_or_404)
from .models import (Service, Contact, Feature,
                     Partner, Portfolio, Testimonial, 
                     FrequentlyAskedQuestion, CompanyInfo)
from .forms import FeedbackForm
from blog.models import Blog

# Create your views here.
def home(request):
    services = Service.objects.all()
    contacts = Contact.objects.all()
    features = Feature.objects.all()
    partners = Partner.objects.all()
    portfolios = Portfolio.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()
    companyinfo = CompanyInfo.objects.get(
        name="Liame Designs")
    blogs = Blog.objects.all().order_by('-pk')[:6]
    
    context = {
        'faqs': faqs,
        'blogs': blogs,
        'services': services,
        'contacts': contacts,
        'features': features,
        'partners': partners,
        'portfolios': portfolios,
        'companyinfo': companyinfo,
        'testimonials': testimonials,
    }
    
    template_name = 'index/home.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)

def portfolio(request):
    portfolio = Portfolio.objects.all()
    partners = Partner.objects.all()
    companyinfo = CompanyInfo.objects.get(
        name="Liame Designs")
    contacts = Contact.objects.all()
    features = Feature.objects.all()

    context = {'portfolios':portfolio, 
               'partners':partners,
               'companyinfo':companyinfo,
               'features':features,
               'contacts':contacts}
    
    template_name = 'index/portfolio.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)

def portfolioDetails(request, id):
    portfolio = Portfolio.objects.get(id=id)
    companyinfo = CompanyInfo.objects.get(
        name="Liame Designs")
    contacts = Contact.objects.all()
    partners = Partner.objects.all()

    context = {'portfolio':portfolio, 
               'description': markdown.markdown(portfolio.description),
               'companyinfo':companyinfo,
               'partners':partners,
               'contacts':contacts}
    
    template_name = 'index/portfolio_details.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)


def services(request):
    services = Service.objects.all()
    partners = Partner.objects.all()
    companyinfo = CompanyInfo.objects.get(
        name="Liame Designs")
    contacts = Contact.objects.all()
    features = Feature.objects.all()

    context = {'services':services, 
               'partners':partners,
               'companyinfo':companyinfo,
               'features':features,
               'contacts':contacts}
    
    template_name = 'index/services.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)

def about(request):
    companyinfo = CompanyInfo.objects.get(
        name="Liame Designs")
    contacts = Contact.objects.all()
    features = Feature.objects.all()
    partners = Partner.objects.all()
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all().order_by('-pk')[:6]

    context = {'about':about, 
               'blogs':blogs,
               'partners':partners,
               'testimonials':testimonials,
               'companyinfo':companyinfo,
               'features':features,
               'contacts':contacts}
    
    template_name = 'index/about.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)

def contact(request):    
    companyinfo = CompanyInfo.objects.get(
        name="Liame Designs")
    contacts = Contact.objects.all()
    features = Feature.objects.all()

    context = {'companyinfo':companyinfo,
               'features':features,
               'contacts':contacts,}

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            context['message'] = 'Thanks for contacting us, We will get back to you as soon as possible'
            template_name = 'message.html'
            return render(request=request,
                          template_name=template_name,
                          context=context)
                          
        else:
            context['errors'] = form.errors
    else:
        context['form'] = FeedbackForm()

    template_name = 'index/contact.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)


def termsOfService(request):
    terms_of_service = TermOfService.objects.all()
    context = {'terms_of_service':terms_of_service}
    
    template_name='index/terms_of_service.html'
    return render(request=request, template_name=template_name, context=context)

def privacyPolicy(request):
    privacy_policy = PrivacyPolicy.objects.all()
    context = {'privacy_policy':privacy_policy}
    
    template_name='index/privacy_policy.html'
    return render(request=request, template_name=template_name, context=context)

def notAllowed(request):
    context = {'message': 'You are not allowed to access this page, contact admin for help.'}
    template_name = 'message.html'
    return render(request=request, template_name=template_name, context=context)

def paidFeature(request):
    context = {'message': 'This is a paid feature, however, a trial period can be granted, please contact admin for more information.'}
    template_name = 'message.html'
    return render(request=request, template_name=template_name, context=context)

def sitemap(request):
    template_name = 'index/sitemap.xml'
    return render(request=request, template_name=template_name)

def robots(request):
    template_name = 'index/robots.txt'
    return render(request=request, template_name=template_name)

def ads(request):
    template_name = 'index/ads.txt'
    return render(request=request, template_name=template_name)