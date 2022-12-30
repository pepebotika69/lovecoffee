from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormView

from lovecoffee.forms.contact import ContactForm


class ContactFormView(FormView):
    template_name = 'basic/contact.html'
    form_class = ContactForm

    # TODO suares надо понять как использовать это
    # success_url = reverse('lovecoffee-home')

    def form_valid(self, form):
        form = ContactForm(self.request.POST)
        # TODO suares looks like this validation is not necessary. We access to form_valid only if form is valid
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin_from@example.com', ['admin_to@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponseRedirect(reverse('lovecoffee-home'))

        # TODO suares походу сделано не очень, то есть если все ок то делаем редирект, зачем тогда этот return
        return super().form_valid(form)
