from django.views.generic import DetailView, ListView

from coffee.models.coffee_address import CoffeeAddress as CoffeeAddressModel
from coffee.persistence.coffee_address.coffee_address import CoffeeAddress
from coffee.views.filters.coffee_address import CoffeeAddressFilter


class CoffeeListView(ListView):
    model = CoffeeAddressModel
    template_name = 'coffee/list.html'
    context_object_name = 'coffees'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        return CoffeeAddressFilter(self.request.GET, queryset=CoffeeAddress.get_coffees()).qs


class CoffeeDetailView(DetailView):
    model = CoffeeAddressModel
    context_object_name = 'coffee'
    template_name = 'coffee/detail.html'
