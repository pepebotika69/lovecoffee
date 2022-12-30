"""lovecoffee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from lovecoffee.views.basic import ContactFormView

urlpatterns = [
    path('', TemplateView.as_view(template_name='basic/index.html'), name='lovecoffee-home'),
    path('about/', TemplateView.as_view(template_name='basic/about.html'), name='lovecoffee-about'),
    path('services/', TemplateView.as_view(template_name='basic/services.html'), name='lovecoffee-services'),
    path('contact/', ContactFormView.as_view(), name='lovecoffee-contact'),

    path('admin/', admin.site.urls),

    path('coffee/', include('coffee.urls', namespace='coffee')),

    path('judge/', include('judge.urls', namespace='judge')),

    path('rating/', include('rating.urls', namespace='rating'))
]
