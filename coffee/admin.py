from django.contrib import admin

from coffee.models.brand import Brand
from coffee.models.coffee_address import CoffeeAddress
from coffee.models.legal_entity import LegalEntity

admin.site.register(CoffeeAddress)
admin.site.register(LegalEntity)
admin.site.register(Brand)
