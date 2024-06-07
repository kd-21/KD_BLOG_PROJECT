from django.shortcuts import render

# Create your views here.

# def home_chat(request):
#     context={}
#     return render(request, "chat.html", context)


# from django.shortcuts import render

def home_chat(request):
    return render(request, 'index.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })