from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from home.models import (
    Position,
    TaskType,
    Task, Worker
)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["id", "position"]


@admin.register(TaskType)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "deadline", "is_completed"]
    list_filter = ["name", "deadline", "is_completed"]
    search_fields = ["name"]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )

