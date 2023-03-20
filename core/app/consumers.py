from channels.consumer import SyncConsumer


class MyConsumer(SyncConsumer):
    
    
    def websocket_connect(self ,event):
        print('websocket connected')
        
    def websocket_recieive(self ,event):
        print('websocket receive')
        
    def websocket_disconnect(self ,event):
        print('websocket Disconnected')
        
    