from django.shortcuts import render
from django.views.generic import DetailView

from coffee.models.coffee_address import CoffeeAddress as CoffeeAddressModel
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


class CoffeeDetailView(DetailView):
    model = CoffeeAddressModel
    context_object_name = 'coffee'
    template_name = 'coffee/detail.html'
