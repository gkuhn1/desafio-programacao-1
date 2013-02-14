# encoding: utf-8
"""
Models for sales app
"""


from django.db import models

class Sale(models.Model):
    class Meta:
        db_table = 'app_sales_sale'

    client_name = models.CharField(_(u'Client name'), max_length=100)
    item_description = models.CharField(_(u'Item description'),
        max_length=150)
    item_price = models.DecimalField(_(u'Item price'),
        max_digits=10, decimal_places=2)
    purchase_count = models.IntegerField(_(u'Purchase count'))
    saller_address = models.CharField(_(u'Saller address'), max_length=200)
    saller_name = models.CharField(_(u'Saller name'), max_length=150)

    def __unicode__(self):
        return self.client_name
