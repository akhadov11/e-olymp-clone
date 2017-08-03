from django.contrib import admin

from .models import (
    Account, Country
)

admin.site.register(Account)
admin.site.register(Country)
