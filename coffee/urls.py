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
from django.urls import path

from coffee.views.brand import BrandDetailView
from coffee.views.brand import BrandListView
from coffee.views.coffee import CoffeeDetailView
from coffee.views.coffee import CoffeeListView
from coffee.views.legal_entity import EntityDetailView
from coffee.views.legal_entity import EntityListView

app_name = 'coffee'

urlpatterns = [
    path('entity/', EntityListView.as_view(), name='entity-list'),
    path('entity/<int:pk>/', EntityDetailView.as_view(), name='entity-detail'),

    path('brand/', BrandListView.as_view(), name='brand-list'),
    path('brand/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),

    path('coffee/', CoffeeListView.as_view(), name='coffee-list'),
    path('coffee/<int:pk>/', CoffeeDetailView.as_view(), name='coffee-detail')
]
