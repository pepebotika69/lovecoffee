from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.views import APIView


class Profile(APIView):
    """Profile"""

    @staticmethod
    @login_required(login_url='/judge/login/')
    def get(request):
        # TODO getting error if not logged
        return render(
            request,
            'profile/profile.html'
        )
