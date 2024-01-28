# -*- coding: utf-8 -*-


from django.contrib import admin
from pages.models import ContentBlock, Articles
from ckeditor.widgets import CKEditorWidget
from django import forms


class ContentBlockInlineForm(forms.ModelForm):
    class Meta:
        model = ContentBlock
        fields = '__all__'
        widgets = {
            'text': CKEditorWidget(),
        }

class ContentBlockInline(admin.TabularInline):
    model = ContentBlock
    extra = 0
    form = ContentBlockInlineForm


class ArticlesAdminForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
        widgets = {
            'final_content': CKEditorWidget(),
            'article_name': forms.Textarea(attrs={'rows': 2, 'cols': 52}),
        }

class ArticlesAdmin(admin.ModelAdmin):
    form = ArticlesAdminForm
    list_display = ('article_name', 'article_type')
    inlines = [ContentBlockInline]

    fieldsets = [
        ('Основная информация', {'fields': ['article_name', 'cover_desktop',
                                    'cover_mobile', 'main_cover_desktop',
                                    'main_cover_mobile',
                                    'information', 'first_abzac']}),
        ('Дополнительная информация', {'fields': ['final_content',
                                                  'access_number',
                                                  'speciality', 'drug',
                                                  'article_type','center_title',
                                                  'priority']}),
    ]


admin.site.register(Articles, ArticlesAdmin)
