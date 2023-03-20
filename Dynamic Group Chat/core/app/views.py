from django.shortcuts import render

# Create your views here.

def home(request , group_name):

    print('Group_Name : ' , group_name)
    
    return render(request, 'index.html' , {'group_name':group_name} )
