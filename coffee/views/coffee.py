from django.shortcuts import render

from coffee.persistence.coffee_address.coffee_address import CoffeeAddress


def index(request):
    return render(request, 'coffee/index.html', {
        'coffees': CoffeeAddress.get_coffees()
    })
