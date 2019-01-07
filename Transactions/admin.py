from django.contrib import admin
from .models import *


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Transactions._meta.fields]

    class Meta:
        model = Transactions


@admin.register(TypeOperation)
class TypeOperationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TypeOperation._meta.fields]

    class Meta:
        model = TypeOperation
