from django.urls import path
from threads.consumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/notification/<str:chat_name>/', ChatConsumer.as_asgi())
]