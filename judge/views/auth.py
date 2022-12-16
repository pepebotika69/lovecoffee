from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView


class Login(APIView):
    """Login"""

    @staticmethod
    def get(request):
        return render(
            request,
            'profile/login.html'
        )

    @staticmethod
    def post(request):
        user: User = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/judge/profile/')


class Logout(APIView):
    """Logout"""

    @staticmethod
    def get(request):
        logout(request)
        return HttpResponseRedirect('/judge/login/')
