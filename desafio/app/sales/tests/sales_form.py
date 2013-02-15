# encoding: utf-8
"""
Test for sales forms
"""
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from app.sales.forms import ImportSalesForm

class TestSaleImportForm(TestCase):

    def setUp(self):
        pass

    def test_invalid_file(self):
        'Test with an invalid file'
        upload = open('app/sales/tests/data/invalid_file.tab', 'rb')
        FILES = {'file': SimpleUploadedFile(upload.name, upload.read())}

        form = ImportSalesForm({}, FILES)

        self.assertFalse(form.is_valid())

    def test_valid_file(self):
        'Test with a valid file'
        upload = open('app/sales/tests/data/valid_file.tab', 'rb')
        FILES = {'file': SimpleUploadedFile(upload.name, upload.read())}

        form = ImportSalesForm({}, FILES)

        self.assertTrue(form.is_valid())

