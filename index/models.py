from django.db import models

# Create your models here.
    
class CompanyInfo(models.Model):
    name = models.CharField(max_length=122, default='Liame Designs')
    highlight = models.CharField(max_length=122, default='Precise concept design for stylish living')
    description = models.TextField(default='If you are looking at blank cassettes on the web, you may be very confused at the difference in price. You may see some for as low as $.17 each.')
    about_us_highlight = models.CharField(max_length=122, default='About Us')
    about_us_description = models.TextField(default='If you are looking at blank cassettes on the web, you may be very confused at the difference in price. You may see some for as low as $.17 each.')
    quote_highlight = models.CharField(max_length=122, default='Request for quote')
    quote_description = models.TextField(default="One of our services")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=122, default='Service')
    description = models.TextField(default="One of our services")

    def __str__(self):
        return self.name
    

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio')
    name = models.CharField(max_length=122, default='Portfolio')
    description = models.TextField(default='No description')
    rating = models.IntegerField(default=0)
    client = models.CharField(max_length=50, default='Private')
    url = models.CharField(max_length=100, default='No url')
    completed = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name
    

class Feature(models.Model):
    icon = models.CharField(max_length=122, default='icon' )
    name = models.CharField(max_length=122, default='Feature')
    description = models.TextField(default='No description')

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=122)
    image = models.ImageField(upload_to='testimonials')
    testimony = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Exhibition(models.Model):
    image = models.ImageField(upload_to='exhibitions')
    highlight = models.CharField(max_length=122, default='Nice Exhibition')
    description = models.TextField(default="This is a nice exhibition")
    category = models.CharField(max_length=50, default='Category')
    completed = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.highlight
    

class Partner(models.Model):
    name = models.CharField(max_length=122, default='Partner')
    image = models.ImageField(upload_to='partners')
    url = models.CharField(max_length=100, default='No url')

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    icon = models.CharField(max_length=122, default='contact')
    name = models.CharField(max_length=122)
    contact = models.CharField(max_length=122)

    def __str__(self):
        return self.name

    
class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=122)
    answer = models.TextField()

    def __str__(self):
        return self.question
    

class TermOfService(models.Model):
    name = models.CharField(max_length=122, default='Terms of Service')
    description = models.TextField(default='By using the services provided by Data Idea ("the Company"), you agree to comply with and be bound by the following Terms of Service ("TOS"). If you do not agree with these terms, please do not use our services.')

    def __str__(self):
        return self.name
    

class PrivacyPolicy(models.Model):
    name = models.CharField(max_length=122, default='Privacy Policy')
    description = models.TextField(default='By using the services provided by Data Idea ("the Company"), you agree to comply with and be bound by the following Privacy Policy ("Privacy Policy"). If you do not agree with these terms, please do not use our services.')

    def __str__(self):
        return self.name
    

class Feedback(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=244)
    message = models.TextField()

    def __str__(self):
        return self.subject