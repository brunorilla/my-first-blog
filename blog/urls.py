from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^translate/', views.translate, name='translate'),
    url(r'^about/', views.about, name='about'),
]