# -*- coding: utf-8 -*-

from django import forms
from ckeditor.widgets import CKEditorWidget
from pages.models import Articles, Drug, Icon

class ArticlesForm(forms.ModelForm):
    article_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Articles
        fields = '__all__'


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = '__all__'

class IconForm(forms.ModelForm):
    class Meta:
        model = Icon
        fields = '__all__'
