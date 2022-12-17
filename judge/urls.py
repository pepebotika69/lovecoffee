"""
"""
from django.urls import path

from judge.views.auth import Login, Logout
from judge.views.profile import Profile

urlpatterns = {
    path('login/', Login.as_view(), name='judge-login'),
    path('logout/', Logout.as_view(), name='judge-logout'),

    path('profile/', Profile.as_view(), name='judge-profile'),
}
