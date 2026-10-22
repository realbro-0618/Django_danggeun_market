from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    birth_date = models.DateField(
        verbose_name="생년월일"
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="휴대폰번호"
    )

    def __str__(self):
        return self.user.username

class Product(models.Model):

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products"
    )

    title = models.CharField(
        max_length=100
    )

    content = models.TextField()

    image_url = models.URLField(
        blank=True,
        null=True
    )

    region = models.CharField(
        max_length=100
    )

    price = models.PositiveIntegerField()

    negotiable = models.BooleanField(
        default=False
    )

    view_count = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @property
    def wish_count(self):
        return self.wishlists.count()

    @property
    def chat_count(self):
        return self.chat_rooms.count()


class Wishlist(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="wishlists"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="wishlists"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "product"],
                name="unique_user_product_wishlist"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"


class ChatRoom(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="chat_rooms"
    )

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="selling_chat_rooms"
    )

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="buying_chat_rooms"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "buyer"],
                name="unique_product_buyer_chatroom"
            )
        ]

    def __str__(self):
        return f"{self.product.title} / {self.seller.username} - {self.buyer.username}"


class ChatMessage(models.Model):

    room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="chat_messages"
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.sender.username}: {self.content[:20]}"