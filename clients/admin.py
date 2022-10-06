from django.contrib import admin
from .models import ClientsList, NotActiveClientsList, ActivePaymentClients, NotActiveLastcallClients, ErrorClients

class ClientListAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')

class NotActiveClientListAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')

class ActivePaymentClientsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')

class NotActiveLastcallClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')

class ErrorClientsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')

admin.site.register(ClientsList, ClientListAdmin)
admin.site.register(NotActiveClientsList, NotActiveClientListAdmin)
admin.site.register(ActivePaymentClients, ActivePaymentClientsAdmin)
admin.site.register(NotActiveLastcallClients, NotActiveLastcallClientAdmin)
admin.site.register(ErrorClients, ErrorClientsAdmin)