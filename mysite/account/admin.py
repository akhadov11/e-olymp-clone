from django.contrib import admin

from .models import (
    Account, Country
)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'institution', 'city', 'country')
    list_filter = ('city', 'country', )


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(Account, AccountAdmin)
admin.site.register(Country, CountryAdmin)



