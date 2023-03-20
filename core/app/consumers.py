from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer 

# Sync

class MyConsumer(SyncConsumer):
    
    
    def websocket_connect(self ,event):
        print('websocket connected' , event)
        # for making a connection 
        self.send({ 
            'type':'websocket.accept',
        })
        
    def websocket_recieive(self ,event):
        print('websocket receive' , event)
        
    def websocket_disconnect(self ,event):
        print('websocket Disconnected' , event)
        
    
    
    
# Async

class MyAsynConsumer(SyncConsumer):
    
    
    async def websocket_connect(self ,event):
        print('websocket connected' , event)
        # for making a connection 
        await self.send({ 
            'type':'websocket.accept',
        })
        
    async def websocket_recieive(self ,event):
        print('websocket receive' , event)
        
    async def websocket_disconnect(self ,event):
        print('websocket Disconnected' , event)