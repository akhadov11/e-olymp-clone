from django.contrib import admin

from .models.models import Deliberation, Answer


class DeliberationAdmin(admin.ModelAdmin):
    list_display = ('name', 'account')
    list_filter = ('name',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_time', 'answered_by')
    list_filter = ('answer_time', 'answered_by')


admin.site.register(Deliberation, DeliberationAdmin)
admin.site.register(Answer, AnswerAdmin)
