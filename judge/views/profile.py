from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from rest_framework.views import APIView


class Profile(APIView, PermissionRequiredMixin):
    """Profile"""

    @staticmethod
    def get(request):
        print(f'###########################')
        # TODO getting error if not logged
        return render(
            request,
            'profile/profile.html'
        )
