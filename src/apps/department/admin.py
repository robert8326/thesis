from django.contrib import admin

from apps.department.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
