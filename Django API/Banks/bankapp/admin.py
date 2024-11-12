from django.contrib import admin
from .models import BankModel

# Register your models here.
@admin.register(BankModel)
class BankModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'ifsc_code')
    search_fields = ('name', 'branch')
    list_filter = ('branch',)
    readonly_fields = ('created_at',)