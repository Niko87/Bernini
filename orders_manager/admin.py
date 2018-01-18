# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

class OrderRowInline(admin.TabularInline):
    model = OrderRow

class OrdersAdmin(admin.ModelAdmin):
    inlines = [ OrderRowInline, ]

class ProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrdersAdmin)
admin.site.register(Product, ProductsAdmin)

# Register your models here.
