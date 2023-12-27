# -*- coding: utf-8 -*-

from django import forms
from ckeditor.widgets import CKEditorWidget
from pages.models import Articles

class ArticlesForm(forms.ModelForm):
    article_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Articles
        fields = '__all__'
