from django.shortcuts import render
from .models import Message

# Create your views here.
def index(request):

    if request.user.is_authenticated:
        messages = Message.objects.filter(recipient=request.user.id)
        logged_in = True
    else:
        messages = []
        logged_in = False

    return render(request, 'index.html', {
        'title': 'Send Message',
        'messages': messages,
        'logged_in': logged_in
    })


def send(request):
    return render(request, 'send.html', {
        'title': 'Send Message'
    })


def read(request, id):
    message = Message.objects.get(pk=id)
    print(message)
    return render(request, 'read.html', {
        'title': 'Send Message',
        'message': message
    })