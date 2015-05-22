from django.shortcuts import render
from django.http import HttpResponse
from .models import Message


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the messenger index")

def messages(request):
    user_messages = Message.objects.order_by('-time_sent')
    context = {'user_messages' : user_messages}
    return render(request, 'messages/messages.html', context)
