from tabnanny import verbose
from django.db import models
from django.forms import CharField



class ClientsList(models.Model):
    full_name = models.CharField('Full_name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Date')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('status')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'

class NotActiveClientsList(models.Model):
    full_name = models.CharField('Full_name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Date')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('status')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'not active client'
        verbose_name_plural = 'not active clients'

class ActivePaymentClients(models.Model):
    full_name = models.CharField('Full_name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Date')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('status')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'active payment client'
        verbose_name_plural = 'active payment clients'

class NotActiveLastcallClients(models.Model):
    full_name = models.CharField('Full_name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Date')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('status')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'not active lastcall client'
        verbose_name_plural = 'not active lastcall clients'

class ErrorClients(models.Model):
    full_name = models.CharField('Full_name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Date')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('status')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'error client'
        verbose_name_plural = 'error clients'