# -*- coding: utf-8 -*-
from django.contrib import admin

from ..models import ChoiceAnswer


@admin.register(ChoiceAnswer)
class ChoiceAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'user', 'question')
    list_display_links = ('answer',)
    list_filter = ('user', 'question', 'answer')