from django.shortcuts import render, redirect
from .models import Message, Reply
from .forms import MessageForm, ReplyForm
from pprint import pprint


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
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('/read/{}'.format(message.pk))
    else:
        form = MessageForm()
    return render(request, 'send.html', {
        'title': 'Send Message',
        'form': form
    })


def read(request, id):
    message = Message.objects.get(pk=id)
    replies = Reply.objects.filter(message=message)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.message = message
            reply.author = request.user
            reply.save()
    else:
        form = ReplyForm()


    return render(request, 'read.html', {
        'title': 'Send Message',
        'message': message,
        'form': form,
        'replies': replies
    })
