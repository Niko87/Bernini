# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import serializers, filters, viewsets, routers
from django.contrib.admin.sites import AdminSite
from django.contrib import admin

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

nonadmin.register(Order, OrdersAdmin)

# Create your views here.
