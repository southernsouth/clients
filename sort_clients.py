import os, datetime
from pydoc import cli
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram.settings')

import django
django.setup()
from django.core.management.base import BaseCommand
from clients.models import ClientsList, NotActiveClientsList, ActivePaymentClients, NotActiveLastcallClients, ErrorClients

def sort_by_not_active():
    for i in range(ClientsList.objects.count()):
        client = ClientsList.objects.get(id=(i+1))
        if client.status == 0:
            save_not_active_client = NotActiveClientsList(full_name=client.full_name, email=client.email, address=client.address,
            phone_number=client.phone_number, current_balance=client.current_balance, last_payment=client.last_payment,
            reg_date=client.reg_date, lastcall_date=client.lastcall_date, status=client.status)
            save_not_active_client.save()

def sort_by_payment_data():      
    date_now = str(datetime.datetime.today())[:10]
    date_now = [int(date_now[:4]), int(date_now[5:7])]
    date_now[1] -= 6
    if date_now[1] <= 0:
        date_now[1] = 12 + date_now[1]
        date_now[0] -= 1

    for i in range(ClientsList.objects.count()):
        client = ClientsList.objects.get(id=(i+1))
        date = str(client.last_payment)[:10]
        date = [int(date[:4]), int(date[5:7])]

        if date >= date_now:
            save_not_active_client = ActivePaymentClients(full_name=client.full_name, email=client.email, address=client.address,
            phone_number=client.phone_number, current_balance=client.current_balance, last_payment=client.last_payment,
            reg_date=client.reg_date, lastcall_date=client.lastcall_date, status=client.status)
            save_not_active_client.save()

def sort_by_lastcall_date():
    date_now = str(datetime.datetime.today())[:10]
    date_now = [int(date_now[:4]), int(date_now[5:7])]
    date_now[1] -= 6
    if date_now[1] <= 0:
        date_now[1] = 12 + date_now[1]
        date_now[0] -= 1

    for i in range(ClientsList.objects.count()):
        client = ClientsList.objects.get(id=(i+1))
        date = str(client.lastcall_date)[:10]
        date = [int(date[:4]), int(date[5:7])]

        if date <= date_now and client.status == 1:
            save_not_active_client = NotActiveLastcallClients(full_name=client.full_name, email=client.email, address=client.address,
            phone_number=client.phone_number, current_balance=client.current_balance, last_payment=client.last_payment,
            reg_date=client.reg_date, lastcall_date=client.lastcall_date, status=client.status)
            save_not_active_client.save()

def sort_by_error():
    for i in range(ClientsList.objects.count()):
        client = ClientsList.objects.get(id=(i+1))
        if client.current_balance > 0 and client.status == 0:
            save_not_active_client = ErrorClients(full_name=client.full_name, email=client.email, address=client.address,
            phone_number=client.phone_number, current_balance=client.current_balance, last_payment=client.last_payment,
            reg_date=client.reg_date, lastcall_date=client.lastcall_date, status=client.status)
            save_not_active_client.save()
