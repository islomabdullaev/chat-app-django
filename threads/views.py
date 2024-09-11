from django.http import HttpResponse
from django.shortcuts import redirect, render

from threads.models import Chat, Message


def homeView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        chat_name = request.POST.get("chat")

        try:
            chat = Chat.objects.get(name=chat_name)
        except Chat.DoesNotExist:
            Chat.objects.create(name=chat_name)
        
        return redirect("threads", chat_name=chat_name, username=username)

    return render(request, "index.html")

def threadView(request, chat_name: str, username: str):
    chat = Chat.objects.get(name=chat_name)
    messages = Message.objects.filter(chat=chat)

    context = {
        "messages": messages,
        "user": username,
        "chat_name": chat_name
    }
    
    return render(request, "_message.html", context=context)