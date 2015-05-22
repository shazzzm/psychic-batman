from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Message


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the messenger index")

def inbox(request):
    user_messages = Message.objects.order_by('-time_sent')
    context = {'user_messages' : user_messages}
    return render(request, 'inbox/inbox.html', context)

def message(request):
    if request.method == "GET":
        message_id = request.GET.get("message_id", -1)
        message = get_object_or_404(Message, pk=message_id)
        context = {'message' : message}
        return render(request, 'message/message.html', context)
