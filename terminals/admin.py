# terminals/admin.py
from django.contrib import admin
from .models import Terminal, TerminalClientBinding, TerminalApkDistribution


@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ['terminal_code', 'description', 'location', 'is_deleted']
    list_filter = ['is_deleted']
    search_fields = ['terminal_code', 'description']
    actions = ['soft_delete']

    def soft_delete(self, request, queryset):
        queryset.update(is_deleted=True)
    soft_delete.short_description = "Soft delete selected terminals"



@admin.register(TerminalClientBinding)
class TerminalClientBindingAdmin(admin.ModelAdmin):
    list_display = ['terminal', 'client', 'start_date', 'end_date']
    list_filter = ['terminal', 'client']
    search_fields = ['terminal__terminal_code', 'client__name']  # 确保这里使用的是实际的字段名

@admin.register(TerminalApkDistribution)
class TerminalApkDistributionAdmin(admin.ModelAdmin):
    list_display = ['terminal', 'apk']
    list_filter = ['terminal']
    search_fields = ['terminal__terminal_code', 'apk__name']  # 确保这里使用的是实际的字段名