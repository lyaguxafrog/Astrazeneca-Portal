from dataclasses import field
from django.contrib import admin
from pages.models import ContentBlock, Articles
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.db import models


class ContentBlockInlineForm(forms.ModelForm):
    class Meta:
        model = ContentBlock
        fields = '__all__'
        widgets = {
            'text': CKEditorWidget(),
        }


class ContentBlockInline(admin.StackedInline):
    model = ContentBlock
    extra = 0
    form = ContentBlockInlineForm
    verbose_name = "Блок контента"


class ArticlesAdminForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
        widgets = {
            'final_content': CKEditorWidget(),
        }

class ArticlesAdmin(admin.ModelAdmin):
    form = ArticlesAdminForm
    inlines = [ContentBlockInline]

    fieldsets = [
        ('Основная информация', {'fields': ['article_name', 'cover', 'short_description', 'information', 'first_abzac']}),
        ('Дополнительная информация', {'fields': ['final_content', 'access_number', 'speciality', 'drug', 'article_type']}),
    ]

    # def get_formsets_with_inlines(self, request, obj=None):
    #     for inline in self.get_inline_instances(request, obj):
    #         yield inline.get_formset(request, obj), inline


admin.site.register(Articles, ArticlesAdmin)
