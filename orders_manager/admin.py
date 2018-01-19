# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrdersAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'user' , 'date', 'total' ]
    inlines = [ OrderItemInline, ]

class ProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrdersAdmin)
admin.site.register(Product, ProductsAdmin)

# Register your models here.
