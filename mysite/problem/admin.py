from django.contrib import admin

from .models import (
    ProblemTest, Competition, Problem,
    Classification, Complexity, Status, Bookmark,
    Try, Compiler, Test,
    CompetitionStatus, CompetitionRule, CompetitionType,
)


class ProblemTestAdmin(admin.ModelAdmin):
    list_display = ('compiler', 'test', )
    list_filter = ('compiler',)


class ProblemInLine(admin.TabularInline):
    model = Problem
    raw_id_fields = ('classification', 'status')


class ComplexityAdmin(admin.ModelAdmin):
    inlines = [
        ProblemInLine
    ]
    list_display = ('name', 'description')
    list_filter = ('name',)


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('name', 'classification', 'complexity', 'status', 'bookmarks')
    list_filter = ('name',)


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'rule', 'type', 'status', 'creation_time')
    list_filter = ('name', 'creation_time')


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', )


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', )


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', )


class CompetitionRuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)


class CompetitionStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)


class CompetitionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)


class TryAdmin(admin.ModelAdmin):
    list_display = ('source', 'problem')
    list_filter = ('problem',)


class TestAdmin(admin.ModelAdmin):
    list_display = ('input_data', 'problem')
    list_filter = ('input_data',)


class CompilerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(ProblemTest, ProblemTestAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Complexity, ComplexityAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Try, TryAdmin)
admin.site.register(Compiler, CompilerAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(CompetitionType, CompetitionTypeAdmin)
admin.site.register(CompetitionRule, CompetitionRuleAdmin)
admin.site.register(CompetitionStatus, CompetitionStatusAdmin)
