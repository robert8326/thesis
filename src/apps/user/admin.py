from django.contrib import admin
from django.utils.html import format_html

from apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'department', 'date_joined', 'is_superuser', 'image_tag', 'password')
    list_display_links = ('id', 'username')
    exclude = ('email', 'is_staff', 'is_active', 'groups', 'user_permissions', 'password', 'last_login', 'is_superuser')
    readonly_fields = ('date_joined',)
    search_fields = ('id', 'username', 'first_name')
    list_filter = ('department',)

    def image_tag(self, obj):
        if obj.avatar:
            return format_html(f'<img src="{obj.avatar.url}" width=50 height=50/>')
        return None

    image_tag.short_description = 'Image'
