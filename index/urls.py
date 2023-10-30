from . import views
from django.urls import (path, include)

app_name = 'index'

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='services', view=views.services, name='services'),
    path(route='about', view=views.about, name='about'),
    path(route='contact', view=views.contact, name='contact'),
    path(route='portfolio', view=views.portfolio, name='portfolio'),
    path(route='terms-of-service', view=views.termsOfService, name='terms_of_service'),
    path(route='privacy-policy', view=views.privacyPolicy, name='privacy_policy'),
    path(route='portfolio-details/<int:id>', view=views.portfolioDetails, name='portfolio_details'),
    path(route='not-allowed', view=views.notAllowed, name='not_allowed'),
    path(route='paid-feature', view=views.paidFeature, name='paid_feature'),
    path(route='sitemap', view=views.sitemap, name='sitemap'),
    path(route='sitemap.xml', view=views.sitemap, name='sitemap'),
    path(route='robots', view=views.robots, name='robots'),
    path(route='robots', view=views.robots, name='robots'),
    path(route='ads', view=views.ads, name='ads'),
    path(route='Ads', view=views.ads, name='ads'),
    path(route='ads.txt', view=views.ads, name='ads'),
    path(route='Ads.txt', view=views.ads, name='ads'),
]