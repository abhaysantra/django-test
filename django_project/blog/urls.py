from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    # url(r'', views.home, name='blog-home'),
    # url(r'about/', views.about, name='blog-about'),

    # using path
    path('',views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]