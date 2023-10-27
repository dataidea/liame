# from .models import Testimonial
from .models import (TermOfService, PrivacyPolicy, Feedback)
from django.shortcuts import (render, redirect, get_object_or_404)
from .models import (Service, Contact, Feature, Exhibition,
                     Partner, Portfolio, Testimonial, 
                     FrequentlyAskedQuestion, CompanyInfo)

# Create your views here.
def home(request):
    services = Service.objects.all()
    contacts = Contact.objects.all()
    features = Feature.objects.all()
    partners = Partner.objects.all()
    exhibitions = Exhibition.objects.all()
    portfolios = Portfolio.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()
    companyinfo = CompanyInfo.objects.get(
        name="Liame Designs")
    
    context = {
        'faqs': faqs,
        'services': services,
        'contacts': contacts,
        'features': features,
        'partners': partners,
        'portfolios': portfolios,
        'exhibitions': exhibitions,
        'companyinfo': companyinfo,
        'testimonials': testimonials,
    }
    
    template_name = 'index/home.html'
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
               'companyinfo':companyinfo,
               'partners':partners,
               'contacts':contacts}
    
    template_name = 'index/portfolio_details.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)


def services(request):
    services = Service.objects.all()
    companyinfo = CompanyInfo.objects.get(
        name="Liame Designs")
    contacts = Contact.objects.all()
    features = Feature.objects.all()

    context = {'services':services, 
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

    context = {'about':about, 
               'companyinfo':companyinfo,
               'features':features,
               'contacts':contacts}
    
    template_name = 'index/about.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)

def feedback(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        feedback = Feedback(name=name, email=email, 
                            subject=subject, message=message)
        feedback.save()
    
        context = {'message': f'Thank you for contacting us {name}. We will get in touch as soon as possible.'}
    except Exception as e:
        context = {'message': f'Something went wrong. Please try again later.'}

    template_name='components/message.html'
    return render(request=request, template_name=template_name, context=context)


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