from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from vbb_backend.users.models import User, Executive, ProgramManager, ProgramDirector, Headmaster, Teacher, Mentor, Parent, Student


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Management",
            {
                "fields": (
                    "user_type",
                    "personal_email",
                    "verification_level",
                    "first_name",
                    "last_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)

admin.site.register(Executive)
admin.site.register(ProgramManager)
admin.site.register(ProgramDirector)
admin.site.register(Headmaster)
admin.site.register(Teacher)
admin.site.register(Mentor)
admin.site.register(Parent)
admin.site.register(Student)
