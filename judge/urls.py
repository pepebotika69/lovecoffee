"""
"""
from django.urls import path

from judge.views.auth import Login, Logout
from judge.views.profile import Profile, UpdateProfileView

app_name = 'judge'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    path('profile/', Profile.as_view(), name='profile-show'),
    path('profile/edit/<int:pk>/', UpdateProfileView.as_view(), name='profile-edit')
]
