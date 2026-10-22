from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.main,
        name="main"
    ),

    path(
        "signup/",
        views.signup,
        name="signup"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    path(
        "",
        views.main,
        name="main"
    ),

    path(
        "products/",
        views.product_list,
        name="product_list"
    ),

    path(
        "products/new/",
        views.product_create,
        name="product_create"
    ),

    path(
        "products/<int:product_id>/",
        views.product_detail,
        name="product_detail"
    ),

    path(
        "products/<int:product_id>/edit/",
        views.product_update,
        name="product_update"
    ),

    path(
        "products/<int:product_id>/delete/",
        views.product_delete,
        name="product_delete"
    ),

    path(
        "products/<int:product_id>/wishlist/",
        views.wishlist_toggle,
        name="wishlist_toggle"
    ),

    path(
        "products/<int:product_id>/chat/",
        views.chat_start,
        name="chat_start"
    ),

    path(
        "chats/",
        views.chat_list,
        name="chat_list"
    ),

    path(
        "chats/<int:room_id>/",
        views.chat_room,
        name="chat_room"
    ),

]