# encoding: utf-8
"""
Views for sales app
"""
from decimal import Decimal
from django.core.urlresolvers import reverse
from django.views.generic import FormView

from app.sales.models import Sale
from app.sales.forms import ImportSalesForm
from app.sales.parser import TabFileParser


class ImportSalesView(FormView):
    '''
    View to show sales and upload a tab file to be processed
    '''
    form_class = ImportSalesForm
    success_url = 'sales_import'
    template_name = 'sales/import.html'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        file = form.cleaned_data['file']
        parser = TabFileParser(file)
        for sale in parser.sales():
            sale.save()
        return super(ImportSalesView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Sale.objects.all()
        kwargs['total_sales'] = self.get_total_sales()
        return super(ImportSalesView, self).get_context_data(**kwargs)

    def get_total_sales(self):
        total = Decimal('0.0')
        for sale in Sale.objects.all():
            total += sale.purchase_count * sale.item_price
        return total

import_sales = ImportSalesView.as_view()
