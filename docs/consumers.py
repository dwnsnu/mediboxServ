import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class TextRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.owner_name = self.scope['url_route']['kwargs']['owner_name']
        self.owner_group_name = 'owner_%s' % self.owner_name

        # Join room group
        await self.channel_layer.group_add(
            self.owner_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.owner_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type = text_data_json['type']
        text = text_data_json['text']
        sender = text_data_json['sender']

        # Send message to room group
        await self.channel_layer.group_send(
            self.owner_group_name,
            {
                'type': type,
                'message': text,
                'sender': sender
            }
        )

    # Receive message from room group
    async def permission(self, event):
        type = event['type']
        text = event['message']
        sender = event['sender']
        owner = self.owner_name

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            # 'text': text,
            'type': type,
            'text': 'Confirmed access to ' + sender,
            'sender': owner
        }))