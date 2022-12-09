from django.shortcuts import render


def index(request):
    return render(request, 'basic/index.html')


def about(request):
    return render(request, 'basic/about.html')


def services(request):
    return render(request, 'basic/services.html')


def contact(request):
    return render(request, 'basic/contact.html')
