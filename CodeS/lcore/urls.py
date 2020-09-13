from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views

from .views import base, blog, home, pdf, services, about, show_pdf, contact

app_name = 'lcore'
urlpatterns = [
    # path("home", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('about', about, name='about'),
    path('base', base, name='base'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('home', home, name='home'),
    path('pdf', pdf, name='pdf'),
    path('services', services, name='services'),
    re_path('article/(?P<pk>\d+)', show_pdf, name='show_pdf'),
    ]
