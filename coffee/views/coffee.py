from django.shortcuts import render

from coffee.persistence.coffee_address.coffee_address import CoffeeAddress
from coffee.views.filters.coffee_address import CoffeeAddressFilter


def index(request):
    return render(
        request,
        'coffee/index.html',
        {
            'coffees': CoffeeAddressFilter(request.GET, queryset=CoffeeAddress.get_coffees()).qs
        }
    )


def detail(request, pk):
    return render(
        request,
        'coffee/detail.html',
        {
            'coffees': CoffeeAddressFilter(request.GET, queryset=CoffeeAddress.get_coffees()).qs
        }
    )
