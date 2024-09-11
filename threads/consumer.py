import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from threads.models import Chat, Message


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.chat_name = f"chat_{self.scope['url_route']['kwargs']['chat_name']}"
        await self.channel_layer.group_add(self.chat_name, self.channel_name)
        await self.accept()

    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.chat_name, self.channel_name)
    

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json

        event = {
            'type': 'send_message',
            'message': message
        }

        await self.channel_layer.group_send(self.chat_name, event)
    

    async def send_message(self, event):
        data = event['message']
        await self.create_message(data=data)
        response_data = {
            'user': data['user'],
            'message': data['message']
        }
        await self.send(text_data=json.dumps({'message': response_data}))
    

    @database_sync_to_async
    def create_message(self, data):
        get_chat_by_name = Chat.objects.get(name=data['chat_name'])
        if not Message.objects.filter(message=data['message']).exists():
            new_message = Message(chat=get_chat_by_name, user=data['user'], message=data['message'])
            new_message.save()