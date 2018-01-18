# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xlwt
import StringIO

from django.shortcuts import render
from rest_framework import serializers, filters, viewsets, routers
from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from forms import *
from models import *
from serializers import *

class ProductApi( viewsets.ModelViewSet):
    '''
        API VIEW
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.OrderingFilter,filters.SearchFilter,)
    search_fields = ('code','name',)
    ordering_fields = ('code','name', 'price')
    filter_fields =('code','name', 'price')


apirouter = routers.SimpleRouter()
apirouter.register(r'products', ProductApi)


class NonAdmin(AdminSite):
    '''
        BUYER VIEW
    '''
    login_form = NonAdminAuthenticationForm
    def has_permission(self, request):
        return request.user.is_active  and not  request.user.is_staff

nonadmin = NonAdmin(name='user_orders')

class OrderRowInline(admin.TabularInline):
    model = OrderRow
    def has_add_permission(self, request):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    def has_change_permission(self, request, obj=None):
        return True

class OrdersAdmin(admin.ModelAdmin):
    inlines = [ OrderRowInline, ]
    fields= ['address']

    def has_module_permission(self, request):
        return True
    def has_add_permission(self, request):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    def has_change_permission(self, request, obj=None):
        return True

    def get_queryset(self, request):
        queryset = super(OrdersAdmin, self).get_queryset(request)
        if not request.user.is_staff:
            return queryset.filter(user=request.user)
        return queryset
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def send_XLSX(self, obj):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Order')
        row = 2
        sheet.write(row, 0 , 'Client:' )
        sheet.write(row, 1 , str(obj.user) )
        row += 1
        sheet.write(row, 0 , 'Address:' )
        sheet.write(row, 1 , obj.address )
        row +=2
        sheet.write(row, 0 , 'Item' )
        sheet.write(row, 1 , 'Quantity' )
        sheet.write(row, 2 , 'Price' )
        row +=1
        
        for item in obj.order_rows.all():
            sheet.write(row, 0 , str(item.product) )
            sheet.write(row, 1 , item.quantity )
            sheet.write(row, 2 , item.subtotal )
            row +=1
        
        sheet.write(row, 1 , 'Total' ) 
        sheet.write(row, 2 , obj.total )
        
        ios = StringIO.StringIO()
        workbook.save(ios)
        file_excel = ios.getvalue()
        ios.close()
        filename = 'order_{}.xls'.format(obj.id)

        subject = 'New order'
        body = 'New order'
        email_message = EmailMultiAlternatives(subject, body, None, [settings.SHOP_EMAIL])
        email_message.attach(*(filename, file_excel ,'application/vnd.ms-excel'))
        email_message.send()

    def save_related(self, request, form, formsets, change):

        super( OrdersAdmin, self ).save_related(request, form, formsets, change)
        print(form.instance.order_rows.all().count())
        self.send_XLSX(form.instance)

							
nonadmin.register(Order, OrdersAdmin)

# Create your views here.
