from channels.routing import ProtocolTypeRouter, URLRouter
# import app.routing
from django.urls import re_path, path
from docs.consumers import TextRoomConsumer as RoomConsumer
# from pet.consumers import TextRoomConsumer as PetConsumer

websocket_urlpatterns = [
    # path('<str:room_name>/', MriConsumer.as_asgi()),
    re_path(r'^request/(?P<owner_name>[^/]+)/$', RoomConsumer.as_asgi()),
    # re_path(r'^pet/(?P<room_name>[^/]+)/$', PetConsumer.as_asgi()),
]

# # the websocket will open at 127.0.0.1:8000/ws/<room_name>
# application = ProtocolTypeRouter({
#     'websocket':
#         URLRouter(
#             websocket_urlpatterns
#         )
#     ,
# })