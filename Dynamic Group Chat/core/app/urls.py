from django.urls import path
from app.views import home 
urlpatterns=[
    path('<str:group_name>' , home , name='home'),
]