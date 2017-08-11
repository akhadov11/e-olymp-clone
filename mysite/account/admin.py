from django.db.models import Count
from django.contrib import admin

from .models import (
    Account, Country
)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'institution', 'city', 'country')
    list_filter = ('city', 'country', )


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_users')
    list_filter = ('name',)

    def number_of_users(self, obj):
        return obj.accounts_count

    def get_queryset(self, request):
        return Country.objects.annotate(
            accounts_count=Count('account')
        )

admin.site.register(Account, AccountAdmin)
admin.site.register(Country, CountryAdmin)



