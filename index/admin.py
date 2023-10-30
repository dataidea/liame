from django.contrib import admin
from .models import (CompanyInfo, Service, Portfolio, 
                     Feature, Testimonial, Partner, Contact,
                     TermOfService, PrivacyPolicy,  Feedback,
                     FrequentlyAskedQuestion,  
                     )

# Register your models here.
admin.site.register(model_or_iterable=[CompanyInfo, Service, Portfolio, 
                     Feature, Testimonial, Partner, Contact,
                     TermOfService, PrivacyPolicy,  Feedback,
                     FrequentlyAskedQuestion, ])

admin.site.site_header = "Liame Designs Admin Panel"

admin.site.site_title = "Liame Designs Admin Panel"