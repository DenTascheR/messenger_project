from django.shortcuts import render
from .models import Message

def chat_view(request, username):
    messages = Message.objects.filter(sender=request.user, receiver__username=username)
    return render(request, 'chat/chat.html', {'messages': messages})
