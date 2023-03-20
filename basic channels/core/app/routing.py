from app.consumers import MyConsumer , MyAsynConsumer
from django.urls import path 

urlpatterns=[
    path('ws/chat/' , MyConsumer.as_asgi()),   
    path('ws/amsg/' , MyAsynConsumer.as_asgi()),   
] 