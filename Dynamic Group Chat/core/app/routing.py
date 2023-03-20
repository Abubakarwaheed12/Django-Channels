from app.consumers import MyConsumer 
from django.urls import path 

urlpatterns=[
    path('ws/chat/<str:group_name>', MyConsumer.as_asgi()),   
] 