from asgiref.sync import async_to_sync

from channels.generic.websocket import (
    JsonWebsocketConsumer,
)

from django.db.models import Q
from django.utils import timezone

from .models import (
    ChatRoom,
    ChatMessage,
)


class ChatConsumer(
    JsonWebsocketConsumer
):

    def connect(self):

        self.room_id = (
            self.scope[
                "url_route"
            ]["kwargs"]["room_id"]
        )

        self.user = self.scope["user"]

        if self.user.is_anonymous:

            self.close()
            return

        room_exists = (
            ChatRoom.objects
            .filter(id=self.room_id)
            .filter(
                Q(seller=self.user)
                |
                Q(buyer=self.user)
            )
            .exists()
        )

        if not room_exists:

            self.close()
            return

        self.room_group_name = (
            f"chat-{self.room_id}"
        )

        async_to_sync(
            self.channel_layer.group_add
        )(
            self.room_group_name,
            self.channel_name
        )

        self.accept()


    def disconnect(
        self,
        close_code
    ):

        if hasattr(
            self,
            "room_group_name"
        ):

            async_to_sync(
                self.channel_layer.group_discard
            )(
                self.room_group_name,
                self.channel_name
            )


    def receive_json(
        self,
        content,
        **kwargs
    ):

        message_text = (
            content
            .get("message", "")
            .strip()
        )

        if not message_text:
            return

        room = ChatRoom.objects.get(
            id=self.room_id
        )

        message = ChatMessage.objects.create(
            room=room,
            sender=self.user,
            content=message_text
        )

        async_to_sync(
            self.channel_layer.group_send
        )(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message.content,
                "username": self.user.username,
                "created_at":
                    timezone.localtime(
                        message.created_at
                    ).strftime("%H:%M"),
            }
        )


    def chat_message(
        self,
        event
    ):

        self.send_json({
            "message": event["message"],
            "username": event["username"],
            "created_at": event["created_at"],
        })