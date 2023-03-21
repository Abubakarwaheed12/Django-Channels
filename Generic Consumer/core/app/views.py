from django.shortcuts import render
from app.models import Chat , Group
# Create your views here.

def home(request , group_name):

    print('Group_Name : ' , group_name)
    
    group=Group.objects.filter(name=group_name).first()
    chats=[]
    if group:
        chats=Chat.objects.filter(group=group)
    else:
        group=Group(name=group_name)
        group.save()
    
    
    context={
        'group_name':group_name,
        'chats':chats,
    }
    
    return render(request, 'index.html' , context)
