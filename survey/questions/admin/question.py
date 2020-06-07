# -*- coding: utf-8 -*-
from django.contrib import admin

# # third party
# from adminsortable2.admin import SortableAdminMixin

# # local
from ..models import Question, Choice


class ChoiceInline(admin.TabularInline):
    '''Tabular Inline View for Choice'''

    model = Choice
    min_num = 0
    max_num = 10
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_text')
    list_display_links = ('title_text',)
    inlines = [ChoiceInline]