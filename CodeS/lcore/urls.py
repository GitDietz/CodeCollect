from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views

from .views import (base, blog, home, pdf, services, about, show_pdf,
                    contact, code_list, test, test_multi, code_detail,
                    feature_list, feature_detail)

app_name = 'lcore'
urlpatterns = [
    # path("home", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('about', about, name='about'),
    path('base', base, name='base'),
    re_path('code/(?P<pk>\d+)', code_detail, name='code_detail'),
    path('code_list', code_list, name='code_list'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    re_path('feature/(?P<pk>\d+)', feature_detail, name='feature_detail'),
    path('feature_list', feature_list, name='feature_list'),
    path('home', home, name='home'),
    path('pdf', pdf, name='pdf'),
    path('services', services, name='services'),
    path('test', test, name='test'),
    path('test_multi', test_multi, name='test_multi'),
    re_path('article/(?P<pk>\d+)', show_pdf, name='show_pdf'),
    ]
