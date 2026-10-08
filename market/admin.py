from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "birth_date",
        "phone",
    ]

    search_fields = [
        "user__username",
        "user__first_name",
        "phone",
    ]