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
    form_class = ImportSalesForm
    success_url = 'sales_import'
    template_name = 'sales/import.html'

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        Sale.objects.all().delete()
        file = form.cleaned_data['file']
        parser = TabFileParser(file)
        self.sales = []
        # from IPython import embed; embed()
        for sale in parser.sales():
            sale.save()
            self.sales.append(sale)
        return super(ImportSalesView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Sale.objects.all()
        total = Decimal('0.0')
        for sale in Sale.objects.all():
            total += sale.purchase_count * sale.item_price
        kwargs['total_sales'] = total
        return super(ImportSalesView, self).get_context_data(**kwargs)

import_sales = ImportSalesView.as_view()
