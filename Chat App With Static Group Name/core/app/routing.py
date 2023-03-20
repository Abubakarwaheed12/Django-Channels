from app.consumers import MyConsumer 
from django.urls import path 

urlpatterns=[
    path('ws/chat/' , MyConsumer.as_asgi()),   
] 