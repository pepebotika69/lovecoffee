"""
"""
from django.urls import path

from judge.views.auth import LoginFormView, LogoutRedirectView
from judge.views.profile import UpdateProfileView, ProfileDetailView

app_name = 'judge'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutRedirectView.as_view(), name='logout'),

    path('profile/', ProfileDetailView.as_view(), name='profile-show'),
    path('profile/edit/', UpdateProfileView.as_view(), name='profile-edit')
]
