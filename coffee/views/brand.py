from django.shortcuts import render

from coffee.persistence.brand.brand import Brand


def index(request):
    return render(request, 'brand/index.html', {
        'brands': Brand.get_brands()
    })
