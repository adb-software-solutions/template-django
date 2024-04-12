from django.contrib import admin

from authentication.models import User


class UserAdmin(admin.ModelAdmin[User]):
    list_display = ("email", "is_superuser", "is_staff", "is_active")
    list_filter = ("is_superuser", "is_staff", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
