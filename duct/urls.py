from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView


from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^signup/$', views.signup, name='signup'),
]