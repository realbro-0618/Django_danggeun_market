from django.contrib import admin

from .models import Profile

from .models import (
    Product,
    Wishlist,
    ChatRoom,
    ChatMessage,
)

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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "title",
        "seller",
        "region",
        "price",
        "negotiable",
        "view_count",
        "created_at",
    ]

    search_fields = [
        "title",
        "content",
        "seller__username",
        "region",
    ]

    list_filter = [
        "negotiable",
        "region",
        "created_at",
    ]


admin.site.register(Wishlist)
admin.site.register(ChatRoom)
admin.site.register(ChatMessage)