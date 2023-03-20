from app.consumers import MyConsumer , MyAsynConsumer

urlpatterns=[
    path('ws/msg/' , MyConsumer.as_asgi()),   
    path('ws/amsg/' , MyAsynConsumer.as_asgi()),   
] 