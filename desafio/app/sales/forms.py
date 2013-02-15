# encoding: utf-8
"""
"""

from django import forms

from app.sales.models import Sale
from app.sales.parser import TabFileParser

class ImportSalesForm(forms.Form):
    file = forms.FileField(required=True)

    def clean_file(self):
        file = self.cleaned_data['file']
        parser = TabFileParser(file)
        if not parser.check_file():
            raise forms.ValidationError(u'File is invalid.')
        return file




