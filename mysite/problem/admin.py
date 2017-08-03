from django.contrib import admin

from .models import (
    ProblemTest, Competition, Problem
)

admin.site.register(ProblemTest)
admin.site.register(Problem)
admin.site.register(Competition)


# class ProblemTestAdmin(admin.ModelAdmin):
#     list_display = ('')