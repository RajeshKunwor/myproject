# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
from mptt.models import TreeForeignKey, MPTTModel

# Create your models here.

class MedicineCatetory(MPTTModel):

    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class MPTTMeta:
        order_insertioin_by = ['name']


class Hospital(models.Model):

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Medicine(models.Model):

    name = models.CharField(max_length=50)
    rate = models.FloatField()
    description = models.TextField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Bill(models.Model):

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.id


class MedicinePurchaseAmount(models.Model):

    bill = models.OneToOneField(Bill, on_delete=models.CASCADE, related_name='bill_amount')
    discount = models.FloatField()
    net_total = models.FloatField()

    def __str__(self):
        return "Bill No: "+self.medicine_purchase+"has net total is "+self.net_total


class MedicinePurchase(models.Model):

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bill_medicine_purchase')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='medicine_purchase')
    quantity = models.IntegerField()
    manufacture_date = models.DateField()
    expiry_date = models.DateField()



    def cal_date(self):
        today = date.today()
        diff_date =  self.expiry_date-today
        return diff_date.days

    def __str__(self):
        return self.medicine+"has been purchased in "+ self.created_date


