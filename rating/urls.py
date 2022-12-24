"""
"""
from django.urls import path

from rating.views.rate import RateEntityView

app_name = 'rating'

urlpatterns = [
    path('do-rate/entity/<int:pk>/', RateEntityView.as_view(), name='entity-rate')
]
