from django.contrib import admin

from common.models.city import City
from common.models.state import State

admin.site.register(State)
admin.site.register(City)
