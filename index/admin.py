from django.contrib import admin
from .models import (CompanyInfo, Service, Portfolio, 
                     Feature, Testimonial, 
                     Exhibition, Partner, Contact,
                     TermOfService, PrivacyPolicy,  Feedback,
                     FrequentlyAskedQuestion,  
                     )

# Register your models here.
admin.site.register(model_or_iterable=[CompanyInfo, Service, Portfolio, 
                     Feature, Testimonial, 
                     Exhibition, Partner, Contact,
                     TermOfService, PrivacyPolicy,  Feedback,
                     FrequentlyAskedQuestion, ])