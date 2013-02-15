# encoding: utf-8
"""
Views for sales app
"""

from django.views.generic import FormView

from app.sales.forms import ImportSalesForm


class ImportSalesView(FormView):
    form = ImportSalesForm
    success_url = '/'


import_sales = ImportSalesView.as_view()
