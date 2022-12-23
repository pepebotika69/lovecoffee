from django.shortcuts import render
from django.views.generic import DetailView, ListView

from coffee.models.coffee_address import CoffeeAddress as CoffeeAddressModel
from coffee.persistence.coffee_address.coffee_address import CoffeeAddress
from coffee.views.filters.coffee_address import CoffeeAddressFilter


def index(request):
    # TODO @deprecated
    return render(
        request,
        'coffee/list.html',
        {
            'coffees': CoffeeAddressFilter(request.GET, queryset=CoffeeAddress.get_coffees()).qs
        }
    )


class CoffeeListView(ListView):
    model = CoffeeAddressModel
    template_name = 'coffee/list.html'
    context_object_name = 'coffees'
    paginate_by = 2

class CoffeeDetailView(DetailView):
    model = CoffeeAddressModel
    context_object_name = 'coffee'
    template_name = 'coffee/detail.html'
