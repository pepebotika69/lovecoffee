from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView

from judge.forms.login import LoginForm


class LoginFormView(FormView):
    template_name = 'profile/login.html'
    form_class = LoginForm

    # TODO suares надо понять как использовать это
    # success_url = reverse('judge:profile-show')

    def form_valid(self, form):
        user: User = authenticate(username=self.request.POST['username'], password=self.request.POST['password'])

        if user is not None and user.is_active:
            login(self.request, user)
            # TODO suares может быть нужно сделать через success_url
            return HttpResponseRedirect(reverse('judge:profile-show'))

        return super().form_valid(form)


class LogoutRedirectView(RedirectView):
    pattern_name = 'judge:login'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
