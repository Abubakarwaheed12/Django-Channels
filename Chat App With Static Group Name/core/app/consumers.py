from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer 
from asgiref.sync import async_to_sync
# Sync

class MyConsumer(SyncConsumer):
    
    
    def websocket_connect(self ,event):
        print('websocket connected' , event)
        print('Channel Layer : ' , self.channel_layer)
        print('Channel Name : ' , self.channel_name)
        # Add Channel to A  Group 
        async_to_sync(self.channel_layer.group_add)('test_group' , self.channel_name)
        self.send({ 
            'type':'websocket.accept',
        })
        
        
    def websocket_receive(self ,event):
        print('websocket receive' , event)
        
        async_to_sync(self.channel_layer.group_send)('test_group' , {
            'type':'chat.message',
            'message':event['text']
        })
        
    def chat_message(self , event):
        print(event)
        print('actuall data : ' , event['message'])
        
        self.send({
            'type':'websocket.send',
            'text':event['message'],
        })
         
        
    def websocket_disconnect(self ,event):
        print('websocket Disconnected' , event) 
        print('Channel Layer : ' , self.channel_layer)
        print('Channel Name : ' , self.channel_name)
        # Discard Group
        async_to_sync(self.channel_layer.group_discard)('test_group' , self.channel_name)
        self.send({ 
            'type':'websocket.accept',
        })
        raise StopConsumer()
        
    
    
    
