from django.contrib import admin

from rating.models.brand import Brand
from rating.models.coffee_address import CoffeeAddress
from rating.models.legal_entity import LegalEntity

admin.site.register(Brand)
admin.site.register(LegalEntity)
admin.site.register(CoffeeAddress)
