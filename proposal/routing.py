from django.urls import re_path
from proposal.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/some_path/$', ChatConsumer.as_asgi()),
]