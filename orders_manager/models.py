# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Product(models.Model):
    code = models.CharField(max_length=128,unique=True, verbose_name=_('code') )
    name = models.CharField(max_length=128,  verbose_name=_('name') )
    price = models.DecimalField(decimal_places=2 ,max_digits=7, verbose_name=_('price') )
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
    def __str__(self):
        return self.code +' - '+self.name

@python_2_unicode_compatible
class OrderRow(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    order = models.ForeignKey('Order', related_name='order_rows')
    class Meta:
        verbose_name = _('row')
        verbose_name_plural = _('rows')
    def __str__(self):
        return '{} - {}'.format(self.product, self.quantity)


@python_2_unicode_compatible
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=512, verbose_name=_('address') )
    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
    @property
    def total(self):
        total = 0
        for obj in self.order_rows.all():
            total += obj.product.price*obj.quantity 
        return total
    def __str__(self):
        return 'Order {:%d/%m/%Y} - {} €'.format(self.date ,self.total)

# Create your models here.
