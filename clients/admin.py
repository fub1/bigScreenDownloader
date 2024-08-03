# clients/admin.py
from django.contrib import admin
from .models import Client, ClientLog

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['identifier','client_android_api', 'created_at', 'is_deleted', ]
    readonly_fields = ['identifier', 'client_android_api', 'created_at',  'client_android_api']
    actions = ['soft_delete']

    def soft_delete(self, request, queryset):
        queryset.update(is_deleted=True)
    soft_delete.short_description = "Soft delete selected clients"

@admin.register(ClientLog)
class ClientLogAdmin(admin.ModelAdmin):
    list_display = ['client', 'ip', 'logged_at']
    readonly_fields = ['client', 'ip', 'logged_at']
    exclude = ['client']  # Assuming you want to hide the client editing

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False