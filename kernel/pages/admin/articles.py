from dataclasses import field
from django.contrib import admin
from pages.models import ContentBlock, Articles
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.db import models



class ContentBlockInline(admin.StackedInline):
    model = ContentBlock
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
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
        ('Основная информация', {'fields': ['article_name', 'cover']}),
        ('Дополнительная информация', {'fields': ['short_description','final_content', 'access_number', 'speciality', 'drug', 'article_type']}),
    ]

admin.site.register(Articles, ArticlesAdmin)
